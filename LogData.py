import sqlite3
import sys

class LogData():
    def __init__(self):
        self.connect()
        try:
            self.c.execute('CREATE TABLE IF NOT EXISTS LoggedData(datetime , action TEXT)')
        except:
            pass

    def connect(self):
        self.conn = sqlite3.connect('loggeddata.db')
        #mem = sqlite3.Connection(':memory:')
        self.c = self.conn.cursor()

    def add_data(self, action):
        self.connect()
        try:
            self.c.execute("INSERT INTO LoggedData (datetime, action) VALUES(CURRENT_TIMESTAMP, :ACT)", {'ACT':action})
        except:
            self.conn.rollback()

        self.conn.commit()
        self.c.close()

    def print_data(self):
        self.connect()
        row = self.c.execute("SELECT action, datetime FROM LoggedData")
        for col in row:
            print col

        self.c.close()




