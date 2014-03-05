"""重新建立编号，删除无效编号
"""


from pymongo import MongoClient


class Mov():
    client = MongoClient()
    movie = client.bastogne.movie
    pid = 1

    def change_id(self):
        cursor = self.movie.find()
        for pid, post in enumerate(cursor):
            print(post['id'], pid+1)
            self.movie.update({'id': post['id']}, {'$set': {'id': pid+1}})


if __name__ == '__main__':
    Mov().change_id()
