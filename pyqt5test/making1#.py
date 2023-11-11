import sys
import typing
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QStackedWidget


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("pyqt5test/welcome.ui",self)#loading
        self.login_button.clicked.connect(self.gotologin)
        self.create_button.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)#flip to different .ui
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def signupfunction(self):
        user = self.id_field.text()
        password = self.password_field.text()
        password2= self.password2_field.text()

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("pyqt5test/login.ui",self)#load login

        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.loginfunction)

    def persons(self):
        persons = [
        {"ID": "23000040", "Şifre": "1122", "İsim": "Ahmet Yildirim"},
        {"ID": "22000025", "Şifre": "3344", "İsim": "Elif Öztürk"},
        {"ID": "23000027", "Şifre": "5566", "İsim": "Murat Doğan"},
        {"ID": "21000042", "Şifre": "7788", "İsim": "Yasemin Erdem"},
        {"ID": "1", "Şifre": "1", "İsim": "Gökhan"}
        ]
        return persons

    def loginfunction(self):
        user = self.id_field.text()
        password = self.password_field.text()
    
        if len(user)==0 or len(password)==0:
            self.error_label.setText("Please input all fields")

        else:
            for person in self.persons():
                if person["ID"] ==user and person["Şifre"] == password:
                    print("Succesfully logged in.")
                    self.error_label.setText("")
                else:
                    self.error_label.setText("Invalid username or password")

                    

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen,self).__init__()
        loadUi("pyqt5test/createacc.ui",self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)#pasword type
        self.password2_field.setEchoMode(QtWidgets.QLineEdit.Password)
        


#main
app = QApplication(sys.argv)#need this
welcome =WelcomeScreen()
widget= QStackedWidget()#we can move screen eachother
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(431)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")


