#encoding:utf-8

import urllib.request, re
import sqlite3
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding


def startDataBase():
    conn = sqlite3.connect('diario.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    conn.execute("DROP TABLE IF EXISTS DIARIO")
    conn.execute('''CREATE TABLE IF NOT EXISTS DIARIO
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       JORNADA            INTEGER       NOT NULL,
       LOCAL              TEXT       NOT NULL,
       VISITANTE          TEXT       NOT NULL,
       GOLES_LOCALES      INTEGER       NOT NULL,
       GOLES_VISITANTES   INTEGER     NOT NULL,
       LINK               TEXT NOT NULL);''')
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
    jornadas = []
    i = 1
    for jornada in soup.find_all("tbody"): #jornadas
        jornadaBD = []
        for partido in jornada.find_all("tr"):
            #equipos print(partido.find("span",attrs={"class","nombre-equipo"}).get_text())
            local = partido.find("td",attrs={"class","col-equipo-local"}).find("span",attrs={"class","nombre-equipo"}).get_text()
            visitante = partido.find("td",attrs={"class","col-equipo-visitante"}).find("span",attrs={"class","nombre-equipo"}).get_text()
            resultado = partido.find("td",attrs={"class","col-resultado"}).find("a").get_text().split()
            golesLocales = resultado[0]
            golesVisitantes = resultado[2]
            link = partido.find("td",attrs={"class","col-resultado"}).find("a").get("href")
            #print(local,int(golesLocales),"-",int(golesVisitantes),visitante,link)
            jornadaBD.append([i,local,visitante,int(golesLocales),int(golesVisitantes),link])
        jornadas.append(jornadaBD)
        i+=1
    print(jornadas)

lecturaWeb()

# for x in lecturaWeb():
#     print(x)
# print(lecturaWeb())
        
    #dataBase.startDataBase()
        
        
       
        