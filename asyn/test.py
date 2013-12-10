"""tornado异步测试
server.py 模拟外部资源提供服务器
当该资源时仍可以相应新的请求 /test

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
