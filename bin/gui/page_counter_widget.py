from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout

from functools import partial


class PageCounterWidget(QWidget):
    """Provide tables listing functionality gui"""

    SEPARATOR = "/"

    def __init__(self, update_func):
        super().__init__()

        self.current_page = 1
        self.total_pages = None

        self.counter = QLabel("0/0")
        self.previous_page_button = QPushButton("❮")
        self.next_page_button = QPushButton("❯")

        self.previous_page_button.clicked.connect(partial(self.increment_page, -1))
        self.next_page_button.clicked.connect(partial(self.increment_page, 1))

        self.update_func = update_func

        layout = QHBoxLayout()

        layout.addWidget(self.counter)
        layout.addWidget(self.previous_page_button)
        layout.addWidget(self.next_page_button)

        self.setLayout(layout)

    def init_pages(self, total_pages):
        """Used for switching between tables"""
        self.current_page = 1
        self.total_pages = total_pages

    def increment_page(self, increment):
        self.current_page += increment

        self.current_page = 1 if self.current_page < 1 else self.current_page
        self.current_page = self.total_pages if self.current_page > self.total_pages else self.current_page

        self.update_func()

    def update(self):
        """Update counter ui"""
        text = "{}{}{}".format(self.current_page, self.SEPARATOR, self.total_pages)

        self.counter.setText(text)
