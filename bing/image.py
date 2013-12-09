"""获取每日bing背景图
    api: http://cn.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1
"""
from xml.etree import ElementTree
from urllib.request import urlopen
from urllib.parse import urlencode


class BingImage():
    #api接口地址
    url = 'http://cn.bing.com/HPImageArchive.aspx?'

    def __init__(self, idx, n):
        self.idx = idx
        self.n = n
        self.data = self.get_data()

    def get_image(self):
        return 'http://s.cn.bing.net' + self.data['url']

    def get_date(self):
        return self.data['enddate']

    def get_copyright(self):
        return self.data['copyright']

    def get_copyright_link(self):
        return self.data['copyrightlink']

    def get_data(self):
        re = self._fetch()
        root = ElementTree.fromstring(re)
        return {child.tag: child.text for child in root[0]}

    def _fetch(self):
        response = urlopen(self._get_url())
        return response.read().decode()

    def _get_url(self):
        data = {
            'format': 'xml',
            'idx': self.idx,
            'n': self.n,
        }
        return self.url + urlencode(data)

if __name__ == '__main__':
    image = BingImage(0, 1)
    print(image.get_image())
    print(image.get_copyright())
    print(image.get_copyright_link())
    print(image.get_date())

