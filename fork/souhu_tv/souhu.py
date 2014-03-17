"""
@date 2014-03-17
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from pymongo import MongoClient
from bs4 import BeautifulSoup


class Tv():
    url = 'http://tv.sohu.com/'
    db = MongoClient().souhu

    def __init__(self):
        pass

    def fork(self):
        response = urlopen(self.url)

        soup = BeautifulSoup(response.read())
        hrefs = soup.find_all('a')
        for href in hrefs:
            try:
                url = href['href']
                print(url)

            except KeyError as e:
                pass
        # print(str(hrefs))


if __name__ == '__main__':
    tv = Tv()
    tv.fork()
