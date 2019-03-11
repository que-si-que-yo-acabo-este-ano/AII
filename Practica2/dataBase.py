#encoding:utf-8
import sqlite3

def startDataBase():
    conn = sqlite3.connect('test.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    # conn.execute("DROP TABLE IF EXISTS FORUM")   
    conn.execute('''CREATE TABLE IF NOT EXISTS FORUM
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       TITLE        TEXT       NOT NULL,
       LINK         TEXT       NOT NULL,
       AUTHOR       TEXT       NOT NULL,
       DATE         TEXT       NOT NULL,
       ANSWERS      INTEGER    NOT NULL,
       VISITS       INTEGER    NOT NULL);''')
    conn.close()

def insertDataBase():
    pass