class RoomModel:

    TABLE_NAME = "rooms"

    def __init__(self, price, capacity):
        self._price = price
        self._capacity = capacity

    @staticmethod
    def from_table(id, price, capacity):
        return RoomModel(price=price, capacity=capacity)

    def save(self, db):
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (price, capacity) VALUES (%s, %s)".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return self._price, self._capacity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
