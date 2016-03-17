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
        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.db = LogData()
        self.sp = Speech()

    def button_clicked(self):
        #time = datetime.datetime.now()
        action = self.ui.pushButton.text()
        self.db.add_data(action)
        self.sp.say_action(action)

if __name__ == '__main__':
    import sys
 
    app = QtWidgets.QApplication(sys.argv)

    screen = Main()
    screen.show()
 
    sys.exit(app.exec_())