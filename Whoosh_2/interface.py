#!/usr/bin/python
#encoding:utf-8

from tkinter import *
from tkinter import messagebox

root = Tk()
almacenado = False

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()



def mainWindow():
    menubar = Menu(root)

    datamenu = Menu(menubar, tearoff=0)
    datamenu.add_command(label="Cargar", command=load)
    datamenu.add_separator()
    datamenu.add_command(label="Salir", command=root.destroy)
    menubar.add_cascade(label="Datos", menu=datamenu)

    buscarmenu = Menu(menubar, tearoff=0)
    buscarmenu.add_command(label="Noticia", command=searchNews)
    buscarmenu.add_command(label="Fuente", command=searchSource)
    buscarmenu.add_command(label="Fecha", command=searchDate)
    menubar.add_cascade(label="Buscar", menu=buscarmenu)

    root.config(menu=menubar)
    root.mainloop()



def load():
    donothing()


def loadAndClose():
    donothing()


def searchNews():
    searchNewsWin = Toplevel(root)

    searchNewsLabel = Label(searchNewsWin, text="Introduzca su consulta sobre noticias:")
    searchNewsLabel.grid(row=0, columnspan=2)
    searchNewsEntry = Entry(searchNewsWin)
    searchNewsEntry.grid(row=1, column=0)
    searchNewsButton = Button(searchNewsWin, text="Buscar", command=lambda: findNews(searchNewsEntry.get(),searchNewsWin))
    searchNewsButton.grid(row=1, column=1)


def findNews(consulta, win):
    findNewsWin = Toplevel(root)
    win.destroy()

    findNewsScroll = Scrollbar(findNewsWin, orient="vertical")
    findNewsScroll.pack(side=RIGHT, fill=Y)

    findNewsListbox = Listbox(findNewsWin, yscrollcommand=findNewsScroll.set)
    # Añadir los resultados a la listbox



def searchSource():
    searchSourceWin = Toplevel(root)

    searchSourceLabel = Label(searchSourceWin, text="Introduzca su consulta sobre una fuente:")
    searchSourceLabel.grid(row=0, columnspan=2)
    searchSourceEntry = Entry(searchSourceWin)
    searchSourceEntry.grid(row=1, column=0)
    searchSourceButton = Button(searchSourceWin, text="Buscar", command=lambda: findSource(searchSourceEntry.get(),searchSourceWin))
    searchSourceButton.grid(row=1, column=1)


def findSource(consulta, win):
    findSourceWin = Toplevel(root)
    win.destroy()

    findSourceScroll = Scrollbar(findSourceWin, orient="vertical")
    findSourceScroll.pack(side=RIGHT, fill=Y)

    findSourceListbox = Listbox(findSourceWin, yscrollcommand=findSourceScroll.set)
    # Añadir los resultados a la listbox



def searchDate():
    searchDateWin = Toplevel(root)

    searchDateLabel = Label(searchDateWin, text="Introduzca su consulta sobre una fecha:")
    searchDateLabel.grid(row=0, columnspan=2)
    searchDateEntry = Entry(searchDateWin)
    searchDateEntry.grid(row=1, column=0)
    searchDateButton = Button(searchDateWin, text="Buscar", command=lambda: findSource(searchDateEntry.get(),searchDateWin))
    searchDateButton.grid(row=1, column=1)


def findDate(consulta, win):
    findDateWin = Toplevel(root)
    win.destroy()

    findDateScroll = Scrollbar(findDateWin, orient="vertical")
    findDateScroll.pack(side=RIGHT, fill=Y)

    findDateListbox = Listbox(findDateWin, yscrollcommand=findDateScroll.set)
    # Añadir los resultados a la listbox



    
if __name__ == "__main__":
    mainWindow()