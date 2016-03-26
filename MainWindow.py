from PyQt5 import QtGui, QtCore, QtWidgets, uic
import logging
from Button import *

debug_logger = logging.getLogger(__name__)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()

        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.btn_array = ButtonArray()

        # Get the button
        btn1 = Button.builder()\
            .btn(self.ui.pushButton)\
            .id(len(self.btn_array))\
            .text(self.ui.pushButton.text())\
            .build()

        # Add button to the btn array
        self.btn_array.add_btn(btn1)

    def button_clicked(self):
        self.ui.pushButton.setText("Hello!")

    def update_button_text(self):
        self.ui.pushButton.setText("Hi!")


    ### All methods RPC methods ###
    def get_btns(self):
        return str(self.btn_array)

    def set_btn_text(self, id, text):
        try:
            self.btn_array[id].setText(text)
        except KeyError:
            pass

    ### RPC Calback Methods End ###
    
    def create_dispatcher(self):
        dispatcher = {'update_button_text' : self.update_button_text,
                      'get_btns': self.get_btns,
                      'set_btn_text': self.set_btn_text}
        return dispatcher
