import mysql.connector


class GreenSql():
    def __init__(self, host, user, password, database, autocommit=True, buffered=True):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.buffered = buffered
        self.conn = self._connect()

    def _connect(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                       autocommit=self.autocommit, buffered=self.buffered)

    def _close(self):
        pass


class Create():
    def create_table(self):
        pass

    def parse_model(self):
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


class PrimaryKey(Field):
    pass


class ForeignKeyField(Field):
    pass


class Model():
    def select(self, sql):
        pass

    def fm(self):
        pass

    def where(self):
        pass

    def join(self):
        pass

    def order_by(self):
        pass

    def limit(self, start=0, number=1):
        pass


class SelectObject():
    pass