import unittest

from room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.test_object = Room(price=100, capacity=2, location="1F 20", index=1)

    def test_init(self):
        self.assertEqual(self.test_object._index, 1)
        self.assertEqual(self.test_object._price, 100)
        self.assertEqual(self.test_object._capacity, 2)
        self.assertEqual(self.test_object._location, "1F 20")

    def test_get_index(self):
        self.assertEqual(self.test_object.index, 1)


if __name__ == "__main__":
    unittest.main()
