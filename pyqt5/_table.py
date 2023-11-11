import typing
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidgetItem

from _tableform import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.pushButton.clicked.connect(self.saveProduct)
        self.ui.products_tableWidget.doubleClicked.connect(self.doubleClicked)
    
    def doubleClicked(self):
        for item in self.ui.products_tableWidget.selectedItems():
            print(item.row(),item.column(),item.text())
    
    def saveProduct(self):
        name = self.ui.lineEdit.text()
        price = self.ui.lineEdit_2.text()
        if name and price is not None:
            rowCount = self.ui.products_tableWidget.rowCount()
            self.ui.products_tableWidget.insertRow(rowCount)
            self.ui.products_tableWidget.setItem(rowCount,0,QTableWidgetItem(QTableWidgetItem(name)))
            self.ui.products_tableWidget.setItem(rowCount,1,QTableWidgetItem(QTableWidgetItem(price)))


    def loadProducts(self):
        

        products = [
            {"name": "Samsung S5", "price": 2000},
            {"name": "Samsung S6", "price": 3000},
            {"name": "Samsung S7", "price": 4000},
            {"name": "Samsung S8", "price": 53000},
        ]
    
        self.ui.products_tableWidget.setRowCount(len(products))
        self.ui.products_tableWidget.setColumnCount(2)
        rowIndex = 0
        for product in products:
            self.ui.products_tableWidget.setItem(rowIndex,0,QTableWidgetItem(product["name"]))
            self.ui.products_tableWidget.setItem(rowIndex,1,QTableWidgetItem(str(product["price"])))
            rowIndex +=1
        self.ui.products_tableWidget.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.products_tableWidget.setColumnWidth(0,300)
        """
        self.ui.products_tableWidget.setItem(0,0,QTableWidgetItem("Samsung S5"))
        self.ui.products_tableWidget.setItem(0,1,QTableWidgetItem("2000"))
        self.ui.products_tableWidget.setItem(1,0,QTableWidgetItem("Samsung S6"))
        self.ui.products_tableWidget.setItem(1,1,QTableWidgetItem("3000"))
"""

def app():
    app =QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()