# coding=UTF-8
import json
import base64
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
            text = self.get_argument('t', 'hello world').encode('utf-8')
            format = self.get_argument('f', ' ')

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            img = qr.make_image()
            img.save(code)

            bucket = Bucket('image')
            image_name = base64.urlsafe_b64encode(text) + '.png'
            bucket.put_object(image_name, code.getvalue())
            code.close()
            image_url = bucket.generate_url(image_name)
            if format == 'json':
                self.write(json.dumps({'text': text, 'url': image_url}))
            else:
                self.redirect(image_url)
        except Exception as e:
            self.write(e)


app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
    ],
)


application = sae.create_wsgi_app(app)