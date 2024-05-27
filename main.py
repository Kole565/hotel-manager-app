"""Hotel app launching script."""
from PySide6.QtWidgets import QApplication

from bin.gui.tables_viewer import TablesViewer


app = QApplication([])

window = TablesViewer()
window.show()

app.exec()
