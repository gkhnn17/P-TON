from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox


from _listform import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        #load Students
        self.loadStudents()

        #add new student
        self.ui.add_pushButton.clicked.connect(self.addStudent)

        #edit student
        self.ui.cut_pushButton.clicked.connect(self.editStudent)

        #delete Student
        self.ui.remove_pushButton.clicked.connect(self.removeStudent)
       
        #up
        self.ui.up_pushButton.clicked.connect(self.upStudent)

        #down
        self.ui.down_pushButton.clicked.connect(self.upStudent)

        #sort
        self.ui.sort_pushButton.clicked.connect(self.sortStudents)

        #close
        self.ui.exit_pushButton.clicked.connect(self.close)
    def loadStudents(self):
        self.ui.listWidget.addItems(["Ahmet","Ali","Johny"])
        self.ui.listWidget.setCurrentRow(0)


    def addStudent(self):
        currentIndex = self.ui.listWidget.currentRow()
        text,ok = QInputDialog.getText(self,"New student","Student Name")
        #getInt
        #getItem
        
        if ok and text is not None:
            self.ui.listWidget.insertItem(currentIndex,text)

    def editStudent(self):
        index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(index)



        if item is not None:
            text,ok = QInputDialog.getText(self,"Edit Student","Student Name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removeStudent(self):
        index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(index)

        if item is None:
            return

        q =QMessageBox.question(self,"Remove Student","Are you sure delete: ?"+ item.text(),QMessageBox.Yes|QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listWidget.takeItem(index)
            del item
        

    def upStudent(self):
        index = self.ui.listWidget.currentRow()

        if index >=1:
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index-1,item)
            self.ui.listWidget.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listWidget.currentRow()

        if index < self.ui.listWidget.count()-1:
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index+2,item)
            self.ui.listWidget.setCurrentItem(item)

    def sortStudents(self):
        self.ui.listWidget.sortItems()

    def close(self):
        quit()
def app():
    app =QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()