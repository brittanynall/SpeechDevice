import sqlite3
import sys

class LogData():
    def __init__(self):
        self.connect()
        try:
            self.c.execute('CREATE TABLE IF NOT EXISTS LoggedData(datetime , action TEXT)')
        except:
            pass

    def add_data(self, action):
        self.connect()
        try:
            self.c.execute("INSERT INTO LoggedData (datetime, action) VALUES(CURRENT_TIMESTAMP, :ACT)", {'ACT':action})
        except:
            self.conn.rollback()

        self.conn.commit()
        self.print_data()
        self.c.close()

    def print_data(self):
        row = self.c.execute("SELECT action, datetime FROM LoggedData")
        for col in row:
            print col

    def storeDB(self):
        mem = sqlite3.Connection(':memory:')
        memcon = mem.cursor()
        try:
            mem.execute('CREATE TABLE IF NOT EXISTS LoggedData(datetime , action TEXT)')
        except:
            pass
        try:
            row = self.c.execute("SELECT datetime, action FROM LoggedData")
            for col in row:
                mem.execute("INSERT INTO LoggedData (datetime, action) VALUES(:TIM, :ACT)", {'TIM':col[0], 'ACT':col[1]})
        except:
            memcon.rollback()

        mem.commit()
        mem.close()
        self.c.execute("DELETE FROM LoggedData")


    def connect(self):
        self.conn = sqlite3.connect('loggeddata.db')
        self.c = self.conn.cursor()

