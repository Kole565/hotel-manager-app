from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class SearchWidget(QWidget):

    def __init__(self, fetch_func):
        super().__init__()

        layout = QHBoxLayout()

        self.entry = QLineEdit()
        self.button = QPushButton("Fetch")
        self.button.clicked.connect(lambda: fetch_func(self._get_table_name()))

        layout.addWidget(self.entry)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def _get_table_name(self):
        return self.entry.text()
