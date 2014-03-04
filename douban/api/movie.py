"""豆瓣电影
"""

from urllib.request import urlopen
from urllib.parse import urlencode


class Movie():
    url = 'https://api.douban.com/v2/movie/search?'

    def __init__(self):
        pass

    def get_movie(self, name):
        data = {
            'q': name,
        }
        url = self.url + urlencode(data)

        response = urlopen(url)
        print(response.read().decode())


if __name__ == '__main__':
    movie = Movie()
    movie.get_movie('阿甘正传')
