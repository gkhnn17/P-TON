import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget
import sys



class MYWindow(QMainWindow):#i will use them in mywindow
    def __init__(self,):
        super(MYWindow,self).__init__()
        self.setGeometry(100,100,500,500)#xpos,ypos,witdh,height
        self.setWindowTitle("Tech with me")   
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)#LABEL
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)#BUTTON
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clickedme)


    def clickedme(self):
        self.label.setText("you pressed this button ")
        self.uptade()

    def uptade(self):#uptading size when you press button
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MYWindow()
    win.show()
    sys.exit(app.exec_())#exit for x button

window()