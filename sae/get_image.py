# coding=UTF-8
"""利用sinaapp的Storage存储

[doc](http://sae.sina.com.cn/doc/python/storage.html)
"""

import tornado.wsgi
import tornado.web
import sae
from sae.storage import Bucket


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        bucket = Bucket('image')
        from urllib import urlopen
        re = urlopen('http://s.cn.bing.net/az/hprichbg/rb/TianyuHan_ZH-CN8095317153_1366x768.jpg')
        bucket.put_object('a.jpg', re)
        self.write(bucket.generate_url('t.py'))


app = tornado.wsgi.WSGIApplication([
    (r"/", IndexHandler),
])

application = sae.create_wsgi_app(app)