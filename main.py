from PySide6.QtWidgets import QApplication

from bin.gui.main_menu import MainMenu


app = QApplication([])

window = MainMenu()
window.show()

app.exec()
