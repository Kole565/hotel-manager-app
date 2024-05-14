from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class EntryEditWidget(QWidget):
    """Provide table item manipulation gui like add, del, edit"""

    def __init__(self, add_func, remove_func=None, edit_func=None, save_func=None):
        super().__init__()

        layout = QVBoxLayout()

        self.add = QPushButton("Add")
        self.remove = QPushButton("Del")
        self.edit = QPushButton("Edit")
        self.save = QPushButton("Save")

        self.add.clicked.connect(add_func)
        self.remove.clicked.connect(remove_func)
        self.edit.clicked.connect(edit_func)
        self.save.clicked.connect(save_func)

        layout.addWidget(self.add)
        layout.addWidget(self.remove)
        layout.addWidget(self.edit)
        layout.addWidget(self.save)

        self.setLayout(layout)
