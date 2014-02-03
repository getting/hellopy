import mysql.connector
from mysql.connector.errors import Error

__version__ = 0.1
__author__ = 'imaguowei@gmail.com'


def get_version():
    return __version__


class GreenSql():
    conn = ''

    def __init__(self, host, user, password, database, autocommit=True, buffered=True):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.buffered = buffered
        GreenSql.conn = self._connect()

    @staticmethod
    def get_connect():
        if not GreenSql.conn:
            raise Error('database connect error!')
        return GreenSql.conn

    def _connect(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                       autocommit=self.autocommit, buffered=self.buffered)

    def _close(self):
        pass


class Model():
    def __init__(self):
        self.db = GreenSql.get_connect()
        self.select_object = SelectObject(self)

    def select(self, sql=''):
        cur = self.db.cursor()
        print(self.select_object.get_sql())
        cur.execute(self.select_object.get_sql())
        # cur.execute('SELECT * FROM user')
        print(cur.fetchone())
        cur.close()

    def insert(self, sql=''):
        pass

    def update(self, sql=''):
        pass

    def delete(self, sql=''):
        pass

    def fm(self, fm):
        self.select_object.fm = fm

    def where(self, where):
        self.select_object.where = where

    def join(self):
        pass

    def order_by(self, order):
        pass

    def limit(self, start=0, number=1):
        self.select_object.limit = (start, number)

    def create_table(self):
        CreateTable().create_table(self)


class SqlObject():
    def __init__(self, model):
        self.table_name = model.__class__.__name__.lower()


class SelectObject(SqlObject):
    def __init__(self, model):
        self.fm = ''
        self.where = ''
        self.limit = ''
        self.sql = ''
        super.__init__(model)

    def get_sql(self):
        self.sql += 'SELECT * FROM '
        if not self.fm:
            self.fm = self.table_name
        self.sql += self.fm
        return self.sql

    def __str__(self):
        return 'SelectObject:' + self.sql


class DeleteObject(SqlObject):
    pass


class UpdateObject(SqlObject):
    pass


class InsertObject(SqlObject):
    pass


class Field():
    field_type = 'varchar'

    def __init__(self, default=''):
        self.default = default


class CharField(Field):
    field_type = 'varchar'


class IntField(Field):
    field_type = 'int'


class TextField(Field):
    field_type = 'text'


class DataTimeField(Field):
    field_type = 'datetime'


class EmailField(Field):
    field_type = 'email'


class PrimaryKey(Field):
    pass


class ForeignKeyField(Field):
    pass


class CreateTable():
    table_name = ''

    def __init__(self):
        pass

    def create_table_sql(self):
        pass

    def create_table(self, model):
        self.table_name = model.__class__.__name__.lower()