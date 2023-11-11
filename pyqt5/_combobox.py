import typing
from PyQt5 import QtCore, QtWidgets
import sys

from PyQt5.QtWidgets import QWidget

from _comboboxform import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.city_comboBox
        combo.addItem("Ankara")
        combo.addItem("İstanbul")
        
        self.ui.load_Button.clicked.connect(self.LoadItems)
        self.ui.getItem_Button.clicked.connect(self.GetItem)
        self.ui.city_comboBox.addItem("Rize")

        self.ui.city_comboBox.currentIndexChanged.connect(self.SelectedChanged)
        self.ui.city_comboBox.currentIndexChanged[str].connect(self.SelectedChangedText)

    def LoadItems(self):
        citys = ["Adana","İzmir","Sivas","Kocaeli"]
        self.ui.city_comboBox.addItems(citys)


    def GetItem(self):
        print(self.ui.city_comboBox.currentText())
        print(self.ui.city_comboBox.currentIndex())

        count = self.ui.city_comboBox.count()
        for index in range(count):
            print(self.ui.city_comboBox.itemText(index))


    def SelectedChanged(self,index):
        print(index)
        

    def SelectedChangedText(self,text):
        print(text)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()