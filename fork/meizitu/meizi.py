from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://jandan.net/ooxx/page-"
num = 1
for i in range(0, 987):
    r = urlopen(url + str(i)).read().decode()
    b = BeautifulSoup(r)
    imgs = b.select('li p img')
    for img in imgs:
        num += 1
        print(i, num, img)