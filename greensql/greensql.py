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
    pass


class CharField():
    pass


class IntField():
    pass


class TextField():
    pass


class DataTimeField():
    pass


class ForeignKeyField():
    pass


class Model():
    def select(self):
        pass

    def fm(self):
        pass

    def where(self):
        pass

    def join(self):
        pass

    def order_by(self):
        pass

    def limit(self):
        pass