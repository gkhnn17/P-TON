import sys
import typing
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate,QTime,QDateTime
from _datetimeform import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.totalCalculate)

    def totalCalculate(self):
        start = self.ui.dateEdit.date()
        end = self.ui.dateEdit_2.date()

        print(start,end)

        print("Days in month:{0}".format(start.daysInMonth()))
        now = QDate.currentDate()

        

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()