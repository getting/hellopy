from urllib.request import urlopen, HTTPError
from urllib import parse

#登陆认证页面
login_url = 'http://www.douban.com/j/app/login'

channel_list = 'http://www.douban.com/j/app/radio/channels'

data = {
    'app_name': 'radio_desktop_win',
    'version': 100,
    'email': '',
    'password': '',
}

data = parse.urlencode(data).encode()
try:
    r = urlopen(login_url, data)
    print(r.read().decode())
except HTTPError as err:
    print(err)