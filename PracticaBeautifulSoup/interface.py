#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime
import urllib.request, re
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding
from test.test_importlib.namespace_pkgs.both_portions.foo.one import attr

### Borrar donothing ###########

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
################################

## -------------------- Relativo a la base de datos --------------
def startDataBase():
    conn = sqlite3.connect('cine.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    
    conn.execute("DROP TABLE IF EXISTS PELICULAS") 
    conn.execute("DROP TABLE IF EXISTS GENEROS") 
    
    conn.execute('''CREATE TABLE IF NOT EXISTS GENEROS
        (GENERO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        GENERO            TEXT NOT NULL,
        PELICULA_ID        INTEGER NOT NULL,
        CONSTRAINT FK_PELICULA
            FOREIGN KEY (PELICULA_ID)
            REFERENCES PELICULAS(PELICULA_ID) 
        );''')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS PELICULAS
        (PELICULA_ID INTEGER PRIMARY KEY  AUTOINCREMENT,
        TITULO              TEXT       NOT NULL,
        TITULO_ORIGINAL     TEXT       NOT NULL,
        PAIS                TEXT       NOT NULL,
        FECHA_ESTRENO       DATE     NOT NULL,
        DIRECTOR            TEXT       NOT NULL
        );''')
    
    
    conn.close()
    

def insertPeliculas(peliculas):
    conn = sqlite3.connect('cine.db')
    for i,pelicula in enumerate(peliculas,1):
        pelicula[3] = pelicula[3].replace("/","-")
        pelicula[3] = datetime.strptime(pelicula[3], '%d-%m-%Y')
        #print(pelicula[3].strftime('%d-%m-%Y'))
        
        conn.execute("""INSERT INTO PELICULAS 
            (TITULO,TITULO_ORIGINAL,PAIS,FECHA_ESTRENO,DIRECTOR) VALUES (?,?,?,?,?)""",(pelicula[0],pelicula[1],pelicula[2],pelicula[3],pelicula[4]))
        
        for genero in pelicula[5]:
            conn.execute("""INSERT INTO GENEROS (GENERO,PELICULA_ID) VALUES (?,?)""",(genero,i))
    
    conn.commit()
    conn.close()

def selectCount():
    conn = sqlite3.connect('cine.db')
    num = conn.execute("""SELECT COUNT(*) FROM PELICULAS""")
    return num.fetchone()[0]

def selectTiposGeneros():
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT GENERO FROM GENEROS""")
    res = []
    for genero in rows.fetchall():
        res.append(genero[0])
    conn.close()
    return list(set(res))
    
def selectPeliculaPorGenero(genero):
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT TITULO,strftime('%d-%m-%Y',FECHA_ESTRENO) FROM PELICULAS WHERE PELICULA_ID IN (SELECT PELICULA_ID FROM GENEROS WHERE GENERO=(?))""",(genero,))
    res = []
    for pelicula in rows.fetchall():
        res.append(pelicula)
    conn.close()
    return res


## --------------------------------------------------------------

## ------------------ Relativo a BeautifulSoap ------------------
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
    file="peliculas"
    open_url("https://www.elseptimoarte.net/estrenos/",file)
    html_doc = open(file,"r")
    soup = beautifulRead(html_doc)
    head = "https://www.elseptimoarte.net"
    listaFinal = []
    for li in soup.find(attrs={"class":"elements"}).find_all("li"):
        pel = li.find('a',href=True).get("href")
        link = head + pel
        
        file2="peliculasAux"
        open_url(link,file2)
        html_doc = open(file2,"r")
        soup2 = beautifulRead(html_doc)
        
        titulo = soup2.find(attrs={"class":"highlight"}).find_all("dd")[0].get_text().lstrip()
        titulo_original = soup2.find(attrs={"class":"highlight"}).find_all("dd")[1].get_text().lstrip()
        pais = soup2.find(attrs={"class":"highlight"}).find_all("dd")[2].get_text().lstrip().strip()
        if "," in pais:
            paises = pais.split(",")
            pais= ""
            for p in range(len(paises)):
                pais = pais + ", " + paises[p].lstrip()   
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
                
        
#         if "España" in pais:
#             fecha = soup2.find(attrs={"class":"highlight"}).find_all("dd")[3].get_text().lstrip().lstrip() 
#         else:
#             fecha = soup2.find(attrs={"class":"highlight"}).find_all("dd")[4].get_text().lstrip().lstrip()
            
        generos = []
        for gen in soup2.find(attrs={"class":"categorias"}).find_all('a'):
            generos.append(gen.get_text().lstrip())
        lista = [titulo,titulo_original,pais,fecha,director,generos]
        listaFinal.append(lista)
        
    return listaFinal






## --------------------------------------------------------------



## ------------------------- Interfaz ---------------------------

almacenado = True ### Cambiar a False cuando pueda importar
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
    searchMenu.add_command(label="Título", command=donothing)
    searchMenu.add_command(label="Fecha", command=donothing)
    menubar.add_cascade(label="Buscar", menu=searchMenu)

    menubar.add_command(label="Películas por género", command=filmsByGenre)

    root.config(menu=menubar)
    root.mainloop()


def importFilms():
    startDataBase()
    insertPeliculas(lecturaWeb()) ## Hay que pasarle la lectura
    global almacenado
    almacenado = True
    countWin = Toplevel(root)
    numFilms = selectCount()
    countLabel = Label(countWin, text="Hay " + str(numFilms) + " estrenos.")
    countLabel.grid(row=0)


def importAndClose(win):
    importFilms()
    win.destroy()


def filmsByGenre():
    genreWin = Toplevel(root)

    if almacenado:
        genreLabel = Label(genreWin, text="Seleccione un género")
        genreLabel.grid(row=0, columnspan=2)
        genreSpin = Spinbox(genreWin, values=selectTiposGeneros(),wrap=True)
        genreSpin.grid(row=1, columnspan=2)
        genreButton = Button(genreWin, text="Buscar", command=lambda: filmsByGenreListed(genreSpin.get(),genreWin))
        genreButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(genreWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(genreWin, text="Almacenar estrenos", command=lambda: importAndClose(genreWin))
        alertButton.grid(row=1)


def filmsByGenreListed(genre,win):
    genreListWin = Toplevel(root)
    win.destroy()
    filmsByGenreScroll = Scrollbar(genreListWin, orient="vertical")
    filmsByGenreScroll.pack(side=RIGHT, fill=Y)
    filmsByGenreSearched = Listbox(genreListWin, yscrollcommand=filmsByGenreScroll.set)
    filmsByGenreSelect = selectPeliculaPorGenero(genre)
    filmsByGenreList = []
    for s in filmsByGenreSelect:
        filmsByGenreList.append("Pelicula de género A") ### Modificar de acuerdo a la estructura del string
    for l in filmsByGenreList:
        filmsByGenreSearched.insert(END, l)
    filmsByGenreSearched.pack(fill=BOTH)
    filmsByGenreScroll.config(command=filmsByGenreSearched.yview)


def showFilmsByTitle(title,win):
    searchFilmsByTitleWin = Toplevel(root)
    win.destroy()
    filmsByTitleScroll = Scrollbar(searchFilmsByTitleWin, orient="vertical")
    filmsByTitleScroll.pack(side=RIGHT, fill=Y)
    filmsByTitleSearched = Listbox(searchFilmsByTitleWin, yscrollcommand=filmsByTitleScroll.set)
    filmsByTitleSelect = searchFilmsByTitle(title)
    filmsByTitleList = []
    for s in filmsByTitleSelect:
        filmsByTitleList.append("Pelicula de género A") ### Modificar de acuerdo a la estructura del string
    for l in filmsByTitleList:
        filmsByTitleSearched.insert(END, l)
    filmsByTitleSearched.pack(fill=BOTH)
    filmsByTitleScroll.config(command=filmsByTitleSearched.yview)


def searchByTitle():
    searchTitleWin = Toplevel(root)

    if almacenado:
        searchTitleLabel = Label(searchTitleWin, text="Introduzca una palabra a buscar:")
        searchTitleLabel.grid(row=0, columnspan=2)
        searchTitleEntry = Entry(searchTitleWin)
        searchTitleEntry.grid(row=1, columnspan=2)
        searchTitleButton = Button(searchTitleWin, text="Buscar", command=lambda: showFilmsByTitle(searchTitleEntry.get(),searchTitleWin))
        searchTitleButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(searchTitleWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchTitleWin, text="Almacenar estrenos", command=lambda: importAndClose(searchTitleWin))
        alertButton.grid(row=1)


def searchByDate():
    searchDateWin = Toplevel(root)

    if almacenado:
        searchDateLabel = Label(searchDateWin, text="Introduzca una fecha a buscar:")
        searchDateLabel.grid(row=0, columnspan=2)

        searchDateEntry1 = Entry(searchDateWin, width=2)
        searchDateEntry1.grid(row=1, column=0)
        separador1 = Label(searchDateWin, text="-")
        separador1.grid(row=1, column=1)
        searchDateEntry2 = Entry(searchDateWin, width=2)
        searchDateEntry2.grid(row=1, column=2)
        separador2 = Label(searchDateWin, text="-")
        separador2.grid(row=1, column=3)
        searchDateEntry3 = Entry(searchDateWin, width=4)
        searchDateEntry3.grid(row=1, column=4)

        date = searchDateEntry1.get() + "-" + searchDateEntry2.get() + "-" + searchDateEntry3.get()

        searchDateButton = Button(searchDateWin, text="Buscar", command=lambda: showFilmsByDate(searchTitleEntry.get(),searchTitleWin))
        searchDateButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(searchDateWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchDateWin, text="Almacenar estrenos", command=lambda: importAndClose(searchDateWin))
        alertButton.grid(row=1)

    
if __name__ == "__main__":
    mainWindow()




