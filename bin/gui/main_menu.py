from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton
from PySide6.QtCore import QSize

from bin.gui.tables_viewer import TablesViewer
from bin.gui.rent_adder import RentAdder


class MainMenu(QMainWindow):
    """GUI that contain references to other programs"""

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(150, 200))
        self.setWindowTitle("Main Menu")

        layout = QGridLayout()

        self.tables_viewer_button = QPushButton("Tables Viewer")
        self.rent_adder_button = QPushButton("Rent Adder")

        self.tables_viewer_button.clicked.connect(lambda: self.show_item(TablesViewer))
        self.rent_adder_button.clicked.connect(lambda: self.show_item(RentAdder))

        layout.addWidget(self.tables_viewer_button)
        layout.addWidget(self.rent_adder_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def show_item(self, window_class):
        window = window_class()
        window.show()


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    window = MainMenu()
    window.show()

    app.exec()
