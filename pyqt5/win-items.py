import typing
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
 
        self.setWindowTitle("First app")
        self.setGeometry(200,200,500,500)#1,2 ->location,3,4 ->size
        self.setToolTip("My tool tip")
        
        self.initUi()

    def initUi(self):

        self.lbl_name =QtWidgets.QLabel(self)
        self.lbl_name.setText("Your name: ")
        self.lbl_name.move(50,50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surname: ")
        self.lbl_surname.move(50,90)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("RESULT")
        self.lbl_result.move(170,180)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,50)
        self.txt_name.resize(200,32)


        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,90)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(150,130)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        print("your name : " + self.txt_name.text())
        self.lbl_result.setText("NAME: " + self.txt_name.text() )

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    #win.txt_name

window()

# QLabel
# QComboBox ->multiple selection
# QCheckBox 
# QRadioButton
# QPush Button
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar