"""Tests for model."""
import unittest

from bin.client_model import ClientModel
from bin.db import DBManager


class TestClientModel(unittest.TestCase):
    """Test client model class."""

    def _get_test_object(self):
        return ClientModel(
            password_hash="jI938S)FPOJWEPOF",
            username="PrettyJoe",
            name="Joe Gale",
            credentials="123456789101"
        )

    def test_init(self):
        """Test initial data saving."""
        test_object = self._get_test_object()

        self.assertEqual(test_object._password_hash, "jI938S)FPOJWEPOF")
        self.assertEqual(test_object._username, "PrettyJoe")
        self.assertEqual(test_object._name, "Joe Gale")
        self.assertEqual(test_object._credentials, "123456789101")

    def test_set_get_attributes(self):
        """Test data saving-retrieving via model."""
        test_object = self._get_test_object()

        test_object.password_hash = "jI938OJWEPOF"
        test_object.username = "PJoe"
        test_object.name = "Joe Gale"
        test_object.credentials = "123456789101"

        self.assertEqual(test_object.password_hash, "jI938OJWEPOF")
        self.assertEqual(test_object.username, "PJoe")
        self.assertEqual(test_object.name, "Joe Gale")
        self.assertEqual(test_object.credentials, "123456789101")

    def test_save_load(self):
        """Test in runtime data saving-retrieving."""
        db = DBManager("test_db", "test")

        test_object = self._get_test_object()

        test_object.save(db)

        loaded_test_object = ClientModel.from_table(
            *self._objects_list(db)[-1]
        )

        self.assertEqual(
            test_object.password_hash, loaded_test_object.password_hash
        )
        self.assertEqual(
            test_object.username, loaded_test_object.username
        )
        self.assertEqual(
            test_object.name, loaded_test_object.name
        )
        self.assertEqual(
            test_object.credentials, loaded_test_object.credentials
        )

    def _objects_list(self, db):
        query = "SELECT * from clients"

        db.connect()

        db.execute(query)
        result = db.fetch()

        db.disconnect()

        return result


if __name__ == "__main__":
    unittest.main()
