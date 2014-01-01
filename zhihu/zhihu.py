from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class Zhihu():
    url = 'http://www.zhihu.com/'

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def get_index_page(self):
        response = urlopen(self.url)
        return response.read().decode()

    def search(self, q):
        url = self.url + 'search?'
        query = {
            'q': q,
            'type': 'question',
        }
        response = urlopen(url + urlencode(query))
        result = BeautifulSoup(response.read())
        questions = result.find_all('a', class_='question_link')
        for q in questions:
            print(q.em.next_sibling.string, q['href'])


class Follower():
    pass


if __name__ == '__main__':
    zhihu = Zhihu()
    print(zhihu.search('百度'))