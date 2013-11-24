from urllib.parse import urlencode
import tornado.web
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        url = 'https://openapi.baidu.com/oauth/2.0/authorize?'
        data = {
            'client_id': '',
            'response_type': 'code',
            #todo 本地回调地址？
            'redirect_uri': '',
        }
        url = url + urlencode(data)
        self.write(url)


class AuthHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument('code', '')
        if code:
            self.write(str(code))
        else:
            self.write('no code')


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/login', LoginHandler),
            (r'/auth', AuthHandler),
        ]
    )

    tornado.httpserver.HTTPServer(app).listen(10001)
    tornado.ioloop.IOLoop.instance().start()