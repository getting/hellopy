# coding=UTF-8
import json
from urllib import urlopen
import tornado.wsgi
import tornado.web
import sae
from sae.storage import Bucket
from bing.image import BingImage

        
class IndexHandler(tornado.web.RequestHandler):
    def get(self, num=0):
        try:
            #直接输出
            #image = urlopen(BingImage(num).get_image())
            #self.set_header('Content-Type', 'image/jpg; charset=utf-8')
            #self.write(image.read())

            #跳转链接
            image = BingImage(num).get_image()
            self.redirect(image)
        except Exception as e:
            self.write(e)


class SaveImageHandler(tornado.web.RequestHandler):
    def get(self):
        #存储今日图片
        bucket = Bucket('image')
        bing = BingImage(0, 1)
        re = urlopen(bing.get_image())
        image_name = str(bing.get_date()) + '.jpg'
        bucket.put_object(image_name, re)
        self.write(json.dumps({'url': bucket.generate_url(image_name)}))


app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
        (r"/([0-9]+)", IndexHandler),
        (r"/save_image", SaveImageHandler),
    ],
)



application = sae.create_wsgi_app(app)