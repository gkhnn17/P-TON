import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUi()

    def initUi(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayi 1 : ")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1= QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(100,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi 2 : ")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2= QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(100,80)
        self.txt_sayi2.resize(200,32)


        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(100,130)
        #self.btn_topla.clicked.connect(self.toplama)
        self.btn_topla.clicked.connect(self.hesapla)
        self.btn_çıkar = QtWidgets.QPushButton(self)
        self.btn_çıkar.setText("Çıkar")
        self.btn_çıkar.move(100,180)

        self.btn_çarp = QtWidgets.QPushButton(self)
        self.btn_çarp.setText("Çarp")
        self.btn_çarp.move(100,230)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuc: ")
        self.lbl_sonuc.move(320,80)

        self.btn_böl = QtWidgets.QPushButton(self)
        self.btn_böl.setText("Böl")
        self.btn_böl.move(100,280)

    """
    def toplama(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("sonuç: " +str(result))
    """
    def hesapla(self):
        sender = self.sender().text()
        result = 0
        if sender == "Topla":
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("sonuç: " +str(result))
        #çarpma,böleme,çıkarma ...

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()