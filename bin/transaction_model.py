"""Provide model class for item serialization."""


class TransactionModel:
    """Data class for item serialization."""

    TABLE_NAME = "transactions"

    def __init__(self, details, total, completed):
        """Store init data in class."""
        self._details = details
        self._total = total
        self._completed = completed

    @staticmethod
    def from_table(id, details, total, completed):
        """Create model from data acquired from respective table in db."""
        return TransactionModel(
            details=details, total=total, completed=completed
        )

    def save(self, db):
        """From query and put model data in db."""
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (details, sum, completed) \
        VALUES (%s, %s, %s)".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return self._details, self._total, self._completed

    @property
    def details(self):
        """Getter for description property."""
        return self._details

    @details.setter
    def details(self, value):
        """Setter for description property."""
        self._details = value

    @property
    def total(self):
        """Getter for total property."""
        return self._total

    @total.setter
    def total(self, value):
        """Setter for total property."""
        self._total = value

    @property
    def completed(self):
        """Getter for completed state property."""
        return self._completed

    @completed.setter
    def completed(self, value):
        """Setter for completed state property."""
        self._completed = value
