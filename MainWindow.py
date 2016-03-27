from PyQt5 import QtGui, QtCore, QtWidgets, uic
import logging
from Button import *

debug_logger = logging.getLogger(__name__)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()

        self.btn_array = ButtonArray()

        # Add button to the btn array
        for btn in self.create_buttons():
            self.btn_array.add_btn(btn)

    def button_clicked(self):
        self.ui.pushButton.setText("Hello!")

    def update_button_text(self):
        self.ui.pushButton.setText("Hi!")

    ### All methods RPC methods ###
    def get_btns(self):
        debug_logger.debug(str(self.btn_array))
        return str(self.btn_array)

    def set_btn_text(self, id, text):
        try:
            self.btn_array[id].setText(text)
        except KeyError:
            pass

    ### RPC Calback Methods End ###

    def create_dispatcher(self):
        dispatcher = {'update_button_text': self.update_button_text,
                      'get_btns': self.get_btns,
                      'set_btn_text': self.set_btn_text}
        return dispatcher

    def create_buttons(self):
        qbtns = {'milk':    [self.ui.btn1, 'images/milk.jpg'],
                 'bathroom':[self.ui.btn2, 'images/bathroom.jpg'],
                 'blanket': [self.ui.btn3, 'images/blanket.jpg'],
                 'mom':     [self.ui.btn4, 'images/mom.jpg'],
                 'juice':   [self.ui.btn5, 'images/juice.jpg'],
                 'tv':      [self.ui.btn6, 'images/tv.jpg'],
                 'toilet':  [self.ui.btn7, 'images/toilet_signs.png'],
                 'snack':   [self.ui.btn8, 'images/fruit_snack.jpg'],
                 'carrot':  [self.ui.btn9, 'images/carrot.jpg']}

        k = ['milk','bathroom','blanket','mom','juice','tv','toilet','snack','carrot']
        btns = []
        for i,btn in enumerate(k):
            btns.append(Button.builder()
                        .btn(qbtns[btn][0])
                        .id(i)
                        .text(btn)
                        .pic(QtGui.QIcon(qbtns[btn][1]))
                        .uri(qbtns[btn][1].split('/')[1])
                        .icon_size(QtCore.QSize(qbtns[btn][0].width(), qbtns[btn][0].height()))
                        .build())

        return btns
