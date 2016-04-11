import json

class Button:
    def __init__(self, q_btn, id, text=None, uri=None, pic=None, icon_size=None, callback=None):
        self.q_btn = q_btn
        self.id = id
        self.text = text
        self.pic = pic
        self.uri = uri
        self.callback = callback
        self.q_btn.clicked.connect(self.btn_pressed)
        self.q_btn.setText(text)

        if pic:
            self.q_btn.setIcon(pic)
            if icon_size: self.q_btn.setIconSize(icon_size)

    def get_dict(self):
        return {'id' : self.id, 'text' : self.text, 'uri' : self.uri}

    def btn_pressed(self):
        self.callback(self.text)

    @staticmethod
    def builder():
        return ButtonBuilder()

class ButtonBuilder:

    def btn(self, btn):
        self.btn = btn
        return self

    def id(self, id):
        self.id = id
        return self

    def text(self, text=None):
        self.text = text
        return self

    def pic(self, pic=None):
        self.pic = pic
        return self

    def icon_size(self, icon_size=None):
        self.icon_size = icon_size
        return self

    def uri(self, uri=None):
        self.uri = uri
        return self

    def callback(self, callback):
        self.callback = callback
        return self

    def build(self):
        return Button(q_btn=self.btn,
                      id=self.id,
                      text=self.text,
                      pic=self.pic,
                      uri=self.uri,
                      icon_size=self.icon_size,
                      callback=self.callback)

class ButtonArray:
    def __init__(self):
        self.btn_list = []
        self.curent = 0

    def add_btn(self, btn):
        self.btn_list.append(btn)

    def __iter__(self):
        return self

    def next(self):
        if self.curent < len(self.btn_list):
            self.curent += 1
            return self.btn_list[self.curent - 1]
        else:
            raise StopIteration

    def __getitem__(self, id):
        for btn in self.btn_list:
            if btn.id == id: return btn.q_btn
        else: raise KeyError


    def __len__(self):
        return len(self.btn_list)

    def __str__(self):
        l = []
        for btn in self.btn_list:
            l.append(btn.get_dict())
        d = {'buttons': l}
        return json.dumps(d)