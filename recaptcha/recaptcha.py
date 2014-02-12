from urllib.request import urlopen
from urllib.parse import urlencode
import tornado.httpserver
import tornado.ioloop
import tornado.web


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler)
        ]
        settings = dict(
            template_path="templates",
            static_path="static",
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        url = 'http://www.google.com/recaptcha/api/verify'

        challenge = self.get_argument('recaptcha_challenge_field')
        response = self.get_argument('recaptcha_response_field')

        data = {
            'privatekey': '6Lf6seoSAAAAAAQ46JYdXFoTCe81sqGl-0flrpgk',
            'remoteip': self.request.remote_ip,
            'challenge': challenge,
            'response': response
        }

        res = urlopen(url, data=urlencode(data).encode())
        print(res.readline().decode())


if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(10001)
    tornado.ioloop.IOLoop.instance().start()


