from urllib.request import urlopen, Request, HTTPError
import urllib.parse


class Post():
    """数据上传

    """
    #统计计数
    number = 0
    error_number = 0
    #post数据
    data = {}

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post(self, data):
        data = urllib.parse.urlencode(data)
        data = data.encode()
        r = Request(self.url, headers=self.headers)
        try:
            p = urlopen(r, data=data)
            print('第{}条记录上传成功'.format(self.number+1))
            #print(p.read().decode())
        except HTTPError as err:
            print('第{}条记录发生错误:{}'.format(self.number+1, err))
            self.error_number += 1

    def start(self):
        print("<<< 开始上传数据 >>>")
        with open('note.txt') as f:
            for line in f:
                line = line.split(',')
                #print(line)
                self.data['ck'], self.data['note_id'], self.data['note_title'],\
                    self.data['note_text'], self.data['author_tags'], \
                    self.data['author_tags_clone'], self.data['note_privacy'], self.data['note_submit'] = line
                #print(data)
                self.post(self.data)
                self.number += 1
        print('<<<上传完毕！>>>\n共发布 {} 条记录'.format(self.number))
        print('上传成功{}条，失败{}条'.format(self.number-self.error_number, self.error_number))

urls = 'http://www.douban.com/note/create'

header = {
    'Cookie': '填入获取的cookie',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

p = Post(urls, header)
p.start()
