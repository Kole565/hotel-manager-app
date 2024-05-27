"""Provide class for db interaction."""
import psycopg2


class DBManager:
    """Provide helper interface to postgres db."""

    def __init__(self, db_name, user):
        """Initialize data for login into db."""
        self.name = db_name
        self.user = user

        self.connected = False

    def __del__(self):
        """Handle connection closing."""
        self.disconnect()

    def connect(self):
        """Establish and save connection to db."""
        if self.connected:
            return

        self._connection = psycopg2.connect(dbname=self.name, user=self.user)
        self._cursor = self._connection.cursor()

        self.connected = True

    def disconnect(self):
        """Close connection to db."""
        if not self.connected:
            return

        self._cursor.close()
        self._connection.close()

        self.connected = False

    def commit(self):
        """Save last queries results."""
        if not self.connected:
            return

        self._connection.commit()

    def execute_and_return(self, query, args=None):
        """Execute query and return fetched result."""
        self.connect()

        self.execute(query, args)

        result = self.fetch()

        self.disconnect()

        return result

    def execute(self, query, args=None):
        """Execute query."""
        self._cursor.execute(query, args)

    def fetch(self):
        """Return result of fetch operation on db."""
        return self._cursor.fetchall()

    def create_table(self, table_name, columns=[], types=[], temporary=False):
        """Construct table from args."""
        attribute_lines = []
        for column, cell_type in zip(columns, types):
            attribute_lines.append("{} {}".format(column, cell_type))

        attributes = ", ".join(attribute_lines)

        temporary_text = ""
        if temporary:
            temporary_text = "TEMPORARY"

        query = "CREATE {} TABLE {} ({});".format(
            temporary_text, table_name, attributes
        )

        self.execute(query)
