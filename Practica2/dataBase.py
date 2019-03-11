#encoding:utf-8
import sqlite3

def startDataBase():
    conn = sqlite3.connect('ulalox.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    # conn.execute("DROP TABLE IF EXISTS FORUM")   
    conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       MARCA          TEXT       NOT NULL,
       NOMBRE         TEXT       NOT NULL,
       LINK           TEXT       NOT NULL,
       PRECIO         DOUBLE       NOT NULL,
       PRECIO_OFERTA      INTEGER);''')
    

def insertDataBase():
    conn = sqlite3.connect('ulalox.db')
    conn.execute("""INSERT INTO FORUM (MARCA,NOMBRE,LINK,PRECIO,PRECIO_OFERTA) VALUES ("Gluton","Artg","www.gluten.com",2.0,null)""")
    conn.commit()
    conn.close()    

startDataBase()