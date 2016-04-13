import sqlite3


class BtnDb:
    def __init__(self):
        self.conn = sqlite3.connect('button.db')
        self.cursor = self.conn.cursor()
        self.conn.execute('CREATE TABLE IF NOT EXISTS Button(id TEXT, txt TEXT, image TEXT)')

    def add_data(self, id, txt, image):
        if self.exists(id):
            self.update(id, txt, image)
        else:
            self.cursor.execute("INSERT INTO Button (id, txt, image) VALUES (?, ?, ?)", [id, txt, image])
        self.commit()

    def get_data(self, id):
        self.cursor.execute('SELECT * from Button where id =?', [id])
        return self.cursor.fetchall()

    def get_btns(self):
        self.cursor.execute('SELECT * from Button ORDER BY id')
        return self.cursor.fetchall()

    def get_total(self):
        self.cursor.execute('SELECT count(*) from Button')
        return self.cursor.fetchone()[0]

    def update(self, id, txt, image):
        self.cursor.execute("UPDATE Button SET txt=?, image=? WHERE id=?", [txt, image, id])
        self.commit()

    def exists(self, id):
        self.cursor.execute("SELECT EXISTS(SELECT 1 FROM Button WHERE id=? LIMIT 1)", [id])
        if self.cursor.fetchone()[0] == 0: return False
        else: return True

    def print_data(self):
        row = self.cursor.execute("SELECT id, txt, image FROM Button")
        for col in row:
            print(col)

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    logdata = BtnDb()
    if True:
        logdata.add_data('0', 'milk',      'images/milk.jpg')
        logdata.add_data('1', 'bathroom',  'images/bathroom.jpg')
        logdata.add_data('2', 'blanket',   'images/blanket.jpg')
        logdata.add_data('3', 'mom',       'images/mom.jpg')
        logdata.add_data('4', 'juice',     'images/juice.jpg')
        logdata.add_data('5', 'tv',        'images/tv.jpg')
        logdata.add_data('6', 'toilet',    'images/toilet_signs.jpg')
        logdata.add_data('7', 'snack',     'images/fruit_snack.jpg')
        logdata.add_data('7', 'carrot',    'images/carrot.jpg')
        logdata.add_data('8', 'bed',       'images/carrot.jpg')

    logdata.print_data()
    print(logdata.exists('0'))
    print(logdata.get_total())
