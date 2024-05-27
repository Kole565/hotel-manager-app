"""Provide GUI class for data collecting widget."""
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit


class RoomController(QWidget):
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
        id_label = QLabel("Room id:")
        id_entry = QLineEdit("1")

        self.gui["id_entry"] = id_entry

        self.layout.addWidget(id_label, 0, 0)
        self.layout.addWidget(id_entry, 1, 0)

    def data_check(self):
        """Return True if data is good enough for saving/creating."""
        room_id = self.gui["id_entry"].text()
        if room_id in self._rooms_ids():
            return True
        return False

    def _rooms_ids(self):
        query = "SELECT id FROM {}".format("rooms")

        return [str(i[0]) for i in self.db.execute_and_return(query)]

    def _get_price(self, room_id):
        query = "SELECT price FROM {} WHERE id = %s;".format("rooms")

        return self.db.execute_and_return(query, room_id)[0]

    def _get_capacity(self, room_id):
        query = "SELECT capacity FROM {} WHERE id = %s;".format("rooms")

        return self.db.execute_and_return(query, room_id)[0]

    def get_errors(self):
        """Return formatted errors if any."""
        errors = []

        if not self.gui["id_entry"].text():
            errors.append("Room id is empty")

        return errors
