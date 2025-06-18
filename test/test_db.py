import unittest

from db import DB


class DBItem:

    def __init__(self, data, table_name):
        self.data = data

        self.table_name = table_name

    @property
    def record_attributes(self):
        '''In future DBItem realisation this property should be abstract'''
        return [self.data]


class TestDB(unittest.TestCase):

    # TODO: Change name to DBManager or DBHelper as more suitable

    DB_NAME = "test_db"
    TABLE_NAME = "test_table"
    USER = "test"

    def test_init(self):
        db = DB(db_name=self.DB_NAME, user=self.USER)

        self.assertEqual(db.name, self.DB_NAME)
        self.assertEqual(db.user, self.USER)

    def test_create_table(self):
        db = DB(db_name=self.DB_NAME, user=self.USER)
        db.connect()

        db.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'not_exist_table')")
        is_table_exist_before = db.fetch()[0][0]

        db.create_table(table_name="not_exist_table", columns=["test_data", "number"], types=["text", "int"], temporary=True)
        db.commit()

        db.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'not_exist_table')")
        is_table_exist_after = db.fetch()[0][0]

        db.disconnect()

        self.assertFalse(is_table_exist_before)
        self.assertTrue(is_table_exist_after)

    def test_session(self):
        db = DB(db_name=self.DB_NAME, user=self.USER)

        db.connect()

        self.assertFalse(db._connection.closed)
        self.assertFalse(db._cursor.closed)

        db.disconnect()

        self.assertTrue(db._connection.closed)
        self.assertTrue(db._cursor.closed)

    def test_insert(self):
        db = DB(db_name=self.DB_NAME, user=self.USER)

        db.connect()

        db.execute("SELECT * FROM {};".format(self.TABLE_NAME))
        before = db.fetch()

        db.insert(DBItem("some data", self.TABLE_NAME))

        db.execute("SELECT * FROM {};".format(self.TABLE_NAME))
        after = db.fetch()

        self.assertEqual(len(before), 0)
        self.assertEqual(len(after), 1)


if __name__ == "__main__":
    unittest.main()
