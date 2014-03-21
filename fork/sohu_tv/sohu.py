"""搜狐视频爬虫


@date 2014-03-17
"""
import re
import time
from hashlib import sha1
from threading import Thread
from queue import Queue
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from pymongo import MongoClient
from bs4 import BeautifulSoup


class UrlCollector(Thread):
    """广度优先收集url地址
    """
    #需要处理的url
    pattern = re.compile(r'http://.*tv.sohu.com')

    #需要解析的url规则(需要加入tv_queue的url)
    pattern2 = re.compile('http://.*tv.sohu.com(/us)?/\d*/n?\d*.shtml')

    def __init__(self, queue, tv_queue, start='http://tv.sohu.com'):
        Thread.__init__(self)
        self.queue = queue
        self.tv_queue = tv_queue
        self.db = MongoClient().sohu

        #当数据库不存在任何链接时加入起始url,并加入队列
        if not self.db.url.count():
            self.insert_url(start)
            self.queue.put(start)

    def insert_url(self, url):
        """将url插入数据库"""
        self.db.url.insert({'url': url, 'id': self.hash_url(url)})

    @staticmethod
    def get_html(url):
        """根据url获取整个页面
        """
        response = urlopen(url)
        return response.read()

    @staticmethod
    def hash_url(url):
        """对 url hash 处理
        """
        return sha1(url.encode()).hexdigest()

    def fetch_urls(self, soup):
        """从页面提取合法链接
        过滤无用链接
        """
        aas = soup.find_all('a')
        #匹配所有 tv.sohu.com 下的url
        for a in aas:
            href = a.get('href', '')
            if self.pattern.match(href) is not None:
                u_id = self.hash_url(href)
                result = self.db.url.find_one({'id': u_id})
                if result:
                    print('链接已存在', href)
                else:
                    print('添加链接', href)
                    self.insert_url(href)
                    self.queue.put(href)

                    if self.pattern2.match(href) is not None:
                        self.tv_queue.put(href)

            else:
                print('无效链接', href)

    def run(self):
        while True:
            print('UrlCollector', self.getName(), self.queue.qsize())
            url = self.queue.get()
            print(self.getName(), url)
            html = self.get_html(url)
            soup = BeautifulSoup(html)
            self.fetch_urls(soup)
            self.queue.task_done()
            time.sleep(1)


class Tv(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.tv_queue = tv_queue
        self.db = MongoClient().sohu

    @staticmethod
    def parse(url):
        response = urlopen(url)
        soup = BeautifulSoup(response.read())
        head = soup.head
        data = {}
        metas = head.find_all('meta')
        for n, meta in enumerate(metas):
            if meta.get('name') is None or meta.get('property') is None:
                del metas[n]

            data = {meta.get('name') if meta.get('name') is not None else meta.get('property').strip('og:'): meta['content']
                for meta in metas}
        return data

    def run(self):
        while True:
            print('Tv', self.getName(), self.tv_queue.qsize())
            url = self.tv_queue.get()
            data = self.parse(url)
            self.db.tv.insert(data)
            self.tv_queue.task_done()
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    tv_queue = Queue()
    start_url = 'http://tv.sohu.com/map/'
    for i in range(5):
        url_collector = UrlCollector(start_url)
        url_collector.start()

    for j in range(5):
        tv = Tv()
        tv.start()

    queue.join()
    tv_queue.join()