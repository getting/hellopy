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
            text = self.get_argument('t', 'hello world')

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            img = qr.make_image()
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