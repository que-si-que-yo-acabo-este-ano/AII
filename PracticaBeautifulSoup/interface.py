#!/usr/bin/python
#encoding:utf-8

from tkinter import *
from tkinter import messagebox


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
   
root = Tk()
menubar = Menu(root)
datamenu = Menu(menubar, tearoff=0)
datamenu.add_command(label="Cargar", command=donothing)
datamenu.add_command(label="Mostrar", command=donothing)
datamenu.add_separator()
datamenu.add_command(label="Salir", command=root.destroy)
menubar.add_cascade(label="Datos", menu=datamenu)


buscarmenu = Menu(menubar, tearoff=0)
buscarmenu.add_command(label="Tema", command=donothing)
buscarmenu.add_command(label="Autor", command=donothing)
menubar.add_cascade(label="Buscar", menu=buscarmenu)


statsmenu = Menu(menubar, tearoff=0)
statsmenu.add_command(label="Temas mas populares", command=donothing)
statsmenu.add_command(label="Temas mas populares", command=donothing)
menubar.add_cascade(label="Estadisticas", menu=statsmenu)

root.config(menu=menubar)
root.mainloop()

if __name__ == "__main__":
    ##aquí se llama al método principal
    print("método")