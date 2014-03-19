from bs4 import BeautifulSoup
from urllib.request import urlopen


class Parse():
    def __init__(self):
        pass

    def parse(self, url):
        response = urlopen(url)
        soup = BeautifulSoup(response.read())
        title = soup.title.string.strip(' - 搜狐视频')
        print(soup.head)
        # print(title)




a = 'http://tv.sohu.com/20120412/n340313583.shtml'

if __name__ == '__main__':
    parse = Parse()
    parse.parse(a)