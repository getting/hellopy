import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class TalkHandler(tornado.websocket.WebSocketHandler):
    message = []

    def open(self):
        self.write_message('已与服务器建立连接')

    def on_message(self, message):
        self.message.append(message)
        for msg in self.message:
            self.write_message(msg)
            print(message)

    def on_close(self):
        self.write_message('已与服务器断开连接')


app = tornado.web.Application(
    handlers=[
        (r"/talk", TalkHandler),
    ]
)


if __name__ == '__main__':
    tornado.httpserver.HTTPServer(app).listen(10005)
    tornado.ioloop.IOLoop.instance().start()

