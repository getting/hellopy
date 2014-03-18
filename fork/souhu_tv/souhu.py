"""
@date 2014-03-17
"""
import time
import re
from threading import Thread
from queue import Queue
from urllib.request import urlopen
from urllib.error import HTTPError
from pymongo import MongoClient
from bs4 import BeautifulSoup


start_url = 'http://tv.sohu.com/'
db = MongoClient().souhu
queue = Queue()
queue.put(start_url)


class GetUrl(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            response = urlopen(self.queue.get())
            soup = BeautifulSoup(response.read())
            aas = soup.find_all('a')
            for a in aas:
                try:
                    href = a['href']
                    pattern = re.compile(r'http://.*tv.sohu.com')
                    if pattern.match(href) is not None:
                        # print(href)
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
    for i in range(10):
        getUrl = GetUrl()
        getUrl.start()

    for i in range(10):
        tv = Tv()
        tv.start()