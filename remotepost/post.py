from urllib.request import urlopen, Request
import urllib.parse


class Post():
    """数据上传

    """
    #统计计数
    number = 0
    #post数据
    data = {}

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post(self, data):
        data = urllib.parse.urlencode(data)
        data = data.encode()
        r = Request(self.url, headers=self.headers)
        p = urlopen(r, data=data)
        #print(p.read().decode())

    def start(self):
        print("开始上传数据")
        with open('data.txt') as f:
            for line in f:
                line = line.split(',')
                #print(line)
                self.data['title'], self.data['content'], self.data['tags'], self.data['post'] = line
                #print(data)
                self.post(self.data)
                self.number += 1
        print('上传完毕！共发布 {} 条记录'.format(self.number))

url = 'http://mlogtest.sinaapp.com/index.php?post/add'

header = {
    'Cookie': '填写'
}

p = Post(url, header)
p.start()