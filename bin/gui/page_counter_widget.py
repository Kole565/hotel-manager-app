from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout


class PageCounterWidget(QWidget):
    """Provide tables listing functionality gui"""

    def __init__(self, increment_page_func):
        super().__init__()

        self.current = "0"
        self.divider = "/"
        self.max = "0"

        self.current = QLabel("0")
        self.divider = QLabel("/")
        self.max = QLabel("0")
        self.previous_page_button = QPushButton("❮")
        self.next_page_button = QPushButton("❯")

        self.increment_page_func = increment_page_func

        self.previous_page_button.clicked.connect(self.previous_page)
        self.next_page_button.clicked.connect(self.next_page)

        layout = QHBoxLayout()

        layout.addWidget(self.current)
        layout.addWidget(self.divider)
        layout.addWidget(self.max)
        layout.addWidget(self.previous_page_button)
        layout.addWidget(self.next_page_button)

        self.setLayout(layout)

    def next_page(self):
        self.increment_page_func(1)

    def previous_page(self):
        self.increment_page_func(-1)
