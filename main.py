from PySide6.QtWidgets import QApplication

from bin.gui.tables_window import TablesWindow


app = QApplication([])

window = TablesWindow()
window.show()

app.exec()
