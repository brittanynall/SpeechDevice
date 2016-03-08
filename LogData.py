import sqlite3

class LogData():
    def __init__(self):
        #code to recognize already existing database
        sqlite_file = 'logged_data.sqlite'
        self.logging_table = 'logged_table'
        self.action_col = 'action'
        self.col_type = 'TEXT'
        self.datetime_col = 'datetime'

        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS {lt} ({ac} {act})' .format(lt=self.logging_table, ac = self.action_col, act = self.col_type))
        try:
            self.c.execute("ALTER TABLE {lt} ADD COLUMN'{dt}' " .format(lt=self.logging_table, dt = self.datetime_col))
        except:
            pass

    def add_data(self, action):
        self.c.execute("INSERT INTO {lt} ({ac}, {dt}) VALUES('{act}', CURRENT_TIMESTAMP)" .format(lt = self.logging_table, ac = self.action_col, dt = self.datetime_col, act = action))

    def print_data(self):
        row = self.c.execute("SELECT action, datetime FROM {lt}" .format(lt=self.logging_table))
        for c in row:
            print c[0]
            print c[1]
