"""
@date 2014-03-17
"""
import re
from hashlib import sha1
from threading import Thread
from queue import Queue
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from pymongo import MongoClient
from bs4 import BeautifulSoup


# start_url = 'http://tv.sohu.com/'
# 从此页抓取
start_url = 'http://tv.sohu.com/map/'
db = MongoClient().sohu
queue = Queue()
queue.put(start_url)


class UrlCollector(Thread):
    """广度优先收集url地址
    """
    pattern = re.compile(r'http://.*tv.sohu.com')

    def __init__(self):
        Thread.__init__(self)
        self.queue = queue
        self.db = db

    def get_soup(self, url):
        """获取页面 soup
        """
        try:
            response = urlopen(url)
            html = BeautifulSoup(response.read())
            return html
        except URLError as e:
            print(e)

    def fetch_urls(self, soup):
        """从页面提取合法链接
        过滤无用链接
        """
        aas = soup.find_all('a')
        #匹配所有 tv.sohu.com 下的url
        for a in aas:
            try:
                href = a['href']
                if self.pattern.match(href) is not None:
                    u_id = sha1(href.encode()).hexdigest()
                    result = self.db.url.find_one({'id': u_id})
                    if result:
                        # print('链接已存在')
                        pass
                    else:
                        # print(href)
                        result = self.db.url.insert({'url': href, 'id': u_id})
                        self.queue.put(href)
                else:
                    pass
                    # print(href)
            except KeyError as e:
                # print('no href', e)
                pass

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()
            soup = self.get_soup(url)
            self.fetch_urls(soup)


class Tv(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queue = queue
        self.db = db

    def run(self):
        while not self.queue.empty():
            response = urlopen(self.queue.get())
            soup = BeautifulSoup(response.read())
            head = soup.head
            print(head)


if __name__ == '__main__':
    for i in range(10):
        urlCollector = UrlCollector()
        urlCollector.start()

    for i in range(10):
        tv = Tv()
        tv.start()