"""Tests for db helper."""
import unittest

from bin.db import DBManager


class TestDBManager(unittest.TestCase):
    """Test db helper class."""

    DB_NAME = "test_db"
    TABLE_NAME = "test_table"
    USER = "test"

    def test_init(self):
        """Test initial data saving."""
        db = DBManager(db_name=self.DB_NAME, user=self.USER)

        self.assertEqual(db.name, self.DB_NAME)
        self.assertEqual(db.user, self.USER)

    def test_create_table(self):
        """Test table creation."""
        db = DBManager(db_name=self.DB_NAME, user=self.USER)
        db.connect()

        query = "SELECT EXISTS (SELECT FROM information_schema.tables \
            WHERE table_name = 'not_exist_table')"
        db.execute(query)
        is_table_exist_before = db.fetch()[0][0]

        db.create_table(
            table_name="not_exist_table", columns=["test_data", "number"],
            types=["text", "int"], temporary=True
        )
        db.commit()

        query = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE \
            table_name = 'not_exist_table')"
        db.execute(query)
        is_table_exist_after = db.fetch()[0][0]

        db.disconnect()

        self.assertFalse(is_table_exist_before)
        self.assertTrue(is_table_exist_after)

    def test_session(self):
        """Test connection-disconnection."""
        db = DBManager(db_name=self.DB_NAME, user=self.USER)

        db.connect()

        self.assertFalse(db._connection.closed)
        self.assertFalse(db._cursor.closed)

        db.disconnect()

        self.assertTrue(db._connection.closed)
        self.assertTrue(db._cursor.closed)

    def test_insert(self):
        """Test data insertion."""
        db = DBManager(db_name=self.DB_NAME, user=self.USER)

        db.connect()

        db.execute("SELECT * FROM {};".format(self.TABLE_NAME))
        before = db.fetch()

        query = "INSERT INTO {} ({}) VALUES ({})".format(
            self.TABLE_NAME, "data", "%s"
        )
        db.execute(query, ["some_text"])

        db.execute("SELECT * FROM {};".format(self.TABLE_NAME))
        after = db.fetch()

        self.assertEqual(len(before), 0)
        self.assertEqual(len(after), 1)


if __name__ == "__main__":
    unittest.main()
