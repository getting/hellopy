import tornado.web
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        authurl = """
            https://openapi.baidu.com/oauth/2.0/authorize?
            response_type=token&
            client_id=OwbgTepPkzjNwRlfUFCAbNGM&
            redirect_uri=oob&
            scope=email&
            display=popup&
            state=xxx"""
        self.write(authurl)


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/login', LoginHandler),
        ]
    )

    tornado.httpserver.HTTPServer(app).listen(10001)
    tornado.ioloop.IOLoop.instance().start()