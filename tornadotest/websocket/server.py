import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class TalkHandler(tornado.websocket.WebSocketHandler):
    #记录连接的客户端
    clients = []

    def open(self):
        TalkHandler.clients.append(self)
        self.write_message('已与服务器建立连接')

    def on_message(self, message):
        #向每一个连接的客户端广播消息
        for c in TalkHandler.clients:
            c.write_message(message)

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

