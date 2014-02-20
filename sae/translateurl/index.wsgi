# coding=UTF-8
import json
import tornado.wsgi
import tornado.web
import sae
from baidu.translate import BaiduTranslate

        
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        word = self.get_argument('q', u'你好世界')
        word = word.encode('utf-8')

        try:
            result = BaiduTranslate('OwbgTepPkzjNwRlfUFCAbNGM').translate(word).replace(' ', '-')
            
            self.write(json.dumps({'in': word, 'out': result}))
        except Exception as e:
            self.write(e)
            

app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
    ],
)



application = sae.create_wsgi_app(app)