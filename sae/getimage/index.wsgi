# coding=UTF-8
"""利用sinaapp的Storage存储

[doc](http://sae.sina.com.cn/doc/python/storage.html)
"""

from urllib import urlopen
import tornado.wsgi
import tornado.web
import sae
from sae.storage import Bucket
from bing.image import BingImage


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        bucket = Bucket('image')
        bing = BingImage(0, 1)
        re = urlopen(bing.get_image())
        image_name = str(bing.get_date()) + '.jpg'
        bucket.put_object(image_name, re)
        self.write(bucket.generate_url(image_name))


app = tornado.wsgi.WSGIApplication([
    (r"/", IndexHandler),
])

application = sae.create_wsgi_app(app)