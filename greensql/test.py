from .greensql import *


class User(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    reg_date = DataTimeField()

