"""Tests for model."""
import unittest

from bin.room_model import RoomModel
from bin.db import DBManager


class TestRoomModel(unittest.TestCase):
    """Test rent model class."""

    def _get_test_object(self):
        return RoomModel(
            price=100,
            capacity=2,
        )

    def test_init(self):
        """Test initial data saving."""
        test_object = self._get_test_object()

        self.assertEqual(test_object._price, 100)
        self.assertEqual(test_object._capacity, 2)

    def test_set_get_attributes(self):
        """Test data saving-retrieving via model."""
        test_object = self._get_test_object()

        test_object.price = 120
        test_object.capacity = 3

        self.assertEqual(test_object.price, 120)
        self.assertEqual(test_object.capacity, 3)

    def test_save_load(self):
        """Test in runtime data saving-retrieving."""
        db = DBManager("test_db", "test")

        test_object = self._get_test_object()

        test_object.save(db)

        loaded_test_object = RoomModel.from_table(*self._objects_list(db)[-1])

        self.assertEqual(test_object.price, loaded_test_object.price)
        self.assertEqual(test_object.capacity, loaded_test_object.capacity)

    def _objects_list(self, db):
        query = "SELECT * from rooms"

        db.connect()

        db.execute(query)
        result = db.fetch()

        db.disconnect()

        return result


if __name__ == "__main__":
    unittest.main()
