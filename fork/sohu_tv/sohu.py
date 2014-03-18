"""
@date 2014-03-17
"""
import time
import re
from hashlib import sha1
from threading import Thread
from queue import Queue
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from pymongo import MongoClient
from bs4 import BeautifulSoup


# start_url = 'http://tv.sohu.com/'
# #从此页抓取
start_url = 'http://tv.sohu.com/map/'
db = MongoClient().sohu
queue = Queue()
queue.put(start_url)


class GetUrl(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queue = queue
        self.db = db

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()
            try:
                response = urlopen(url)
            except URLError as e:
                print(e, url)
            soup = BeautifulSoup(response.read())
            aas = soup.find_all('a')
            #匹配所有 tv.sohu.com 下的url
            pattern = re.compile(r'http://.*tv.sohu.com')
            for a in aas:
                try:
                    href = a['href']
                    if pattern.match(href) is not None:
                        u_id = sha1(href.encode()).hexdigest()
                        result = self.db.url.find_one({'id': u_id})
                        if result:
                            print('链接已存在')
                        else:
                            print(href)
                            result = self.db.url.insert({'url': href, 'id': u_id})
                            self.queue.put(href)
                    else:
                        pass
                        # print(href)
                except KeyError as e:
                    print('no href', e)


class Tv(Thread):
    db = MongoClient().souhu

    def __init__(self):
        Thread.__init__(self)
        self.queue = queue
        self.db = db

    def run(self):
        while not self.queue.empty():
            response = urlopen(self.queue.get())
            soup = BeautifulSoup(response.read())
            player = soup.select('#playerBar')
            print(player)


if __name__ == '__main__':
    for i in range(30):
        getUrl = GetUrl()
        getUrl.start()
        tv = Tv()
        tv.start()

    # for i in range(30):
    #     tv = Tv()
    #     tv.start()