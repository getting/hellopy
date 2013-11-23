"""tornado异步测试

"""

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient, HTTPClient


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write('hello')
        print('index start')
        client = AsyncHTTPClient()
        client.fetch('http://localhost:10002', callback=self.on_response)

    def on_response(self, response):
        self.write(response.body.decode())
        print('index ok')
        self.finish()


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('test is ok')
        print('test is ok')

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/test', TestHandler),
        ]
    )

    tornado.httpserver.HTTPServer(app).listen(10001)
    tornado.ioloop.IOLoop.instance().start()
