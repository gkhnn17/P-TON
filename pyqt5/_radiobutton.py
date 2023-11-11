import sys
from PyQt5 import QtWidgets
from _radiobuttonform import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tr_radioButton.setChecked(True)
        self.ui.lisans_radioButton_6.setChecked(True)

        self.ui.tr_radioButton.toggled.connect(self.onClickedCountry)
        self.ui.azari_radioButton_4.toggled.connect(self.onClickedCountry)
        self.ui.greek_radioButton_3.toggled.connect(self.onClickedCountry)
        self.ui.grmn_radioButton_2.toggled.connect(self.onClickedCountry)

        self.ui.lise_radioButton_5.toggled.connect(self.onClickedEdu)
        self.ui.lisans_radioButton_6.toggled.connect(self.onClickedEdu)
        self.ui.yksklisans_radioButton.toggled.connect(self.onClickedEdu)

        self.ui.country_Button.clicked.connect(self.getSelectedCountry)

    def onClickedEdu(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())

    def onClickedCountry(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())


    def getSelectedCountry(self):
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.country_lbl.setText(rb.text())

app =QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
