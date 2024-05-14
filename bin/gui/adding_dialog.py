from PySide6.QtWidgets import QDialog, QGridLayout, QLabel, QLineEdit, QDialogButtonBox


class AddingDialog(QDialog):
    """Dialog that collect new table item data from user"""

    def __init__(self, size, headers, collected_data):
        super().__init__()

        self.size = size
        self.headers = headers
        self.collected_data = collected_data

        print(self.size, self.headers, self.collected_data)

        self.layout = QGridLayout()

        self._init_entries()

        self.setLayout(self.layout)

    def _init_entries(self):
        self.entries = []

        for ind, header in enumerate(self.headers):
            self.layout.addWidget(QLabel(header[0]), ind, 0)

        for ind in range(self.size[0]):
            widget = QLineEdit()
            self.entries.append(widget)
            self.layout.addWidget(widget, ind, 1)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(QBtn)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout.addWidget(self.button_box, self.size[0], self.size[1])

    def accept(self):
        for widget in self.entries:
            self.collected_data.append(widget.text())

        super().accept()
