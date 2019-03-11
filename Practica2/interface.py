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

almacenar = Button(root, text ="Almacenar Productos", command = donothing)
almacenar.grid(row=0, column=0, sticky=E+W, pady=5)
marca = Button(root, text ="Mostrar Marca", command = donothing)
marca.grid(row=1, column=0, sticky=E+W, pady=5)
ofertas = Button(root, text ="Buscar Ofertas", command = donothing)
ofertas.grid(row=2, column=0, sticky=E+W, pady=5)

root.config(menu=menubar)
root.mainloop()