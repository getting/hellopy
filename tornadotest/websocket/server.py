import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world')


class NowHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message('connect')

    def on_message(self, message):
        self.write_message(message + 'hello')


app = tornado.web.Application(
    handlers=[
        (r"/", IndexHandler),
        (r"/now", NowHandler),
    ]
)


if __name__ == '__main__':
    tornado.httpserver.HTTPServer(app).listen(10000)
    tornado.ioloop.IOLoop.instance().start()

