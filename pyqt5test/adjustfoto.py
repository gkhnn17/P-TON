# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adjustfoto.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(0, 40, 351, 261))
        self.foto.setText("")
        #my foto
        script_path = os.path.dirname(os.path.abspath(__file__))
        photo_path1 = os.path.join(script_path, "a - Kopya.jpg")
        

        self.foto.setPixmap(QtGui.QPixmap(photo_path1))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")
        self.AStronout = QtWidgets.QPushButton(self.centralwidget)
        self.AStronout.setGeometry(QtCore.QRect(20, 430, 93, 101))
        self.AStronout.setObjectName("AStronout")
        self.itisme = QtWidgets.QPushButton(self.centralwidget)
        self.itisme.setGeometry(QtCore.QRect(230, 430, 93, 101))
        self.itisme.setObjectName("itisme")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.AStronout.clicked.connect(self.show_ast)
        self.itisme.clicked.connect(self.show_its)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AStronout.setText(_translate("MainWindow", "Astonout"))
        self.itisme.setText(_translate("MainWindow", "it is me"))

    def show_ast(self):
        self.foto.setPixmap(QtGui.QPixmap("pyqt5test/a - Kopya.jpg"))

    def show_its(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        photo_path2 = os.path.join(script_path, "science-fiction-digital-art-concept-art-artwork-fantasy-art-fan-art-1717397-wallhere.com.jpg")
        self.foto.setPixmap(QtGui.QPixmap(photo_path2))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
