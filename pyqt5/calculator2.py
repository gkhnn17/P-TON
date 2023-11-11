import typing
from PyQt5 import QtCore, QtWidgets
import sys


from Mainwindow import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0
        if sender == "Toplama":
            result = int(self.ui.txtsayi1.toPlainText()) + int(self.ui.txtsayi2.toPlainText())
        self.ui.label_3.setText("sonuç: " + str(result))
        #çarpma,böleme,çıkarma ...



def app():
    application = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(application.exec_())

app()