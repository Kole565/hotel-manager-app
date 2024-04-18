from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit

from bin.gui.controller import Controller
from bin.transaction_model import TransactionModel


class TransactionController(Controller):

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {}

        self._init_gui()

        self.setLayout(self.layout)

    def _init_gui(self):
        credentials_label = QLabel("Credentials:")
        credentials_entry = QLineEdit()

        self.gui["credentials_entry"] = credentials_entry

        self.layout.addWidget(credentials_label, 0, 0)
        self.layout.addWidget(credentials_entry, 1, 0)
