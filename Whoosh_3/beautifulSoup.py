#encoding:utf-8

import urllib.request, re
import sqlite3
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding
from numpy import insert
from datetime import datetime
from whoosh.index import create_in,open_dir
from whoosh.fields import Schema, TEXT, DATETIME, ID, KEYWORD, STORED, NUMERIC
from whoosh.qparser import QueryParser
from whoosh import qparser
import os
from pip._vendor.distlib.version import get_scheme
from datetime import datetime
from whoosh.searching import Searcher
from whoosh.query import *
from whoosh.qparser.dateparse import DateParserPlugin

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
    
def insertDataBase(jornadas):
    conn = sqlite3.connect('diario.db')
    for jornada in jornadas:
        conn.execute("""INSERT INTO DIARIO (JORNADA,LOCAL,VISITANTE,GOLES_LOCALES,GOLES_VISITANTES,LINK) VALUES (?,?,?,?,?,?)""",(jornada[0],jornada[1],jornada[2],jornada[3],jornada[4],jornada[5]))
    conn.commit()
    conn.close()   

def selectDataBaseCount():
    conn = sqlite3.connect('diario.db')
    num = conn.execute("""SELECT COUNT(*) FROM DIARIO""")
    return num.fetchone()[0]


def selectDataBaseJornadas():
    conn = sqlite3.connect('diario.db')
    rows = conn.execute("""SELECT JORNADA,LOCAL,VISITANTE,GOLES_LOCALES,GOLES_VISITANTES,LINK FROM DIARIO""")
    res = []
    for jornada in rows.fetchall():
        res.append(jornada)
    conn.close()
    return res 

def selectDataBasePartidosPorJornada(jornada):
    conn = sqlite3.connect('diario.db')
    rows = conn.execute("""SELECT JORNADA,LOCAL,VISITANTE,GOLES_LOCALES,GOLES_VISITANTES,LINK FROM DIARIO WHERE JORNADA='{0}'""".format(jornada))
    res = []
    for jornada in rows.fetchall():
        res.append(jornada)
    conn.close()
    return res 

def selectDataBaseGoles(jornada,local,visitante):
    conn = sqlite3.connect('diario.db')
    row = conn.execute("""SELECT LINK FROM DIARIO WHERE JORNADA='{0}' AND LOCAL='{1}' AND VISITANTE='{2}'""".format(jornada,local,visitante))
    return row.fetchall()

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
        for partido in jornada.find_all("tr"):
            #equipos print(partido.find("span",attrs={"class","nombre-equipo"}).get_text())
            local = partido.find("td",attrs={"class","col-equipo-local"}).find("span",attrs={"class","nombre-equipo"}).get_text()
            visitante = partido.find("td",attrs={"class","col-equipo-visitante"}).find("span",attrs={"class","nombre-equipo"}).get_text()
            resultado = partido.find("td",attrs={"class","col-resultado"}).find("a").get_text().split()
            golesLocales = resultado[0]
            golesVisitantes = resultado[2]
            link = partido.find("td",attrs={"class","col-resultado"}).find("a").get("href")
            #print(local,int(golesLocales),"-",int(golesVisitantes),visitante,link)
            jornadas.append([i,local,visitante,int(golesLocales),int(golesVisitantes),link])
        i+=1
    return jornadas

def lecturaWebGoles(jornada,local,visitante):
    raiz = "https://resultados.as.com"
    path = selectDataBaseGoles(jornada, local, visitante)[0][0]
    link = raiz + path
    file = str(jornada)+"-"+local+"vs"+visitante
    open_url(link,file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    goles = []
    for evento in soup.find_all("p",attrs={"class","txt-accion"}):
        accion = evento.find("span",attrs={"class","hidden-xs"}).get_text()
        if accion == "Gol":
            minuto = evento.find("span",attrs={"class","min-evento"}).get_text()
            jugador = evento.find("strong").get_text()
            goles.append([minuto,jugador])
    return goles
        
    #poner str(jornada) si desde tkinter no entra un string
    

"""
startDataBase()
insertDataBase(lecturaWeb())
#a
print(len(selectDataBaseJornadas()))
#b
print(selectDataBaseJornadas())
#a 2º ejer
print(selectDataBasePartidosPorJornada(3))"""

#ecturaWebGoles(1,"Sevilla","Espanyol")
def lecturaWebWhoosh():
    file="DiarioDeportivoWhoosh"
    open_url("http://resultados.as.com/resultados/futbol/primera/2017_2018/calendario/",file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    jornadas = []
    i = 1
    for jornada in soup.find_all("tbody"): #jornadas
        for partido in jornada.find_all("tr"):
            #equipos print(partido.find("span",attrs={"class","nombre-equipo"}).get_text())
            local = partido.find("td",attrs={"class","col-equipo-local"}).find("span",attrs={"class","nombre-equipo"}).get_text()
            visitante = partido.find("td",attrs={"class","col-equipo-visitante"}).find("span",attrs={"class","nombre-equipo"}).get_text()
            resultado = partido.find("td",attrs={"class","col-resultado"}).find("a").get_text().split()
            golesLocales = resultado[0]
            golesVisitantes = resultado[2]
            link = partido.find("td",attrs={"class","col-resultado"}).find("a").get("href")
            titulo,autor,fecha,cronica = lecturaPartidoJornada(i, local, visitante, link)
            jornadas.append([i,local,visitante,int(golesLocales),int(golesVisitantes),fecha,autor,titulo,cronica])
        i+=1
        print(jornadas)
        if i>=4:
            break
    return jornadas   
        
def lecturaPartidoJornada(jornada,local,visitante,path):
    raiz = "https://resultados.as.com"
    link = raiz + path
    file = str(jornada)+"-"+local+"vs"+visitante
    open_url(link,file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    titulo = soup.find("h2",attrs={"class","live-title"}).find("a").get_text()
    autor = soup.find("p",attrs={"class","ntc-autor s-inb"}).find("a").get_text()
    fecha = soup.find("span",attrs={"class","s-inb-sm"}).find("a").get_text()
    cronica = soup.find("div",attrs={"class","cont-cuerpo-noticia principal"}).find("div",attrs={"class","cf"}).find("p").get_text()
    return titulo,autor,fecha,cronica  
    
def crea_index(dirindex):
#     os.mkdir("Datos")
    if not os.path.exists(dirindex):
        os.mkdir(dirindex)
    ## ESTO SE QUITA SI SE HACE EL POP-UP
    if not len(os.listdir(dirindex)) == 0:
        sn = input("Indice no vacío. Desea reindexar? (s/n)")
    else:
        sn="s"
    if sn == "s":
        ix = create_in(dirindex,schema=get_schema())
        writer = ix.writer()
        for jornada in lecturaWebWhoosh():
            add_doc(writer,jornada) ## Método propio 
        writer.commit()
        

def get_schema():
    return Schema(numeroJornada=NUMERIC(stored=True),local=TEXT(stored=True),visitante=TEXT(stored=True),
                  golesLocales=NUMERIC,golesVisitantes=NUMERIC,fecha=DATETIME(stored=True),autor=TEXT,titulo=TEXT(stored=True),cronica=TEXT)

def add_doc(writer,jornada):
    writer.add_document(numeroJornada=jornada[0],local=jornada[1],visitante=jornada[2],
                                golesLocales=jornada[3],golesVisitantes=jornada[4],fecha=datetime.strptime(jornada[5],"%d/%m/%Y"),autor=jornada[6]
                                ,titulo=jornada[7],cronica=jornada[8])

def apartado_a(palabra):
    ix = open_dir("Index")
    query = palabra
    with ix.searcher() as searcher:
        parser = QueryParser("cronica",ix.schema)
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            print(r)
    
    
def apartado_b(equipo):
    ix = open_dir("Index")
    query = equipo
    with ix.searcher() as searcher:
        parser = QueryParser("local",ix.schema)
        query = query + " OR " + "visitante:" + query 
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            print(r)
            
def apartado_c():
    ix = open_dir("Index")
    date1 = "2017-08-21"
    date2 = "2017-08-22"
    ##date1 = datetime.strptime(date1,"%Y/%m/%d")
    ##date2 = datetime.strptime(date2,"%Y/%m/%d")
    with ix.searcher() as searcher:
        parser = QueryParser("fecha",ix.schema)
        ##parser.add_plugin(DateParserPlugin())
        query = "[" + date1 + " to " + date2 + "]"
        print(query)
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            print(r)
##lecturaWebWhoosh()
# [i,local,visitante,int(golesLocales),int(golesVisitantes),fecha,autor,titulo,cronica]
def apartado_d(equipo):
    ix = open_dir("Index")
    query = equipo
    with ix.searcher() as searcher:
        parser = QueryParser("local",ix.schema)
        query = query + " OR " + "visitante: " + query
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            print(r)

crea_index("Index")
apartado_d("Sevilla")




        