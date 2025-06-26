class TransactionModel:

    TABLE_NAME = "transactions"

    def __init__(self, details, total, completed):
        self._details = details
        self._total = total
        self._completed = completed

    @staticmethod
    def from_table(id, details, total, completed):
        return TransactionModel(details=details, total=total, completed=completed)

    def save(self, db):
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (details, sum, completed) VALUES (%s, %s, %s)".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return self._details, self._total, self._completed

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value
