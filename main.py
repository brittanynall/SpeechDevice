from PyQt5 import QtGui, QtCore, QtWidgets, uic
from datetime import datetime
from PyQt5.QtCore import pyqtSlot
from LogData import LogData

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()
        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.db = LogData()


    def button_clicked(self):
        #time = datetime.datetime.now()
        action = self.ui.pushButton.text()
        self.db.add_data(action)
        self.db.print_data()

if __name__ == '__main__':
    import sys
 
    app = QtWidgets.QApplication(sys.argv)

    screen = Main()
    screen.show()
 
    sys.exit(app.exec_())