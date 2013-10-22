import re
import urllib.error
from urllib.request import *

ui = 'http://www.36kr.com/p/'

pattern = re.compile('<h1 class="entry-title sep10">(.*?)</h1>', re.DOTALL)

for i in range(206900, 206954):
    url = ui + str(i) + '.html'
    try:
        page = urlopen(url)
        if page.getcode() != 404:
            page = page.read().decode('utf-8')
            match = pattern.search(page)
            if match:
                print(match.group(1).strip())
    except urllib.error.HTTPError:
        pass
