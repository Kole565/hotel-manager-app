from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit

from bin.gui.controller import Controller
from bin.transaction_model import TransactionModel


class TransactionController(Controller):
    """Used with Rent Adder. Provide form and get input for transaction part of rent model init."""

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {}

        self._init_gui()

        self.setLayout(self.layout)

    def _init_gui(self):
        credentials_label = QLabel("Credentials:")
        credentials_entry = QLineEdit("123456789101")

        self.gui["credentials_entry"] = credentials_entry

        self.layout.addWidget(credentials_label, 0, 0)
        self.layout.addWidget(credentials_entry, 1, 0)

    def data_check(self):
        credentials = self.gui["credentials_entry"].text()
        if self._exist_client_with(credentials):
            return True
        return False

    def _exist_client_with(self, credentials):
        query = "SELECT EXISTS (SELECT 1 FROM {} WHERE credentials = %s);".format("clients")

        return self.db.execute_and_return(query, (credentials,))[0][0]

    def get_errors(self):
        errors = []

        if not self.gui["credentials_entry"].text():
            errors.append("Credentials is empty")
        if not self._exist_client_with(self.gui["credentials_entry"].text()):
            errors.append("Credentials is invalid (no user with such credentials exist)")

        return errors
