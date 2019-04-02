#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox

root = Tk()
almacenado = False

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def mainWindow():
    menuBar = Menu(root)

    dataMenu = Menu(menuBar, tearoff=0)
    dataMenu.add_command(label="Cargar", command=load)
    dataMenu.add_separator()
    dataMenu.add_command(label="Salir", command=root.destroy)
    menuBar.add_cascade(label="Datos", menu=dataMenu)

    searchMenu = Menu(menuBar, tearoff=0)
    searchMenu.add_command(label="Noticia", command=searchNews)
    searchMenu.add_command(label="Equipo", command=searchTeam)
    searchMenu.add_command(label="Fecha", command=searchDate)
    menuBar.add_cascade(label="Buscar", menu=searchMenu)

    root.config(menu=menuBar)
    root.mainloop()


def load():
    global almacenado
    almacenado = True
    donothing()


def loadAndClose(win):
    load()
    win.destroy()



def searchNews():
    searchNewsWin = Toplevel(root)

    if almacenado:
        searchNewsLabel = Label(searchNewsWin, text="Introduzca su consulta sobre noticias:")
        searchNewsLabel.grid(row=0, columnspan=2)
        searchNewsEntry = Entry(searchNewsWin)
        searchNewsEntry.grid(row=1, column=0)
        searchNewsButton = Button(searchNewsWin, text="Buscar", command=lambda: findNews(searchNewsEntry.get(),searchNewsWin))
        searchNewsButton.grid(row=1, column=1)
    else:
        alertLabel = Label(searchNewsWin, text="No se han almacenado partidos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchNewsWin, text="Almacenar partidos", command=lambda: loadAndClose(searchNewsWin))
        alertButton.grid(row=1)


def findNews(consulta, win):
    findNewsWin = Toplevel(root)
    win.destroy()

    findNewsScroll = Scrollbar(findNewsWin, orient="vertical")
    findNewsScroll.pack(side=RIGHT, fill=Y)

    findNewsListbox = Listbox(findNewsWin, yscrollcommand=findNewsScroll.set)
    # Añadir los resultados a la listbox


def searchTeam():
    searchTeamWin = Toplevel(root)

    if almacenado:
        searchTeamLabel = Label(searchTeamWin, text="Introduzca su consulta sobre un equipo:")
        searchTeamLabel.grid(row=0, columnspan=2)
        searchTeamEntry = Entry(searchTeamWin)
        searchTeamEntry.grid(row=1, column=0)
        searchTeamButton = Button(searchTeamWin, text="Buscar", command=lambda: findTeam(searchTeamEntry.get(),searchTeamWin))
        searchTeamButton.grid(row=1, column=1)
    else:
        alertLabel = Label(searchTeamWin, text="No se han almacenado partidos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchTeamWin, text="Almacenar partidos", command=lambda: loadAndClose(searchTeamWin))
        alertButton.grid(row=1)


def findTeam(consulta, win):
    findTeamWin = Toplevel(root)
    win.destroy()

    findTeamScroll = Scrollbar(findTeamWin, orient="vertical")
    findTeamScroll.pack(side=RIGHT, fill=Y)

    findTeamListbox = Listbox(findTeamWin, yscrollcommand=findTeamScroll.set)
    # Añadir los resultados a la listbox


def searchDate():
    searchDateWin = Toplevel(root)

    if almacenado:
        searchDateLabel = Label(searchDateWin, text="Introduzca su consulta sobre un rango de fechas:")
        searchDateLabel.grid(row=0, columnspan=2)
        searchDateEntry = Entry(searchDateWin)
        searchDateEntry.grid(row=1, column=0)
        searchDateButton = Button(searchDateWin, text="Buscar", command=lambda: findDate(searchDateEntry.get(),searchDateWin))
        searchDateButton.grid(row=1, column=1)
    else:
        alertLabel = Label(searchDateWin, text="No se han almacenado partidos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchDateWin, text="Almacenar partidos", command=lambda: loadAndClose(searchDateWin))
        alertButton.grid(row=1)


def findDate(consulta, win):
    findDateWin = Toplevel(root)
    win.destroy()

    findDateScroll = Scrollbar(findDateWin, orient="vertical")
    findDateScroll.pack(side=RIGHT, fill=Y)

    findDateListbox = Listbox(findDateWin, yscrollcommand=findDateScroll.set)
    # Añadir los resultados a la listbox



if __name__ == "__main__":
    mainWindow()