"""Provide GUI class for data collecting widget."""
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit


class TransactionController(QWidget):
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
        credentials_label = QLabel("Credentials:")
        credentials_entry = QLineEdit("123456789101")

        self.gui["credentials_entry"] = credentials_entry

        self.layout.addWidget(credentials_label, 0, 0)
        self.layout.addWidget(credentials_entry, 1, 0)

    def data_check(self):
        """Return True if data is good enough for saving/creating."""
        credentials = self.gui["credentials_entry"].text()
        if self._exist_client_with(credentials):
            return True
        return False

    def _exist_client_with(self, credentials):
        query = "SELECT EXISTS (SELECT 1 FROM {} WHERE credentials = %s);"
        query = query.format("clients")

        return self.db.execute_and_return(query, (credentials,))[0][0]

    def get_errors(self):
        """Return formatted errors if any."""
        errors = []

        if not self.gui["credentials_entry"].text():
            errors.append("Credentials is empty")
        if not self._exist_client_with(self.gui["credentials_entry"].text()):
            errors.append(
                "Credentials is invalid (no user with such credentials exist)"
            )

        return errors
