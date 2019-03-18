#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

import beautifulSoup

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


## --------------------------------------------------------------

## ------------------ Relativo a BeautifulSoap ------------------





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
    insertPeliculas(beautifulSoup.lecturaWeb()) ## Hay que pasarle la lectura
    global almacenado
    almacenado = True
    countWin = Toplevel(root)
    numFilms = selectCount()
    countLabel = Label(countWin, text="Hay " + str(numFilms) + " estrenos.")
    countLabel.grid(row=0)


def importAndClose(win):
    importFilms()
    win.destroy()

    
def getGenres():
    genres = dataBase.selectDataBaseGenres()
    return genres


def searchFilmsByGenre(genre):
    films = dataBase.selectFilmByGenre(genre)
    return films



def filmsByGenre():
    genreWin = Toplevel(root)

    if almacenado:
        genreLabel = Label(genreWin, text="Seleccione un género")
        genreLabel.grid(row=0, columnspan=2)
        genreSpin = Spinbox(genreWin, values=getGenres(),wrap=True)
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
    filmsByGenreSelect = searchFilmsByGenre(genre)
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
        searchDateLabel = Label(searchDateWin, text="Introduzca una palabra a buscar:")
        searchDateLabel.grid(row=0, columnspan=2)
        searchDateEntry = Entry(searchDateWin)
        searchDateEntry.grid(row=1, columnspan=2)
        searchDateButton = Button(searchDateWin, text="Buscar", command=lambda: showFilmsByTitle(searchTitleEntry.get(),searchTitleWin))
        searchDateButton.grid(row=2, columnspan=2)

    else:
        alertLabel = Label(searchDateWin, text="No se han almacenado estrenos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchDateWin, text="Almacenar estrenos", command=lambda: importAndClose(searchDateWin))
        alertButton.grid(row=1)

    
if __name__ == "__main__":
    mainWindow()




