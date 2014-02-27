# coding=UTF-8
import qrcode
import StringIO
import tornado.wsgi
import tornado.web
import sae
from sae.storage import Bucket

        
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            code = StringIO.StringIO()
            img = qrcode.make("test")
            img.save(code)
            self.set_header('Content-Type', 'image/jpg; charset=utf-8')
            self.write(code.getvalue())
            code.close()
            
        except Exception as e:
            self.write(e)


app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
    ],
)


application = sae.create_wsgi_app(app)