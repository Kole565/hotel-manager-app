"""Provide model class for item serialization."""


class RoomModel:
    """Data class for item serialization."""

    TABLE_NAME = "rooms"

    def __init__(self, price, capacity):
        """Store init data in class."""
        self._price = price
        self._capacity = capacity

    @staticmethod
    def from_table(id, price, capacity):
        """Create model from data acquired from respective table in db."""
        return RoomModel(price=price, capacity=capacity)

    def save(self, db):
        """From query and put model data in db."""
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (price, capacity) \
        VALUES (%s, %s);".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return [self._price, self._capacity]

    @property
    def price(self):
        """Getter for price property."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price property."""
        self._price = value

    @property
    def capacity(self):
        """Getter for capacity property."""
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """Setter for capacity property."""
        self._capacity = value
