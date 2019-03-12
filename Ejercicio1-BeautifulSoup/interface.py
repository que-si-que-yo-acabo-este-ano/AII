#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox

root = Tk()
almacenado = False

def mainWindow():
    menubar = Menu(root)

    almacenar = Button(root, text="Almacenar Resultados", command=importResults)
    almacenar.grid(row=0, column=0, columnspan=2, sticky=E + W, pady=5)

    jornada = Button(root, text="Listar Jornadas", command=listMatches)
    jornada.grid(row=1, column=0, sticky=E + W, pady=5)

    buscarJornada = Button(root, text="Buscar Jornada", command=searchMatches)
    buscarJornada.grid(row=2, column=0, columnspan=2, sticky=E + W, pady=5)

    buscarGoles = Button(root, text="Buscar Goles", command=searchGoals)
    buscarGoles.grid(row=3, column=0, columnspan=2, sticky=E + W, pady=5)


    root.config(menu=menubar)
    root.mainloop()



def importResults():
    ## Funcion de almacenado
    global almacenado
    almacenado = True
    resultsWin = Toplevel(root)
    numReg = 0 # Select count del numero de registros en la BD
    resultsLabel = Label(resultsWin, text="Hay " + numReg +" registros.")
    resultsLabel.grid(row=0)


def importAndClose(win):
    importResults()
    win.destroy()



def listMatches():
    matchesWin = Toplevel(root)
    
    if almacenado:
        matchesWin.geometry("400x150")
        matchScroll = Scrollbar(matchesWin, orient="vertical")
        matchScroll.pack(side=RIGHT, fill=Y)
        matches = Listbox(matchesWin, yscrollcommand=matchScroll.set)
        matchSelect = []# Select partidos 
        matchList = []
        for s in matchSelect:
            matchList.append(s[0] + ". - Precio: " + str(s[1]) + " - Oferta: " + str(s[2])) # Modificar acorde a la estructura de lo almacenado
        for l  in matchList:
            matches.insert(END, l)
        matches.pack(fill=BOTH)
        matchScroll.config(command=matches.yview)

    else:
        alertLabel = Label(matchesWin, text="No se han almacenado partidos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(matchesWin, text="Almacenar partidos", command=lambda: importAndClose(matchesWin))
        alertButton.grid(row=1)


def searchMatches(day):
    searchMatchWin = Toplevel(root)
    
    if almacenado:
        searchMatchWin.geometry("400x150")
        searchMatcScroll = Scrollbar(searchMatchWin, orient="vertical")
        searchMatcScroll.pack(side=RIGHT, fill=Y)
        matchesSearched = Listbox(searchMatchWin, yscrollcommand=searchMatcScroll.set)
        matchSearchSelect = []# Select partidos de la jornada en concreto (variable "day")
        matchSearchList = []
        for s in matchSearchSelect:
            matchSearchList.append(s[0] + ". - Precio: " + str(s[1]) + " - Oferta: " + str(s[2])) # Modificar acorde a la estructura de lo almacenado
        for l  in matchSearchList:
            matchesSearched.insert(END, l)
        matchesSearched.pack(fill=BOTH)
        searchMatcScroll.config(command=matchesSearched.yview)

    else:
        alertLabel = Label(searchMatchWin, text="No se han almacenado partidos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(searchMatchWin, text="Almacenar partidos", command=lambda: importAndClose(searchMatchWin))
        alertButton.grid(row=1)


def searchGoals():
    pass


