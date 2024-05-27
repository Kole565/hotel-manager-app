"""Provide GUI class for collecting rent data and creating rent object."""
from PySide6.QtWidgets import (
    QDialog, QGridLayout, QDialogButtonBox, QMessageBox
)

from bin.gui.room_controller import RoomController
from bin.gui.client_controller import ClientController
from bin.gui.rent_controller import RentController
from bin.gui.transaction_controller import TransactionController


class RentAdding(QDialog):
    """Custom adding dialog for rent model."""

    def __init__(self, db):
        """Initialize db and controllers."""
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.controllers = []

        self._init_widgets()

        self._init_control_buttons()

        self.setLayout(self.layout)

    def _init_widgets(self):
        controllers_classes = [
            RoomController, ClientController, RentController,
            TransactionController
        ]
        for i, Controller in enumerate(controllers_classes):
            widget = Controller(self.db)

            self.controllers.append(widget)

            self.layout.addWidget(widget, 0, i)

    def _init_control_buttons(self):
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(QBtn)

        button_box.accepted.connect(self._accept)
        button_box.rejected.connect(self.reject)

        self.layout.addWidget(button_box, 2, 3)

    def _accept(self):
        if not self.data_check():
            return

        self.create()

        super().accept()

    def data_check(self):
        """Return True if data is good enough for saving/creating."""
        ret = True

        errors_lists = []
        for controller in self.controllers:
            if not controller.data_check():
                errors = "; ".join(controller.get_errors())
                errors_lists.append(errors)

                ret = False

        message = "You have encounter errors: {}".format(
            "; ".join(errors_lists)
        )
        if errors_lists:
            QMessageBox.information(
                self,
                "Errors",
                message,
                buttons=QMessageBox.Ok
            )

        return ret

    def create(self):
        """Collect data and create rent object."""
        # Room controller
        room_id = self.controllers[0].gui["id_entry"].text()

        # Client controller
        client_name = self.controllers[1].gui["name_entry"].text()

        client_id = self._get_clients_ids(client_name.split())

        # Rent controller
        self.controllers[2].create(room_id=room_id, client_id=client_id)

    def _get_clients_ids(self, clients_names):
        result = []

        query = "SELECT id FROM {} WHERE fio = %s;".format("clients")
        for name in clients_names:
            result.append(self.db.execute_and_return(query, (name,)))

        return result
