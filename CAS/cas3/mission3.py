# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mission3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Mission3Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 751)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 751, 751))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.492174, y1:0.018, x2:0.502, y2:1, stop:0.432836 rgba(255, 53, 56, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.widget.setObjectName("widget")
        self.image_label = QtWidgets.QLabel(self.widget)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 751, 751))
        self.image_label.setObjectName("image_label")
        self.answer_button = QtWidgets.QPushButton(self.widget)
        self.answer_button.setGeometry(QtCore.QRect(280, 620, 201, 111))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        self.answer_button.setFont(font)
        self.answer_button.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(201, 255, 255);\n"
"font: 75 8pt \"MS Serif\";")
        self.answer_button.setObjectName("answer_button")
        self.southeast_west_label = QtWidgets.QLabel(self.widget)
        self.southeast_west_label.setGeometry(QtCore.QRect(450, 470, 291, 51))
        self.southeast_west_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.southeast_west_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southeast_west_label.setObjectName("southeast_west_label")
        self.northeast_label = QtWidgets.QLabel(self.widget)
        self.northeast_label.setGeometry(QtCore.QRect(450, 120, 291, 51))
        self.northeast_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(170, 0, 0);")
        self.northeast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northeast_label.setObjectName("northeast_label")
        self.southwest_label = QtWidgets.QLabel(self.widget)
        self.southwest_label.setGeometry(QtCore.QRect(10, 410, 291, 51))
        self.southwest_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(170, 0, 0);")
        self.southwest_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southwest_label.setObjectName("southwest_label")
        self.northwest_label = QtWidgets.QLabel(self.widget)
        self.northwest_label.setGeometry(QtCore.QRect(10, 120, 291, 51))
        self.northwest_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"\n"
"color: rgb(170, 0, 0);\n"
"")
        self.northwest_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northwest_label.setObjectName("northwest_label")
        self.northeast_west_label = QtWidgets.QLabel(self.widget)
        self.northeast_west_label.setGeometry(QtCore.QRect(450, 180, 291, 51))
        self.northeast_west_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.northeast_west_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northeast_west_label.setObjectName("northeast_west_label")
        self.northeast_south_label = QtWidgets.QLabel(self.widget)
        self.northeast_south_label.setGeometry(QtCore.QRect(450, 240, 291, 51))
        self.northeast_south_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.northeast_south_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northeast_south_label.setObjectName("northeast_south_label")
        self.northeast_southwest_label = QtWidgets.QLabel(self.widget)
        self.northeast_southwest_label.setGeometry(QtCore.QRect(450, 300, 291, 51))
        self.northeast_southwest_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.northeast_southwest_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northeast_southwest_label.setObjectName("northeast_southwest_label")
        self.northwest_east_label = QtWidgets.QLabel(self.widget)
        self.northwest_east_label.setGeometry(QtCore.QRect(10, 180, 291, 51))
        self.northwest_east_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.northwest_east_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northwest_east_label.setObjectName("northwest_east_label")
        self.northwest_south_label = QtWidgets.QLabel(self.widget)
        self.northwest_south_label.setGeometry(QtCore.QRect(10, 240, 291, 51))
        self.northwest_south_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.northwest_south_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northwest_south_label.setObjectName("northwest_south_label")
        self.northwest_southeast_label = QtWidgets.QLabel(self.widget)
        self.northwest_southeast_label.setGeometry(QtCore.QRect(10, 300, 291, 51))
        self.northwest_southeast_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.northwest_southeast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.northwest_southeast_label.setObjectName("northwest_southeast_label")
        self.southeast_north_label = QtWidgets.QLabel(self.widget)
        self.southeast_north_label.setGeometry(QtCore.QRect(450, 530, 291, 51))
        self.southeast_north_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.southeast_north_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southeast_north_label.setObjectName("southeast_north_label")
        self.southeast_northwest_label = QtWidgets.QLabel(self.widget)
        self.southeast_northwest_label.setGeometry(QtCore.QRect(450, 590, 291, 51))
        self.southeast_northwest_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.southeast_northwest_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southeast_northwest_label.setObjectName("southeast_northwest_label")
        self.southeast_label = QtWidgets.QLabel(self.widget)
        self.southeast_label.setGeometry(QtCore.QRect(450, 410, 291, 51))
        self.southeast_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(170, 0, 0);")
        self.southeast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southeast_label.setObjectName("southeast_label")
        self.southwest_east_label = QtWidgets.QLabel(self.widget)
        self.southwest_east_label.setGeometry(QtCore.QRect(10, 470, 291, 51))
        self.southwest_east_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.southwest_east_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southwest_east_label.setObjectName("southwest_east_label")
        self.southwest_north_label = QtWidgets.QLabel(self.widget)
        self.southwest_north_label.setGeometry(QtCore.QRect(10, 530, 291, 51))
        self.southwest_north_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.southwest_north_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southwest_north_label.setObjectName("southwest_north_label")
        self.southwest_northeast_label = QtWidgets.QLabel(self.widget)
        self.southwest_northeast_label.setGeometry(QtCore.QRect(10, 590, 291, 51))
        self.southwest_northeast_label.setStyleSheet("font: 57 14pt \"Dubai Medium\";\n"
"color: rgb(85, 0, 255);")
        self.southwest_northeast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.southwest_northeast_label.setObjectName("southwest_northeast_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.image_label.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.answer_button.setText(_translate("Dialog", "LOCATİON"))
        self.southeast_west_label.setText(_translate("Dialog", "-"))
        self.northeast_label.setText(_translate("Dialog", "-"))
        self.southwest_label.setText(_translate("Dialog", "-"))
        self.northwest_label.setText(_translate("Dialog", "-"))
        self.northeast_west_label.setText(_translate("Dialog", "-"))
        self.northeast_south_label.setText(_translate("Dialog", "-"))
        self.northeast_southwest_label.setText(_translate("Dialog", "-"))
        self.northwest_east_label.setText(_translate("Dialog", "-"))
        self.northwest_south_label.setText(_translate("Dialog", "-"))
        self.northwest_southeast_label.setText(_translate("Dialog", "-"))
        self.southeast_north_label.setText(_translate("Dialog", "-"))
        self.southeast_northwest_label.setText(_translate("Dialog", "-"))
        self.southeast_label.setText(_translate("Dialog", "-"))
        self.southwest_east_label.setText(_translate("Dialog", "-"))
        self.southwest_north_label.setText(_translate("Dialog", "-"))
        self.southwest_northeast_label.setText(_translate("Dialog", "-"))
