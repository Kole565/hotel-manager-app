from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit

from bin.rent_model import RentModel

from datetime import datetime


class RentController(QWidget):
    """Used with tables viewer. Provide form and get input for rent part of rent model init."""

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {}

        self._init_gui()

        self.setLayout(self.layout)

    def _init_gui(self):
        since_label = QLabel("Since:")
        due_label = QLabel("Due:")
        since_entry = QLineEdit("2000-01-01")
        due_entry = QLineEdit("2000-01-02")

        self.gui["since_entry"] = since_entry
        self.gui["due_entry"] = due_entry

        self.layout.addWidget(since_label, 0, 0)
        self.layout.addWidget(due_label, 1, 0)
        self.layout.addWidget(since_entry, 0, 1)
        self.layout.addWidget(due_entry, 1, 1)

    def data_check(self):
        try:
            since = datetime.strptime(self.gui["since_entry"].text(), "%Y-%m-%d")
            due = datetime.strptime(self.gui["due_entry"].text(), "%Y-%m-%d")

            difference = due - since
        except Exception:
            return False
        else:
            return True

    def create(self, *args, **kwargs):
        room_id = int(kwargs["room_id"])
        client_id = kwargs["client_id"]
        since = datetime.strptime(self.gui["since_entry"].text(), "%Y-%m-%d")
        due = datetime.strptime(self.gui["due_entry"].text(), "%Y-%m-%d")

        model = RentModel(room_id, 0, since, due)

        model.save(self.db)

    def get_errors(self):
        errors = []

        if not self.gui["since_entry"].text():
            errors.append("Rent since is empty")
        if not self.gui["due_entry"].text():
            errors.append("Rent due is empty")
        if not self.data_check():
            errors.append("Rent dates is wrong format (should be 2000-01-01)")

        return errors
