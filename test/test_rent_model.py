import unittest
import datetime

from bin.rent_model import RentModel
from bin.db import DB


class TestRentModel(unittest.TestCase):

    def get_test_object(self):
        return RentModel(
            rooms_ids=None,
            clients_ids=None,
            transaction_id=None,
            since=datetime.date(2020, 5, 10),
            due=datetime.date(2020, 5, 20),
        )

    def test_init(self):
        rent = self.get_test_object()

        self.assertEqual(rent._rooms_ids, None)
        self.assertEqual(rent._clients_ids, None)
        self.assertEqual(rent._transaction_id, None)
        self.assertEqual(rent._since, datetime.date(2020, 5, 10))
        self.assertEqual(rent._due, datetime.date(2020, 5, 20))

        self.assertEqual(rent._duration, datetime.timedelta(days=10))

    def test_set_attributes(self):
        rent = self.get_test_object()

        rent.rooms_ids = [0]
        rent.clients_ids = [0]
        rent.transaction_id = 0
        rent.since = datetime.date(2020, 3, 10)
        rent.due = datetime.date(2020, 3, 20)

        self.assertEqual(rent.rooms_ids, [0])
        self.assertEqual(rent.clients_ids, [0])
        self.assertEqual(rent.transaction_id, 0)
        self.assertEqual(rent.since, datetime.date(2020, 3, 10))
        self.assertEqual(rent.due, datetime.date(2020, 3, 20))

    def test_save_load(self):
        db = DB("test_db", "test")

        rent = self.get_test_object()

        rent.save(db)

        loaded_rent = RentModel.from_table(*self.rents_list(db)[-1], transaction_id=None)

        self.assertEqual(rent.rooms_ids, loaded_rent.rooms_ids)
        self.assertEqual(rent.clients_ids, loaded_rent.clients_ids)
        self.assertEqual(rent.transaction_id, loaded_rent.transaction_id)
        self.assertEqual(rent.since, loaded_rent.since)
        self.assertEqual(rent.due, loaded_rent.due)

    def rents_list(self, db):
        query = "SELECT * from rents"

        db.connect()

        db.execute(query)
        result = db.fetch()

        db.disconnect()

        return result


if __name__ == "__main__":
    unittest.main()
