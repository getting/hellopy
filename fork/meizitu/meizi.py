from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from bs4 import BeautifulSoup


url = "http://jandan.net/ooxx/page-"
num = 2259
for i in range(997, 1058):
    try:
        r = urlopen(url + str(i)).read().decode()
        b = BeautifulSoup(r)
        imgs = b.select('li p img')
        for img in imgs:
            num += 1
            print(i, num, img['src'])

            #存储到SAE
            data = {
                'name': str(num) + '.jpg',
                'url': img['src'],
            }
            urlopen('http://saveimage.sinaapp.com/?' + urlencode(data))
    except HTTPError as e:
        pass