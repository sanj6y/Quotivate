import sqlite3
import pandas as pd

class UserDatabase:
    
    def __init__(self, dbname='user.db'):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')

    def addUser(self, name, email):
        self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        self.conn.commit()

    def removeUser(self, name):
        self.cursor.execute('DELETE FROM users WHERE name = ?', (name,))
        self.conn.commit()

    def getUsers(self):
        df = pd.read_sql_query('SELECT * FROM users', self.conn)
        return df
