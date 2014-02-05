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


# User().create_table()
u = User().fm('post')
print(u)
# print(User().get_by_id(2))
