import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.websocket
from tornado import httpclient


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/now", BitNowHandler),
        ]
        settings = dict(
            template_path="templates",
            static_path="static",
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('websocket.html')


class BitNowHandler(tornado.websocket.WebSocketHandler):
    clients = []
    data = dict()

    def open(self):
        print(str(id(self)) + '建立连接')
        BitNowHandler.clients.append(self)

    def on_message(self, message):
        BitNowHandler.send_to_all(BitNowHandler.data)

    @staticmethod
    def send_to_all(message):
        for c in BitNowHandler.clients:
            c.write_message(message)

    def on_close(self):
        print(str(id(self)) + '退出连接')
        BitNowHandler.clients.remove(self)

    def fetch(self):
        client = httpclient.HTTPClient()
        response = client.fetch('http://blockchain.info/ticker')
        data = response.body.decode()
        return str(data)


if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
