import sqlite3

class Table:
    def __init__(self):
        self.connection = sqlite3.connect("Share.db")