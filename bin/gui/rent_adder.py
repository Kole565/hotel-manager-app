from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QMainWindow, QWidget, QMessageBox,
    QFormLayout, QTableWidget,
    QTableWidgetItem, QDialog, QDialogButtonBox, QToolBar, QLabel, QLineEdit, QPushButton)

# from PySide6.QtGui import QAction


class RentAdder(QMainWindow):
    """Form where you can insert rent data and create one"""

    def __init__(self):
        super().__init__()

        self.room_id_label = QLabel("Room id:")
        self.room_id_edit = QLineEdit()

        layout = QFormLayout()

        layout.addRow(self.room_id_label, self.room_id_edit)

        self.setLayout(layout)

        self.setWindowTitle("Create Rent")
        self.setFixedSize(QSize(600, 600))


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    window = RentAdder()
    window.show()

    app.exec()
