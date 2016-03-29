from PyQt5 import QtGui, QtCore, QtWidgets, uic
from datetime import datetime
from PyQt5.QtCore import pyqtSlot
from LogData import LogData
from Speech import Speech

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()
        self.ui.pushButton.clicked.connect(self.button1_clicked)
        self.ui.pushButton_2.clicked.connect(self.button2_clicked)
        self.ui.pushButton_3.clicked.connect(self.button3_clicked)
        self.ui.pushButton_4.clicked.connect(self.button4_clicked)
        self.ui.pushButton_5.clicked.connect(self.button5_clicked)
        self.ui.pushButton_6.clicked.connect(self.button6_clicked)
        self.ui.pushButton_7.clicked.connect(self.button7_clicked)
        self.ui.pushButton_8.clicked.connect(self.button8_clicked)
        self.ui.pushButton_9.clicked.connect(self.button9_clicked)
        self.db = LogData()
        self.sp = Speech()

    def button1_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton.text()
        self.db.add_data(action)
        #self.sp.say_action(action)

    def button2_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_2.text()
        self.db.add_data(action)
        #self.sp.say_action(action)

    def button3_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_3.text()
        self.db.add_data(action)
        #self.sp.say_action(action)

    def button4_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_4.text()
        self.db.add_data(action)
        #self.sp.say_action(action)

    def button5_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_5.text()
        self.db.add_data(action)
        #self.sp.say_action(action)

    def button6_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_6.text()
        self.db.add_data(action)
        #self.sp.say_action(action)

    def button7_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_7.text()
        self.db.add_data(action)
        self.db.print_data()
        #self.sp.say_action(action)

    def button8_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_8.text()
        self.db.add_data(action)
       # self.sp.say_action(action)

    def button9_clicked(self, num):
        #time = datetime.datetime.now()
        action = self.ui.pushButton_9.text()
        self.db.add_data(action)
       # self.sp.say_action(action)

if __name__ == '__main__':
    import sys
 
    app = QtWidgets.QApplication(sys.argv)

    screen = Main()
    screen.show()
 
    sys.exit(app.exec_())