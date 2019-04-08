#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup


## ------------------------- Interfaz ---------------------------

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

    # menubar.add_command(label="Películas por género", command=filmsByGenre)

    root.config(menu=menubar)
    root.mainloop()


def importFilms(): #TODO # Modificar con lo que tenga Jose para guardar los datos
    startDataBase()
    insertPeliculas(lecturaWeb())
    global almacenado
    almacenado = True
    countWin = Toplevel(root)
    numFilms = selectCount()
    countLabel = Label(countWin, text="Hay " + str(numFilms) + " estrenos.")
    countLabel.grid(row=0)


def importAndClose(win):
    importFilms()
    win.destroy()


# def filmsByGenre():
#     genreWin = Toplevel(root)

#     if almacenado:
#         genreLabel = Label(genreWin, text="Seleccione un género")
#         genreLabel.grid(row=0, columnspan=2)
#         genreSpin = Spinbox(genreWin, values=selectTiposGeneros(),wrap=True)
#         genreSpin.grid(row=1, columnspan=2)
#         genreButton = Button(genreWin, text="Buscar", command=lambda: filmsByGenreListed(genreSpin.get(),genreWin))
#         genreButton.grid(row=2, columnspan=2)

#     else:
#         alertLabel = Label(genreWin, text="No se han almacenado estrenos todavia")
#         alertLabel.grid(row=0)
#         alertButton = Button(genreWin, text="Almacenar estrenos", command=lambda: importAndClose(genreWin))
#         alertButton.grid(row=1)


# def filmsByGenreListed(genre,win):
#     genreListWin = Toplevel(root)
#     win.destroy()
#     filmsByGenreScroll = Scrollbar(genreListWin, orient="vertical")
#     filmsByGenreScroll.pack(side=RIGHT, fill=Y)
#     filmsByGenreSearched = Listbox(genreListWin, yscrollcommand=filmsByGenreScroll.set)
#     filmsByGenreSelect = selectPeliculaPorGenero(genre)
#     filmsByGenreList = []
#     for s in filmsByGenreSelect:
#         filmsByGenreList.append(s[0] + " "+ s[1]) ### Modificar de acuerdo a la estructura del string
#     for l in filmsByGenreList:
#         filmsByGenreSearched.insert(END, l)
#     filmsByGenreSearched.pack(fill=BOTH)
#     filmsByGenreScroll.config(command=filmsByGenreSearched.yview)


def showFilmsByTitleAndPlot(title,win):  #TODO #Modificar
    searchFilmsByTitleWin = Toplevel(root)
    win.destroy()
    filmsByTitleScroll = Scrollbar(searchFilmsByTitleWin, orient="vertical")
    filmsByTitleScroll.pack(side=RIGHT, fill=Y)
    filmsByTitleSearched = Listbox(searchFilmsByTitleWin, yscrollcommand=filmsByTitleScroll.set)
    titleListed = title.split()

    filmsByTitleSelect = selectPorTitulo(titleListed) #Aquí cambiar por la nueva función de búsqueda

    filmsByTitleList = []
    for s in filmsByTitleSelect:
        filmsByTitleList.append(s[0] + " " + s[1] + " " + s[2]) ### Modificar de acuerdo a la estructura del string
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

    filmsByDateSelect = selectPorDate(datesRange) #Aquí cambiar por la nueva función de búsqueda

    filmsByDateList = []
    for s in filmsByDateSelect:
        filmsByDateList.append(s[0] + " " + s[1] + " " + s[2]) ### Modificar de acuerdo a la estructura del string
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

    filmsByCastSelect = selectPorCast(name) #Aquí cambiar por la nueva función de búsqueda

    filmsByCastList = []
    for s in filmsByCastSelect:
        filmsByCastList.append(s[0] + " " + s[1] + " " + s[2]) ### Modificar de acuerdo a la estructura del string
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


