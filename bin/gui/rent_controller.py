from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QDialogButtonBox
from bin.rent_model import RentModel


class RentController(QDialog):

    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QGridLayout()

        self.gui = {"room": {}, "client": {}, "rent": {}, "transaction": {}}

        self._init_room_gui()
        self._init_client_gui()
        self._init_rent_gui()
        self._init_transaction_gui()

        self._init_control_buttons()

        self.setLayout(self.layout)

    def _init_room_gui(self):
        id_label = QLabel("Room id:")
        id_entry = QLineEdit()

        self.gui["room"]["id_entry"] = id_entry

        self.layout.addWidget(id_label, 0, 0)
        self.layout.addWidget(id_entry, 1, 0)

    def _init_client_gui(self):
        name_label = QLabel("Full name:")
        name_entry = QLineEdit()

        self.gui["client"]["name_entry"] = name_entry

        self.layout.addWidget(name_label, 0, 1)
        self.layout.addWidget(name_entry, 1, 1)

    def _init_rent_gui(self):
        since_label = QLabel("Since:")
        due_label = QLabel("Due:")
        since_entry = QLineEdit()
        due_entry = QLineEdit()

        self.gui["rent"]["since_entry"] = since_entry
        self.gui["rent"]["due_entry"] = due_entry

        self.layout.addWidget(since_label, 0, 2)
        self.layout.addWidget(due_label, 1, 2)
        self.layout.addWidget(since_entry, 0, 3)
        self.layout.addWidget(due_entry, 1, 3)

    def _init_transaction_gui(self):
        credentials_label = QLabel("Credentials:")
        credentials_entry = QLineEdit()

        self.gui["transaction"]["credentials_entry"] = credentials_entry

        self.layout.addWidget(credentials_label, 0, 4)
        self.layout.addWidget(credentials_entry, 1, 4)

    def _init_control_buttons(self):
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(QBtn)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.layout.addWidget(button_box, 2, 4)

    def accept(self):
        if not self._is_all_data_inserted():
            # TODO: Add warning
            return

        self._create_clients_if_need_to()
        self._create_transaction()
        self._create_rent()

        self._create_client_rent_binding()

        super().accept()

    def _is_all_data_inserted(self):
        return all((
            self.gui["room"]["id_entry"].text().strip() != "",
            self.gui["client"]["name_entry"].text().strip() != "",
            self.gui["rent"]["since_entry"].text().strip() != "",
            self.gui["rent"]["due_entry"].text().strip() != "",
            self.gui["transaction"]["credentials_entry"].text().strip() != "",
        ))

    def _create_clients_if_need_to(self):
        names = self.gui["client"]["name_entry"].text().split(";")

        registered_names = self._get_clients_names()

        if all([name in registered_names for name in names]):
            return

        self._register_clients([name for name in names if name not in registered_names])

    def _get_clients_names(self):
        self.db.connect()

        query = "SELECT fio FROM clients"

        self.db.execute(query)
        result = self.db.fetch()

        self.db.disconnect()

        names = [el[0] for el in result]

        return names

    def _register_clients(self, names):
        # TODO: This func should register clients, but need ClientModel and ClientController to work
        pass

    def _create_rent(self):
        rooms_ids = self._fetch_rooms_ids()
        clients_ids = self.clients_ids
        since = self.gui["rent"]["since_entry"].text()
        due = self.gui["rent"]["due_entry"].text()

        model = RentModel(rooms_ids, clients_ids, since, due)

        model.save(self.db)
