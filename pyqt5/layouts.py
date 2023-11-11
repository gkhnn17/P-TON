import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

from PyQt5.QtGui import QPalette,QColor


class Color (QWidget):
    def __init__(self,colour) :
        super(Color,self).__init__()
        self.setAutoFillBackground(True)
        

        palette =self.palette()
        palette.setColor(QPalette.Window,QColor(colour))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(300,300,500,500)
        #widget =Color('blue')#only blue

        #layout =QtWidgets.QVBoxLayout()#vertical 
        hlayout1 =QtWidgets.QHBoxLayout()#horizontal
        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("green"))
        hlayout1.addWidget(Color("yellow"))
        hlayout1.setContentsMargins(10,20,10,0)#kenarladan boşluk
        hlayout1.setSpacing(50) #elemanlar arası boşluk

        hlayout2 =QtWidgets.QHBoxLayout()#horizontal
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("yellow"))

        vlayout =QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        
        """
        layout = QtWidgets.QGridLayout()

        layout.addWidget(Color("red"),1,1)
        layout.addWidget(Color("blue"),1,0)
        layout.addWidget(Color("green"),0,1)
        layout.addWidget(Color("yellow"),2,2)

        """
        widget = QWidget()
        widget.setLayout(vlayout)#add layouts

        

        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()