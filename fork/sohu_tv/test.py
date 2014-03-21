import re
from threading import Thread
from queue import Queue
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from pymongo import MongoClient
from bs4 import BeautifulSoup

db = MongoClient().sohu

urls = db.url.find()


pattern2 = re.compile('http://.*tv.sohu.com(/us)?/\d*/n?\d*.shtml')

queue = Queue()
for url in urls:
    if pattern2.match(url['url']) is not None:
        queue.put(url['url'])


print(queue.qsize())


class Tv(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.tv_queue = queue
        self.db = MongoClient().sohu

    @staticmethod
    def parse(url):
        data = {}
        try:
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
        except Exception as e:
            print(e)
        finally:
            return data

    def run(self):
        while True:
            print('Tv', self.getName(), self.tv_queue.qsize())
            url = self.tv_queue.get()
            data = self.parse(url)
            self.db.tv.insert(data)
            self.tv_queue.task_done()


if __name__ == '__main__':
    for i in range(10):
        tv = Tv(queue)
        tv.start()

