if __name__ == '__main__':
    from greensql import *
else:
    from .greensql import *


class User(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    reg_date = DataTimeField()


User()

