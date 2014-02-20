# coding=UTF-8
import urllib
import tornado.wsgi
import tornado.web
import sae
from bing.image import BingImage

        
class IndexHandler(tornado.web.RequestHandler):
    def get(self, num=0):
        try:
            #image = urllib.urlopen(BingImage(num).get_image())
            #self.set_header('Content-Type', 'image/jpg; charset=utf-8')
            #self.write(image.read())
            #跳转
            image = BingImage(num).get_image()
            self.redirect(image)
        except Exception as e:
            self.write(e)
            

app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
        (r"/([0-9]+)", IndexHandler),
    ],
)



application = sae.create_wsgi_app(app)