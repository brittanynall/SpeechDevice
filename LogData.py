import sqlite3
import sys

class LogData():
    def __init__(self):
        self.conn = sqlite3.connect('loggeddata.db')
        self.cursor = self.conn.cursor()
        self.conn.execute('CREATE TABLE IF NOT EXISTS LoggedData(datetime , action TEXT)')

    #adds the data to the database
    def add_data(self, action):
        self.cursor.execute("INSERT INTO LoggedData (datetime, action) VALUES (CURRENT_TIMESTAMP, ?)", [action])
        self.commit()

    #creates a log entry (action, datetime) from each row in the database
    def create_log(self):
        self.loggeddata = []
        logs = self.cursor.execute("SELECT action, datetime FROM LoggedData")

        for l in logs:
            entry = LogEntry(action=l[0],datetime=l[1])
            self.loggeddata.append(entry)

    #prints the data to the console
    def print_data(self):
        row = self.cursor.execute("SELECT action, datetime FROM LoggedData")
        for col in row:
            print(col)

    #commit data added
    def commit(self):
        self.conn.commit()

    def __str__(self):
        l = []
        for entry in self.loggeddata:
            l.append(entry.get_dict())
        d = {'buttons': l}
        return json.dumps(d)

    #close database
    def __del__(self):
        self.conn.close()

##Log Entry : action, datetime
class LogEntry():
    def __init__(self,action=None,datetime=None):
        self.action = action
        self.datetime = datetime

#action and datetime for json
    def get_dict(self):
        return {'action' : self.action, 'datetime': self.datatime}



if __name__ == "__main__":
    logdata = LogData()
    logdata.print_data()