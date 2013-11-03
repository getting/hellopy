from urllib.request import urlopen, Request
import urllib.parse

urls = 'http://mlogtest.sinaapp.com/index.php?post/add'

header = {
    'Cookie': 'saeut=123.233.148.77.1383310445502151; PHPSESSID=2574f32d41f70976d973cdc1567dbb48'
}


def post(url, data, headers):
    data = urllib.parse.urlencode(data)
    data = data.encode()
    r = Request(url, headers=headers)
    p = urlopen(r, data=data)
    #print(p.read().decode())


def start():
    number = 0
    data = {}
    print("开始上传数据")
    with open('data.txt') as f:
        for line in f:
            line = line.split(',')
            #print(line)
            data['title'], data['content'], data['tag'], data['post'] = line
            #print(data)
            post(urls, data, header)
            number += 1
    print('上传完毕！共发布 {} 条记录'.format(number))

start()