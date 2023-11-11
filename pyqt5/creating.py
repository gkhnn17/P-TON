from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
def window():
    app = QApplication(sys.argv)
    win= QMainWindow()

    win.setWindowTitle("First app")
    win.setGeometry(200,200,500,500)#1,2 ->location,3,4 ->size
    win.setToolTip("My tool tip")
    
    win.show()
    sys.exit(app.exec_())

window()