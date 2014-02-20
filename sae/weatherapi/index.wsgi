# coding=UTF-8
import urllib
import tornado.wsgi
import tornado.web
import sae
from weather import Weather

        
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        location = self.get_argument('q', u'北京')
        location = location.encode('utf-8')

        try:
            w = Weather('873a531cec3212a4906a683572b248b5')
            data = w.get_weather(location)
            self.write(data)
        except Exception as e:
            self.write(e)
            

app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
    ],
)



application = sae.create_wsgi_app(app)