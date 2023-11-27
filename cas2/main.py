from PyQt5.QtWidgets import QApplication
from functions import Interface

app = QApplication([])
window = Interface()
window.show()
app.exec_()    