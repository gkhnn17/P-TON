import sqlite3

class Table:
    def __init__(self):
        self.connection = sqlite3.connect("Share.db")

        self.mycursor = self.connection.cursor()

    def create(self):
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Shares(
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Buying REAL,
                        Selling REAL,
                        Unit INTEGER, 
                        Date TEXT
                        )
                        """)

        self.connection.commit()
    
    def close_connection(self):
        self.connection.close()

creater = Table()
creater.create()
