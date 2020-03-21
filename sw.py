from PyQt5 import QtWidgets,QtGui,QtCore
from login import Ui_Loginmysql
from fix import Ui_Dialog
import pymysql
import sys,mysql,os
msg = ""
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_Loginmysql()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonclicked)
        self.ui.pushButton_2.clicked.connect(self.exit)
    def buttonclicked(self):
        user = self.ui.lineEdit.text()
        pwd = self.ui.lineEdit_2.text()
        ip = self.ui.lineEdit_4.text()
        #data = Data.view(user,pwd)
        data=mysql.loginsql(ip,user,pwd)
        if data != 'wrong':
            for i in data:
                self.ui.plainTextEdit.appendPlainText("{}\t{}\t{}".format(i[0],i[1],i[2]))
        else:
            self.ui.plainTextEdit.appendPlainText(data)
    def exit(self):
          sys.exit(app.exec_())
    
class MainWindow1(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow1,self)


        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())        