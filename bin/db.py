import psycopg2


class DBManager:

    """Class that provide simple interface to postgres db"""

    def __init__(self, db_name, user):
        self.name = db_name
        self.user = user

        self.connected = False

    def __del__(self):
        self.disconnect()

    def connect(self):
        if self.connected:
            return

        self._connection = psycopg2.connect(dbname=self.name, user=self.user)
        self._cursor = self._connection.cursor()

        self.connected = True

    def disconnect(self):
        if not self.connected:
            return

        self._cursor.close()
        self._connection.close()

        self.connected = False

    def commit(self):
        if not self.connected:
            return

        self._connection.commit()

    def execute_and_return(self, query, args=None):
        self.connect()

        self.execute(query, args)

        result = self.fetch()

        self.disconnect()

        return result

    def execute(self, query, args=None):
        self._cursor.execute(query, args)

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
