# coding=UTF-8
"""利用sinaapp的Storage存储

[doc](http://sae.sina.com.cn/doc/python/storage.html)
"""

from urllib import urlopen
import time
import json
import tornado.wsgi
import tornado.web
import sae
from sae.storage import Bucket


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        bucket = Bucket('file')
       	name = self.get_argument('name')
        url = self.get_argument('url')
        res = urlopen(url)
        bucket.put_object(name, res)
        self.write(json.dumps({'url':bucket.generate_url(name), 'ip': self.request.remote_ip}))


app = tornado.wsgi.WSGIApplication([
    (r"/", IndexHandler),
])

application = sae.create_wsgi_app(app)