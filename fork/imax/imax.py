from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


class IMax():
    url = 'http://imax.im/movies/'
    error_number = 0

    def __init__(self, start=1, end=16097):
        self.start = start
        self.end = end

    def fork(self):
        for i in range(self.start, self.end):
            try:
                response = urlopen(self.url + str(i))
                restlt = BeautifulSoup(response.read())
                title = restlt.title.string
                #print(i, 'success', title[:title.find('|')])
                print(i, 'success', title.strip('| 高清 BT下载,电驴下载,迅雷下载,在线观看 | IMAX.im'))
                table = restlt.find('table', class_='table table-striped table-condensed')
                trs = table.select('tbody tr')
                for tr in trs:
                    tds = tr.find_all('td')
                    for td in tds:
                        if td['class'][0] == 'qu':
                            print(td.string.strip())
                        elif td['class'][0] == 'size':
                            print(td.span.string)
                        elif td['class'][0] == 'name':
                            print(td.a.string)
                            print(td.a['href'])

                    print('>>>>>>>>>>>>')
            except HTTPError as e:
                self.error_number += 1
                print(i, e)

        print(self.error_number)


if __name__ == '__main__':
    imax = IMax(1, 3)
    imax.fork()