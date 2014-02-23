# coding=UTF-8
import tornado.wsgi
import tornado.web
import sae

        
class IndexHandler(tornado.web.RequestHandler):
    url = 'http://saveimage-file.stor.sinaapp.com/'
    def get(self, num=1):
        ns = range(int(num)*20, int(num)*20+20)
        images = []
        for i in ns:
            images.append(self.url + str(i) + '.jpg')
        self.render('index.html', images=images, page=int(num))
            
            
app = tornado.wsgi.WSGIApplication(
	handlers = [
        (r"/", IndexHandler),
        (r"/([0-9]+)", IndexHandler),
    ], static_path='static', template_path='templates'
)

application = sae.create_wsgi_app(app)