"""Provide model class for item serialization."""


class RentModel:
    """Data class for item serialization."""

    TABLE_NAME = "rents"

    def __init__(self, room_id, transaction_id, since, due):
        """Store init data in class."""
        self._room_id = room_id
        self._transaction_id = transaction_id

        self._since = since
        self._due = due
        self._duration = self._due - self._since

    @staticmethod
    def from_table(id, room_id, transaction_id, since, due):
        """Create model from data acquired from respective table in db."""
        return RentModel(
            room_id=room_id, transaction_id=transaction_id, since=since,
            due=due
        )

    def save(self, db):
        """From query and put model data in db."""
        db.connect()

        db.execute(self._get_save_query(), args=self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (room_id, transaction_id, since, due) \
        VALUES (%s, %s, %s, %s);".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return [self._room_id, self._transaction_id, self._since, self._due]

    @property
    def room_id(self):
        """Getter for room id property."""
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        """Setter for room id property."""
        self._room_id = value

    @property
    def transaction_id(self):
        """Getter for transaction id property."""
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        """Setter for transaction id property."""
        self._transaction_id = value

    @property
    def since(self):
        """Getter for since date property."""
        return self._since

    @since.setter
    def since(self, value):
        """Setter for since date property."""
        self._since = value

    @property
    def due(self):
        """Getter for due date property."""
        return self._due

    @due.setter
    def due(self, value):
        """Setter for due date property."""
        self._due = value

    @property
    def duration(self):
        """Get duration of rent."""
        return self._duration
