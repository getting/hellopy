from urllib.request import urlopen


class Book():
    url = 'https://api.douban.com/v2/book/'

    def __init__(self):
        pass

    def get_book_by_id(self, bid):
        result = urlopen(self.url + str(bid)).read().decode()
        print(result)


if __name__ == '__main__':
    Book().get_book_by_id(1003078)

