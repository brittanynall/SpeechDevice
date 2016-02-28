from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
import Log

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()
        self.ui.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.ui.pushButton.setText("Hello!")


if __name__ == '__main__':
    import sys
 
    app = QtWidgets.QApplication(sys.argv)

    screen = Main()
    screen.show()
 
    sys.exit(app.exec_())