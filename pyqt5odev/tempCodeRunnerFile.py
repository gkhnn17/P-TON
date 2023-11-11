from PyQt5.QtWidgets import QApplication, QMainWindow
from ekran1ui import Ui_ekran1 
from ekran1code import Interface


app = QApplication([])
window = Interface()
window.show()
app.exec_()