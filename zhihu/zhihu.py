from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def get_html(url):
    response = urlopen(url)
    return response.read().decode()


class Zhihu():
    url = 'http://www.zhihu.com/'

    def search(self, q):
        url = self.url + 'search?'
        query = {
            'q': q,
            'type': 'question',
        }

        html = get_html(url + urlencode(query))
        result = BeautifulSoup(html)
        questions = result.find_all('a', class_='question_link')
        for q in questions:
            print(q.em.next_sibling.string, q['href'])


class User():
    def __init__(self, username='', url=''):
        self.username = username
        self.url = url

    def get_answers(self):
        html = get_html(self.url + '/answers')
        return html

    def get_asks(self):
        html = get_html(self.url + '/asks')
        soup = BeautifulSoup(html)
        asks = soup.find_all(class_='zm-profile-section-item zg-clear')
        return asks


if __name__ == '__main__':
    # zhihu = Zhihu()
    # print(zhihu.search('百度'))
    user = User(url='http://www.zhihu.com/people/maguowei')
    print(user.get_asks())


