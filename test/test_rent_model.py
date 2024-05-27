"""Tests for model."""
import unittest
import datetime

from bin.rent_model import RentModel
from bin.db import DBManager


class TestRentModel(unittest.TestCase):
    """Test rent model class."""

    def _get_test_object(self):
        return RentModel(
            room_id=None,
            transaction_id=None,
            since=datetime.date(2020, 5, 10),
            due=datetime.date(2020, 5, 20),
        )

    def test_init(self):
        """Test initial data saving."""
        rent = self._get_test_object()

        self.assertEqual(rent._room_id, None)
        self.assertEqual(rent._transaction_id, None)
        self.assertEqual(rent._since, datetime.date(2020, 5, 10))
        self.assertEqual(rent._due, datetime.date(2020, 5, 20))

        self.assertEqual(rent._duration, datetime.timedelta(days=10))

    def test_set_attributes(self):
        """Test data saving-retrieving via model."""
        rent = self._get_test_object()

        rent.room_id = [0]
        rent.transaction_id = 0
        rent.since = datetime.date(2020, 3, 10)
        rent.due = datetime.date(2020, 3, 20)

        self.assertEqual(rent.room_id, [0])
        self.assertEqual(rent.transaction_id, 0)
        self.assertEqual(rent.since, datetime.date(2020, 3, 10))
        self.assertEqual(rent.due, datetime.date(2020, 3, 20))

    def test_save_load(self):
        """Test in runtime data saving-retrieving."""
        db = DBManager("test_db", "test")

        rent = self._get_test_object()

        rent.save(db)

        loaded_rent = RentModel.from_table(*self._rents_list(db)[-1])

        self.assertEqual(rent.room_id, loaded_rent.room_id)
        self.assertEqual(rent.transaction_id, loaded_rent.transaction_id)
        self.assertEqual(rent.since, loaded_rent.since)
        self.assertEqual(rent.due, loaded_rent.due)

    def _rents_list(self, db):
        query = "SELECT * from rents"

        db.connect()

        db.execute(query)
        result = db.fetch()

        db.disconnect()

        return result


if __name__ == "__main__":
    unittest.main()
