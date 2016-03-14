from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from NetworkService import NetworkService
from RpcService import RpcServer
from threading import Thread

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

    # instantiate new window
    main_window = Main()
    main_window.show()

    # start the rpc server
    try:
        server = RpcServer(main_window)
        server_thread = Thread(target=server.start)
        server_thread.start()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass