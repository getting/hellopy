if __name__ == '__main__':
    from greensql import *
else:
    from .greensql import *


GreenSql('localhost', 'root', 'root', 'test')


class User(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    reg_date = DataTimeField()


User().create_table()
User().select()