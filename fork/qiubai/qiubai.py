from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup


class Quibai():
    url = 'http://www.qiushibaike.com/'

    def __init__(self, start=1, end=30):
        self.start = start
        self.end = end

    def fork(self, url='8hr/page/'):
        url = self.url + url
        for self.start in range(self.end):
            page_url = url + str(self.start)
            try:
                response = urlopen(page_url)
                result = BeautifulSoup(response.read())
                contents = result.find_all(class_='content')
                for c in contents:
                    if c.string:
                        print(c.string.strip())
            except HTTPError:
                pass

    def fork_24hours(self):
        self.fork(url='hot/page/')

    def fork_week(self):
        self.fork(url='week/page/')

    def fork_month(self):
        self.fork(url='month/page/')


if __name__ == '__main__':
    qiubai = Quibai()
    # qiubai.fork()
    qiubai.fork_24hours()
    # qiubai.fork_week()
    # qiubai.fork_month()




