
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from ekran1ui import Ui_ekran1 
from ekran2ui import Ui_ekran2

class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ekran1()
        self.ui.setupUi(self)
        self.ui.enterbutton.clicked.connect(self.enterence)

    def persons(self):
        persons = [
        {"ID": "23000040", "Şifre": "1122", "İsim": "Ahmet Yildirim"},
        {"ID": "22000025", "Şifre": "3344", "İsim": "Elif Öztürk"},
        {"ID": "23000027", "Şifre": "5566", "İsim": "Murat Doğan"},
        {"ID": "21000042", "Şifre": "7788", "İsim": "Yasemin Erdem"},
        {"ID": "1", "Şifre": "1", "İsim": "Gökhan"}

        ]
        return persons


    def enterence(self):
        entered_id = self.ui.id_input.text()
        entered_password = self.ui.password_input.text()

        for person in self.persons(): 
            if person["ID"] == entered_id and person["Şifre"] == entered_password:
                self.ui.mistakes.setText(f"Welcome, {person['İsim']}")
                self.open_ekran2(person["İsim"])
                self.close()
                print("yes")
                return
        msg =QMessageBox()
        msg.setWindowTitle("HATALI GİRİŞ")
        msg.setText("Please check again your ID or password")
        msg.setIcon(QMessageBox.Warning)

        self.ui.mistakes.setText("Login failed. Please check your inputs.")
        print("no")
        msg.exec_()


    def open_ekran2(self, name):
        self.ekran2_window =Ekran2(name)
        self.ekran2_window.show()


class Ekran2(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.ui = Ui_ekran2()
        self.ui.setupUi(self)
        self.ui.welcome_label.setText(f"HOŞGELDİNİZ, {name}")

"""
from PyQt5.QtWidgets import QApplication, QMainWindow
from ekran1ui import Ui_ekran1 

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_ekran1()
    ui.setupUi(window)
    interface = Interface()
    interface.ui = ui  # Assign the UI to the Interface
    window.show()
    sys.exit(app.exec_())

"""