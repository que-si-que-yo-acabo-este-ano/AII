#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox
import dataBase
import beautifulSoup

### Borrar donothing ###########

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
################################


almacenado = True ### Cambiar a False cuando pueda importar
root = Tk()

#### Main

def mainWindow():
    menubar = Menu(root)

    dataMenu = Menu(menubar, tearoff=0)
    dataMenu.add_command(label="Cargar", command=donothing)
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
    dataBase.startDataBase()
    dataBase.insertDataBase(beautifulSoup.lecturaWeb())
    global almacenado
    almacenado = True
    countWin = Toplevel(root)
    numFilms = beautifulSoup.selectDatabaseCount()
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




    
if __name__ == "__main__":
    mainWindow()




