#!/usr/bin/python
# encoding:utf-8

import urllib.request, re
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from idlelib.iomenu import encoding
from test.test_importlib.namespace_pkgs.both_portions.foo.one import attr
from test.test_inspect import attrs_wo_objs
import os
from datetime import datetime
from whoosh.index import create_in,open_dir
from whoosh.fields import Schema, TEXT, DATETIME, ID, KEYWORD, STORED, NUMERIC
from whoosh.qparser import QueryParser,MultifieldParser
from whoosh import qparser
from whoosh.searching import Searcher
from whoosh.query import *
from whoosh.qparser.dateparse import DateParserPlugin



#### BeautifulSoup



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
    file="peliculas2"
    open_url("https://www.elseptimoarte.net/estrenos/",file)
    html_doc = open(file,"r")
    soup = beautifulRead(html_doc)
    head = "https://www.elseptimoarte.net"
    listaFinal = []
    lista = []
    for li in soup.find(attrs={"class":"elements"}).find_all("li"):
        pel = li.find('a',href=True).get("href")
        link = head + pel
        
        file2="peliculasAux"
        open_url(link,file2)
        html_doc = open(file2,"r")
        soup2 = beautifulRead(html_doc)
        
        titulo = ""
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Título"):
                    titulo = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
       
        titulo_original = ""
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Título original"):
                    titulo_original = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
                   
        fecha = ""
        director = ""   
       
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Director"):
                    director = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
        
        
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Estreno en España"):
                    fecha = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
            
        repart = ""
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Reparto"):
                    for actor in soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].find_all("a"):
                        repart = repart + ", " + actor.find(attrs={"itemprop":"name"}).get_text()
              
                acc = acc + 1

        reparto = repart.replace(",", "", 1).lstrip()
    
        sinopsis = ""
        acc=0
        for sip in soup2.find_all(attrs={"class":"highlight"}):
            if(acc==1):
                sinopsis = sip.find("div").get_text().strip()
                break
            acc = acc + 1
                
        lista = [titulo,titulo_original,fecha,director,reparto,sinopsis]
    
        listaFinal.append(lista)
        
    return listaFinal


###### Whoosh
numPeliculas = 0

def crea_index(dirindex):
#     os.mkdir("Datos")
    if not os.path.exists(dirindex):
        os.mkdir(dirindex)
    ## ESTO SE QUITA SI SE HACE EL POP-UP
    if not len(os.listdir(dirindex)) == 0:
        sn = input("Indice no vacio. Desea reindexar? (s/n)")
    else:
        sn="s"
    if sn == "s":
        ix = create_in(dirindex,schema=get_schema())
        writer = ix.writer()
        ##TODO a�adir scraping aqu�
        peliculas = lecturaWeb()
        global numPeliculas
        numPeliculas = len(peliculas)
        for pelicula in peliculas:
            add_doc(writer,pelicula) ## M�todo propio 

        writer.commit()
        
def get_schema():
    return Schema(titulo=TEXT(stored=True),tituloOriginal=TEXT(stored=True),fechaEstreno=DATETIME(stored=True),
                  director=TEXT(stored=True),reparto=TEXT,sinopsis=TEXT)

def add_doc(writer,pelicula):
    writer.add_document(titulo=pelicula[0],tituloOriginal=pelicula[1],fechaEstreno=pelicula[2],director=pelicula[3],reparto=pelicula[4],sinopsis=pelicula[5])


def apartado_a(palabras):
    ix = open_dir("Index")
    dataFromResults = []
    query = palabras
    with ix.searcher() as searcher:
        parser = MultifieldParser(["titulo","sinopsis"],ix.schema,group=qparser.OrGroup)
        query = parser.parse(query)
        print(query)
        results = searcher.search(query)
        for r in results:
            dataFromResults.append([r["titulo"],r["tituloOriginal"],r["director"]])
    return dataFromResults


def apartado_b(date1,date2):
    ix = open_dir("Index")
    dataFromResults = []
    with ix.searcher() as searcher:
        parser = QueryParser("fecha",ix.schema)
        parser.add_plugin(DateParserPlugin())
        query = u"date:[" + date1 + " to " + date2 + "]"
        print(query)
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            dataFromResults.append([r["titulo"],r["fecha"]])
    return dataFromResults

def apartado_c(palabra):
    ix = open_dir("Index")
    query = palabra + ","
    dataFromResults = []
    with ix.searcher() as searcher:
        parser = QueryParser("reparto",ix.schema)
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            dataFromResults.append([r["titulo"],r["tituloOriginal"],r["director"]])
    return dataFromResults





##### Tkinter



almacenado = False
root = Tk()

#### Main

def mainWindow():
    menubar = Menu(root)

    dataMenu = Menu(menubar, tearoff=0)
    dataMenu.add_command(label="Cargar", command=importFilms)
    dataMenu.add_separator()
    dataMenu.add_command(label="Salir", command=root.destroy)
    menubar.add_cascade(label="Datos", menu=dataMenu)

    searchMenu = Menu(menubar, tearoff=0)
    searchMenu.add_command(label="Título y Sinopsis", command=searchByTitleAndPlot)
    searchMenu.add_command(label="Fecha", command=searchByDate)
    searchMenu.add_command(label="Reparto", command=searchByCast)
    menubar.add_cascade(label="Buscar", menu=searchMenu)

    root.config(menu=menubar)
    root.mainloop()


def importFilms(): #TODO # Modificar con lo que tenga Jose para guardar los datos
    crea_index("Index")
    global almacenado
    almacenado = True
    countWin = Toplevel(root)
    numFilms = numPeliculas
    countLabel = Label(countWin, text="Hay " + str(numFilms) + " estrenos.")
    countLabel.grid(row=0)


def importAndClose(win):
    importFilms()
    win.destroy()


def showFilmsByTitleAndPlot(title,win):  #TODO #Modificar
    searchFilmsByTitleWin = Toplevel(root)
    win.destroy()
    filmsByTitleScroll = Scrollbar(searchFilmsByTitleWin, orient="vertical")
    filmsByTitleScroll.pack(side=RIGHT, fill=Y)
    filmsByTitleSearched = Listbox(searchFilmsByTitleWin, yscrollcommand=filmsByTitleScroll.set)

    filmsByTitleSelect = apartado_a(title) #Aquí cambiar por la nueva función de búsqueda

    filmsByTitleList = []
    for s in filmsByTitleSelect:
        filmsByTitleList.append(s[0] + " - " + s[1] + " - " + s[2]) ### Modificar de acuerdo a la estructura del string
    for l in filmsByTitleList:
        filmsByTitleSearched.insert(END, l)
    filmsByTitleSearched.pack(fill=BOTH)
    filmsByTitleScroll.config(command=filmsByTitleSearched.yview)


def searchByTitleAndPlot(): # En teoría debería ir así, puede que haga falta un casteo a String en el get()
    searchTitleWin = Toplevel(root)

    if almacenado:
        searchTitleLabel = Label(searchTitleWin, text="Introduzca su búsqueda:")
        searchTitleLabel.grid(row=0, columnspan=2)
        searchTitleEntry = Entry(searchTitleWin)
        searchTitleEntry.grid(row=1, columnspan=2)
        searchTitleButton = Button(searchTitleWin, text="Buscar", command=lambda: showFilmsByTitleAndPlot(searchTitleEntry.get(),searchTitleWin))
        searchTitleButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(searchTitleWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchTitleWin, text="Almacenar estrenos", command=lambda: importAndClose(searchTitleWin))
        alertButton.grid(row=1)


def getFilmsByDate(datesRange,win):
    getByDateWin = Toplevel(root)
    win.destroy()
    filmsByDateScroll = Scrollbar(getByDateWin, orient="vertical")
    filmsByDateScroll.pack(side=RIGHT, fill=Y)
    filmsByDateSearched = Listbox(getByDateWin, yscrollcommand=filmsByDateScroll.set)

    filmsByDateSelect = apartado_b(datesRange[0],datesRange[1]) #Aquí cambiar por la nueva función de búsqueda

    filmsByDateList = []
    for s in filmsByDateSelect:
        filmsByDateList.append(s[0] + " - " + s[1]) ### Modificar de acuerdo a la estructura del string
    for l in filmsByDateList:
        filmsByDateSearched.insert(END, l)
    filmsByDateSearched.pack(fill=BOTH)
    filmsByDateScroll.config(command=filmsByDateSearched.yview)
    


def searchByDate():
    searchDateWin = Toplevel(root)

    if almacenado:
        searchDateLabel = Label(searchDateWin, text="Introduzca un rango de fechas a buscar:")
        searchDateLabel.grid(row=0, columnspan=2)

        searchDateEntry1 = Entry(searchDateWin, width=2)
        searchDateEntry1.grid(row=1, column=0)
        separador1 = Label(searchDateWin, text="-")
        separador1.grid(row=1, column=1)
        searchDateEntry2 = Entry(searchDateWin, width=2)
        searchDateEntry2.grid(row=1, column=2)

        datesRange = [searchDateEntry1.get(),searchDateEntry2.get()]

        searchDateButton = Button(searchDateWin, text="Buscar", command=lambda: getFilmsByDate(datesRange,searchDateWin))
        searchDateButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(searchDateWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchDateWin, text="Almacenar estrenos", command=lambda: importAndClose(searchDateWin))
        alertButton.grid(row=1)


def getFilmsByCast(name,win):
    getByCastWin = Toplevel(root)
    win.destroy()
    filmsByCastScroll = Scrollbar(getByCastWin, orient="vertical")
    filmsByCastScroll.pack(side=RIGHT, fill=Y)
    filmsByCastSearched = Listbox(getByCastWin, yscrollcommand=filmsByCastScroll.set)

    filmsByCastSelect = apartado_c(name) #Aquí cambiar por la nueva función de búsqueda

    filmsByCastList = []
    for s in filmsByCastSelect:
        filmsByCastList.append(s[0] + " - " + s[1] + " - " + s[2]) ### Modificar de acuerdo a la estructura del string
    for l in filmsByCastList:
        filmsByCastSearched.insert(END, l)
    filmsByCastSearched.pack(fill=BOTH)
    filmsByCastScroll.config(command=filmsByCastSearched.yview)




def searchByCast():
    searchCastWin = Toplevel(root)

    if almacenado:
        searchCastLabel = Label(searchCastWin, text="Introduzca un nombre a buscar:")
        searchCastLabel.grid(row=0, columnspan=2)
        searchCastEntry1 = Entry(searchCastWin, width=2)
        searchCastEntry1.grid(row=1, column=0)
        searchCastButton = Button(searchCastWin, text="Buscar", command=lambda: getFilmsByCast(searchCastEntry1.get(),searchCastWin))
        searchCastButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(searchCastWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchCastWin, text="Almacenar estrenos", command=lambda: importAndClose(searchCastWin))
        alertButton.grid(row=1)


    
if __name__ == "__main__":
    mainWindow()

