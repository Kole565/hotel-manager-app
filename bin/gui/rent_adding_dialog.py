from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QDialogButtonBox

from bin.gui.room_controller import RoomController
from bin.gui.client_controller import ClientController
from bin.gui.rent_controller import RentController
from bin.gui.transaction_controller import TransactionController


class RentAdding(QDialog):

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.controllers = []

        self._init_widgets()

        self._init_control_buttons()

        self.setLayout(self.layout)

    def _init_widgets(self):
        for i, Controller in enumerate((RoomController, ClientController, RentController, TransactionController)):
            widget = Controller(self.db)

            self.controllers.append(widget)

            self.layout.addWidget(widget, 0, i)

    def _init_control_buttons(self):
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(QBtn)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.layout.addWidget(button_box, 2, 4)

    def accept(self):
        if not self.data_check():
            return

        self.create()

        super().accept()

    def data_check(self):
        for controller in self.controllers:
            if not controller.data_check():
                return False

        return True

    def create(self):
        for controller in self.controllers:
            controller.create()
