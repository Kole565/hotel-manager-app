from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout


class PageCounterWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.current = "0"
        self.divider = "/"
        self.max = "0"

        self.current = QLabel("0")
        self.divider = QLabel("/")
        self.max = QLabel("0")
        self.previous_page = QPushButton("❮")
        self.next_page = QPushButton("❯")

        layout = QHBoxLayout()

        layout.addWidget(self.current)
        layout.addWidget(self.divider)
        layout.addWidget(self.max)
        layout.addWidget(self.previous_page)
        layout.addWidget(self.next_page)

        self.setLayout(layout)
