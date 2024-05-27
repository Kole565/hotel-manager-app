"""Provide GUI class for data collecting widget."""
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit


class ClientController(QWidget):
    """Provide form and get input for model init."""

    def __init__(self, db):
        """Initialize elements for data collecting."""
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {}

        self._init_gui()

        self.setLayout(self.layout)

    def _init_gui(self):
        name_label = QLabel("Full name:")
        name_entry = QLineEdit("Joe Gale")

        self.gui["name_entry"] = name_entry

        self.layout.addWidget(name_label, 0, 0)
        self.layout.addWidget(name_entry, 1, 0)

    def data_check(self):
        """Return True if data is good enough for saving/creating."""
        name = self.gui["name_entry"].text()

        if self._exist_client_with(name):
            return True
        return False

    def _exist_client_with(self, name):
        query = "SELECT EXISTS (SELECT 1 FROM {} WHERE fio = %s);".format(
            "clients")

        return self.db.execute_and_return(query, (name,))[0][0]

    def get_errors(self):
        """Return formatted errors if any."""
        errors = []

        if not self.gui["name_entry"].text():
            errors.append("Client fio is empty")
        if not self._exist_client_with(self.gui["name_entry"].text()):
            errors.append("Client fio is not in db")

        return errors
