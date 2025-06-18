import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from frontend.views.table_viewer import Ui_TableViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self._ui = Ui_TableViewer()
        self._ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
