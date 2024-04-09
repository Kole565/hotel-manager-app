import unittest
import datetime

from rent import Rent


class TestRent(unittest.TestCase):

    def test_init(self):
        rent = Rent(
            duration=datetime.timedelta(days=10),
            since=datetime.datetime(2020, 5, 10),
            index=1
        )

        self.assertEqual(rent._duration, datetime.timedelta(days=10))
        self.assertEqual(rent._since, datetime.datetime(2020, 5, 10))
        self.assertEqual(rent._due, datetime.datetime(2020, 5, 20))
        self.assertEqual(rent._index, 1)

    def test_append_room(self):
        rent = Rent(
            duration=datetime.timedelta(days=10),
            since=datetime.datetime(2020, 5, 10),
            index=1
        )
        room = object()

        rent.add_room(room)

        self.assertEqual(rent._rooms, [room])

    def test_append_client(self):
        rent = Rent(
            duration=datetime.timedelta(days=10),
            since=datetime.datetime(2020, 5, 10),
            index=1
        )
        client_index = 42

        rent.add_client(client_index)

        self.assertEqual(rent._clients, [client_index])

    def test_save(self):
        rent = Rent(
            duration=datetime.timedelta(days=10),
            since=datetime.datetime(2020, 5, 10),
            index=1
        )
        rent.save()


if __name__ == "__main__":
    unittest.main()
