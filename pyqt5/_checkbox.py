import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from _checkboxform import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self) :
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cinema_cb.stateChanged.connect(self.show_state)
        self.ui.book_cb.stateChanged.connect(self.show_state)
        self.ui.spor_cb.stateChanged.connect(self.show_state)

        self.ui.button.clicked.connect(self.getAllChecked)


    def show_state(self,value):
        cb = self.sender()#it goes to selected item
        print(cb.text())
        print(cb.isChecked())
        #print(value)#2
        #print(self.ui.cinema_cb.isChecked())
        #print(self.ui.cinema_cb.text())
    
    def getAllChecked(self):
        result = ""
        items = self.ui.groupBox.findChildren(QtWidgets.QCheckBox)
        for item in items:
            if item.isChecked():
                result += item.text() + "\n"
        self.ui.label.setText(result)
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()


