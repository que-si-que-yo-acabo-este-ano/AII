#encoding:utf-8

import urllib.request, re
import sqlite3
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding


def startDataBase():
    conn = sqlite3.connect('ulalox.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    conn.execute("DROP TABLE IF EXISTS DIARIO")   
    conn.execute('''CREATE TABLE IF NOT EXISTS DIARIO
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       MARCA          TEXT       NOT NULL,
       NOMBRE         TEXT       NOT NULL,
       LINK           TEXT       NOT NULL,
       PRECIO         DOUBLE     NOT NULL,
       PRECIO_OFERTA  DOUBLE);''')
    conn.close()

def open_url(url,file):
    try:
        urllib.request.urlretrieve(url,file)
        return file
    except:
        print  ("Error al conectarse a la página")
        return None
    
def beautifulRead(html):
    return BeautifulSoup(html,"html.parser")


def lecturaWeb():
    file="DiarioDeportivo"
    open_url("http://resultados.as.com/resultados/futbol/primera/2017_2018/calendario/",file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    

# for x in lecturaWeb():
#     print(x)
# print(lecturaWeb())
        
    #dataBase.startDataBase()
        
        
       
        