from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
from mysql.connector import connect, Error


class Quibai():
    url = 'http://www.qiushibaike.com/'
    conn = None

    def __init__(self, start=1, end=281, save=False):
        """
        start 起始页
        end 结束页
        save 是否保存到数据库
        """
        self.start = start
        self.end = end
        self.save = save
        self.get_connect()

    def fork(self, url='8hr/page/'):
        """默认是8小时内容
        fork 不同的内容只需要修改url参数，也可以调用下面的快捷方法
        糗百的页面结构貌似都是相同的，原则上也可以fork history部分，需要判断日期
        """
        cursor = self.conn.cursor()
        sql = 'INSERT INTO `post` (`content`, `image`) VALUES (%s, %s)'
        url = self.url + url
        for self.start in range(self.end):
            page_url = url + str(self.start)
            try:
                response = urlopen(page_url)
                result = BeautifulSoup(response.read())
                contents = result.find_all(class_='content')
                for c in contents:
                    if c.string:
                        title = c.string.strip()
                        p = c.parent
                        thumb = p.find(class_='thumb')
                        if thumb:
                            image = thumb.a.img['src']
                        else:
                            image = ''
                        print(title, image)
                        cursor.execute(sql, (title, image))
            except HTTPError:
                pass
        cursor.close()
        self.conn.close()

    def fork_24hours(self):
        self.fork(url='hot/page/')

    def fork_week(self):
        self.fork(url='week/page/')

    def fork_month(self):
        self.fork(url='month/page/')

    def get_connect(self):
        self.conn = connect(host='localhost', user='root', password='root', buffered=True, autocommit=True, database='qiubai')
        return self.conn


if __name__ == '__main__':
    qiubai = Quibai()
    # qiubai.fork()
    # qiubai.fork_24hours()
    qiubai.fork_week()
    # qiubai.fork_month()