from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit

from bin.gui.controller import Controller
from bin.room_model import RoomModel


class RoomController(Controller):

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {}

        self._init_gui()

        self.setLayout(self.layout)

    def data_check(self):
        room_id = self.gui["id_entry"].text()
        if room_id in self._rooms_ids():
            return True
        return False

    def _rooms_ids(self):
        query = "SELECT id FROM {}".format("rooms")

        return [str(i[0]) for i in self.db.execute_full(query)]

    def create(self):
        pass

    def _init_gui(self):
        id_label = QLabel("Room id:")
        id_entry = QLineEdit()

        self.gui["id_entry"] = id_entry

        self.layout.addWidget(id_label, 0, 0)
        self.layout.addWidget(id_entry, 1, 0)
