from PyQt5.QtWidgets import *
from odev_gui import Ui_MainWindow
from PyQt5 import QtGui, QtCore, QtWidgets

class Interface(QMainWindow):

        def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                