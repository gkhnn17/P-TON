import sqlite3

class Table:
    def __init__(self):
        self.connection = sqlite3.connect("Share.db")
        self.mycursor = self.connection.cursor()

    def create(self):
        self.mycursor.execute("""CREATE TABLE Shares,
                              (Buying REAL,
                              Selling REAL,
                              Unit INTEGER,
                              Date TEXT)
                              """)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()