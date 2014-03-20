from bs4 import BeautifulSoup
from urllib.request import urlopen


class Parse():
    """
    收集的信息
    ('og:title', 'keywords', 'description', 'og:url', 'og:type', 'og:video', 'og:image') =>
    ('title', 'keywords', 'description', 'url', 'type', 'video', 'image')
    """
    def parse(self, url):
        response = urlopen(url)
        soup = BeautifulSoup(response.read())
        head = soup.head
        data = {}
        metas = head.find_all('meta')
        #
        # for meta in metas:
        #     if meta.get('property') == 'og:title':
        #         data['title'] = meta.get('content').strip(' - 搜狐视频')
        #     elif meta.get('name') == 'keywords':
        #         data['keywords'] = meta.get('content')
        #     elif meta.get('name') == 'description':
        #         data['description'] = meta.get('content')
        #     elif meta.get('property') == 'og:url':
        #         data['url'] = meta.get('content')
        #     elif meta.get('property') == 'og:type':
        #         data['type'] = meta.get('content')
        #     elif meta.get('property') == 'og:video':
        #         data['video'] = meta.get('video')
        #     elif meta.get('property') == 'og:image':
        #         data['image'] = meta.get('content')

        # #上面的更直观？
        for n, meta in enumerate(metas):
            if meta.get('name') is None or meta.get('property') is None:
                del metas[n]

            data = {meta.get('name') if meta.get('name') is not None else meta.get('property').strip('og:'): meta['content']
                for meta in metas}

        print(data)

a = 'http://my.tv.sohu.com/us/50333101/61461681.shtml'

if __name__ == '__main__':
    parse = Parse()
    parse.parse(a)