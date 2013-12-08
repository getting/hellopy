import tornado.ioloop
import tornado.httpserver
import tornado.web
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
        self.render('index.html')


class BitNowHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        #异步
        client = httpclient.AsyncHTTPClient()
        client.fetch('http://blockchain.info/ticker', callback=self.on_response)

        #同步
        #client = httpclient.HTTPClient()
        #response = client.fetch('http://blockchain.info/ticker')
        #data = response.body.decode()
        #self.write(str(data))
        #self.finish()

    def on_response(self, response):
        data = response.body.decode()
        self.write(str(data))
        self.finish()


if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(8088)
    tornado.ioloop.IOLoop.instance().start()