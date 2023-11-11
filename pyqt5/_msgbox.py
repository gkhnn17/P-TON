from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

from _msgboxform import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

       
        self.ui.exit_pushButton.clicked.connect(self.ShowDialog)


    def ShowDialog(self):
        result = QMessageBox.question(self,"Close Applicatation","Are you sure ?",QMessageBox.Ok |QMessageBox.Cancel | QMessageBox.No,QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print("Yeap")
            QtWidgets.qApp.quit()

        """
        msg = QMessageBox()
        msg.setWindowTitle("Close")
        msg.setText("Are you sure about it ?")
        #msg.setIcon(QMessageBox.Question)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok |QMessageBox.Cancel | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Cancel)    
        msg.setDetailedText("Detals is here riiight here look (.)(.)")
        
        

        x = msg.exec_()#comes a number
        print(x)
        button = msg.clickedButton()  # Get the clicked button
        if button is not None:
            self.popup_button(button)
        

    def popup_button(self,i):
        print(i.text())

        if i.text() == "OK":
            print("OKEY OKEY GOOd")
            QtWidgets.qApp.quit()
"""


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()