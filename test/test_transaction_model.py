import unittest

from bin.transaction_model import TransactionModel
from bin.db import DBManager


class TestTransactionModel(unittest.TestCase):

    def get_test_object(self):
        return TransactionModel(
            details="",
            total=200,
            completed=True,
        )

    def test_init(self):
        test_object = self.get_test_object()

        self.assertEqual(test_object._details, "")
        self.assertEqual(test_object._total, 200)
        self.assertEqual(test_object._completed, True)

    def test_set_get_attributes(self):
        test_object = self.get_test_object()

        test_object.details = "ID: 900"
        test_object.total = 300
        test_object.completed = False

        self.assertEqual(test_object.details, "ID: 900")
        self.assertEqual(test_object.total, 300)
        self.assertEqual(test_object.completed, False)

    def test_save_load(self):
        db = DBManager("test_db", "test")

        test_object = self.get_test_object()

        test_object.save(db)

        loaded_test_object = TransactionModel.from_table(*self.objects_list(db)[-1])

        self.assertEqual(test_object.details, loaded_test_object.details)
        self.assertEqual(test_object.total, loaded_test_object.total)
        self.assertEqual(test_object.completed, loaded_test_object.completed)

    def objects_list(self, db):
        query = "SELECT * from transactions"

        db.connect()

        db.execute(query)
        result = db.fetch()

        db.disconnect()

        return result


if __name__ == "__main__":
    unittest.main()
