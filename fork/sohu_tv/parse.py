from bs4 import BeautifulSoup
from urllib.request import urlopen



url = 'http://tv.sohu.com/20120412/n340313583.shtml'


response = urlopen(url)
soup = BeautifulSoup(response.read())
title = soup.title.string.strip(' - 搜狐视频')
print(soup.head)
# print(title)

