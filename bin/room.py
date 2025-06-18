import psycopg2


class Room:

    USER_NAME = "kole"
    DB_NAME = "hotel"
    TABLE_NAME = "rooms"

    def __init__(self, price, capacity, location, index=None):
        self._price = price
        self._capacity = capacity
        self._location = location

        if index is None:
            self._index = self._get_index()
            self._increment_index()
        else:
            self._index = index

    def _get_index(self):
        connection = psycopg2.connect(dbname=self.DB_NAME, user=self.USER_NAME)
        cursor = connection.cursor()

        query = "SELECT max_index FROM index WHERE type = 'room'"
        cursor.execute(query)

        index = cursor.fetchone()[0] + 1

        cursor.close()
        connection.close()

        return index

    def _increment_index(self):
        connection = psycopg2.connect(dbname=self.DB_NAME, user=self.USER_NAME)
        cursor = connection.cursor()

        query = "UPDATE index SET max_index = {} WHERE type = 'room'".format(self._get_index())
        cursor.execute(query)

        connection.commit()
        cursor.close()
        connection.close()

    def save(self, folder, db_name="hotel"):
        connection = psycopg2.connect(dbname=self.DB_NAME, user=self.USER_NAME)
        cursor = connection.cursor()

        if not self.table_exist(cursor, self.TABLE_NAME):
            self.create_table()

        query = self._get_save_query(cursor)
        cursor.execute(*query)

        connection.commit()
        cursor.close()
        connection.close()

    def table_exist(self, db_cursor, table_name):
        query = "SELECT EXISTS (SELECT FROM pg_tables WHERE tablename = '{}');".format(table_name)
        db_cursor.execute(query)
        result = db_cursor.fetchone()[0]

        return result

    def create_table(self):
        connection = psycopg2.connect(dbname=self.DB_NAME, user=self.USER_NAME)
        cursor = connection.cursor()

        query = "CREATE TABLE rooms (id serial PRIMARY KEY, price integer, capacity integer, location varchar);"
        cursor.execute(query)

        connection.commit()
        cursor.close()
        connection.close()

    def _get_save_query(self, db_cursor):
        query = "INSERT INTO {} (id, price, capacity, location) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO UPDATE SET price = EXCLUDED.price, capacity = EXCLUDED.capacity, location = EXCLUDED.location;".format(self.TABLE_NAME), (self._index, self._price, self._capacity, self._location)

        return query

    @property
    def index(self):
        return self._index


if __name__ == "__main__":
    room = Room(120, 2, "t", 4)
    room.save("test_data")
