from threading import Thread
from pymongo import MongoClient


db = MongoClient().test

test = db.test


class InsertThread(Thread):
    @staticmethod
    def counter(name):
        ret = db.counters.find_and_modify(query={'id': name}, update={'$inc': {'next': 1}}, upsert=True, new=True)
        return ret['next']

    def run(self):
        test.insert({'id': self.counter("user")})


if __name__ == '__main__':
    for i in range(20):
        insert = InsertThread()
        insert.start()
