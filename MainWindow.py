from PyQt5 import QtGui, QtCore, QtWidgets, uic
import logging
from Button import *
from BtnDb import BtnDb
import pyttsx
debug_logger = logging.getLogger(__name__)


class Main(QtWidgets.QMainWindow):
    def __init__(self, db_logger=None):
        QtWidgets.QMainWindow.__init__(self, parent=None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()
        self.db_logger = db_logger
        self.btn_array = ButtonArray()

        # Add speech to text
        self.engine = pyttsx.init()
        self.engine.setProperty('rate', (self.engine.getProperty('rate')-75))
        self.engine.setProperty('volume', 100)
        self.slider.valueChanged.connect(self.update_volume())

        # Add button to the btn array
        for btn in self.create_buttons():
            self.btn_array.add_btn(btn)

    def update_volume(self):
        v = self.slider.value()
        self.engine.setProperty('volume',v)

    def on_btn_clicked(self, text):
        """
        Common slot for all
        :return:
        """
        self.engine.say(text)
        self.engine.runAndWait()

        if self.db_logger:
            self.db_logger.add_data(text)

        print (text)

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
        dispatcher = {'get_btns':     self.get_btns,
                      'set_btn_text': self.set_btn_text,
                      'update_image': self.update_btn}
        return dispatcher

    def update_btn(self, id, text, file_name):
        # Add to the database
        btn_db = BtnDb()
        btn_db.add_data(id, text, file_name)
        btn = self.btn_array.get_btn(int(id))
        btn.set_text(text)
        btn.set_pic(QtGui.QIcon(file_name), QtCore.QSize(btn.btn_width(), btn.btn_height()))
        btn.set_uri(file_name)

    def recreate_btn(self, id):
        pass

    def create_buttons(self):
        qbtns = [self.ui.btn1,
                 self.ui.btn2,
                 self.ui.btn3,
                 self.ui.btn4,
                 self.ui.btn5,
                 self.ui.btn6,
                 self.ui.btn7,
                 self.ui.btn8,
                 self.ui.btn9]

        btn_db = BtnDb()
        row = btn_db.get_btns()
        btns = []
        for i, btn in enumerate(row):
            btns.append(Button.builder()
                        .btn(qbtns[int(btn[0])])
                        .id(int(btn[0]))
                        .text(btn[1])
                        .pic(QtGui.QIcon(btn[2]))
                        .uri(btn[2])
                        .icon_size(QtCore.QSize(qbtns[i].width(), qbtns[i].height()))
                        .callback(self.on_btn_clicked)
                        .build())

        return btns
