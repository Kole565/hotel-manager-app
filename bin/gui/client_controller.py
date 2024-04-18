from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit

from bin.gui.controller import Controller
from bin.client_model import ClientModel


class ClientController(Controller):

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {}

        self._init_gui()

        self.setLayout(self.layout)

    def data_check(self):
        # TODO: Implement
        return True

    def _init_gui(self):
        name_label = QLabel("Full name:")
        name_entry = QLineEdit()

        self.gui["name_entry"] = name_entry

        self.layout.addWidget(name_label, 0, 0)
        self.layout.addWidget(name_entry, 1, 0)
