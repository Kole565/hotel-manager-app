from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QDialogButtonBox

from bin.gui.controller import Controller
from bin.rent_model import RentModel

from datetime import datetime


class RentController(Controller):

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
        since_entry = QLineEdit()
        due_entry = QLineEdit()

        self.gui["since_entry"] = since_entry
        self.gui["due_entry"] = due_entry

        self.layout.addWidget(since_label, 0, 0)
        self.layout.addWidget(due_label, 1, 0)
        self.layout.addWidget(since_entry, 0, 1)
        self.layout.addWidget(due_entry, 1, 1)

    def data_check(self):
        try:
            since = datetime.strptime(self.gui["since_entry"].text(), "%Y-%m-%d")
            due = datetime.strptime(self.gui["since_entry"].text(), "%Y-%m-%d")

            difference = due - since
        except Exception as e:
            raise e

        print(difference.date)

    def _create(self):
        rooms_ids = self._fetch_rooms_ids()
        clients_ids = self.clients_ids
        since = self.gui["rent"]["since_entry"].text()
        due = self.gui["rent"]["due_entry"].text()

        model = RentModel(rooms_ids, clients_ids, since, due)

        model.save(self.db)
