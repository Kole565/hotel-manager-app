import psycopg2

from bin.exceptions import *


class DB:

    # TODO: Change name to DBManager or DBHelper as more suitable

    def __init__(self, db_name, user):
        self.name = db_name
        self.user = user

        self.connected = False

    def connect(self):
        self._connection = psycopg2.connect(dbname=self.name, user=self.user)
        self._cursor = self._connection.cursor()

        self.connected = True

    def disconnect(self):
        self._cursor.close()
        self._connection.close()

        self.connected = False

    def insert(self, item):
        placeholders = ["%s"] * (len(item.record_attributes))
        query = "INSERT INTO {} VALUES ({})".format(
            item.table_name, *placeholders)

        self.execute(query, item.record_attributes)

    def upsert(self, table):
        raise NotImplemented

    def commit(self):
        if not self.connected:
            return

        self._connection.commit()

    def delete(self, index, table_name):
        raise NotImplemented

    def execute(self, query, *args, **kwargs):
        if not self.connected:
            raise NotConnectedException

        self._cursor.execute(query, *args, **kwargs)

    def fetch(self):
        return self._cursor.fetchall()

    def create_table(self, table_name, columns=[], types=[], temporary=False):
        attribute_lines = []
        for column, cell_type in zip(columns, types):
            attribute_lines.append("{} {}".format(column, cell_type))

        attributes = ", ".join(attribute_lines)

        temporary_text = ""
        if temporary:
            temporary_text = "TEMPORARY"

        query = "CREATE {} TABLE {} ({});".format(temporary_text, table_name, attributes)

        self.execute(query)
