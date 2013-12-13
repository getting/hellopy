import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado import httpclient
from tornado import gen


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/now", BitNowHandler),
            (r"/chartapi", ChartApiHandler),
            (r"/chart", ChartHandler),
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
    """使用回调产生实现异步

    """
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


class ChartApiHandler(tornado.web.RequestHandler):
    """采用异步生成器

    """
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        url = 'http://blockchain.info/charts/market-price?format=json'
        client = httpclient.AsyncHTTPClient()
        response = yield gen.Task(client.fetch, url)
        data = response.body.decode()
        self.write(data)
        self.finish()


class ChartHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('chart.html')


if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(8088)
    tornado.ioloop.IOLoop.instance().start()