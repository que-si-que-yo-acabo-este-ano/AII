#!/usr/bin/python
#encoding:utf-8

from tkinter import *
from tkinter import messagebox


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()



def getBrands():
   # Un select de las marcas, meterlas en una lista
   brandsList = ["a","b","c"]
   return brandsList



def selectProductsFromBrand():
   productsWin = Toplevel(root)
   prodScroll = Scrollbar(productsWin, orient="vertical")
   prodScroll.pack(side=RIGHT, fill=Y)

   products = Listbox(productsWin, yscrollcommand=prodScroll.set)
   # Hacer select de los productos de una marca
   for x in range(20):
      products.insert(x,"Producto numero "+str(x))
   products.pack()
   prodScroll.config(command=products.yview)



def selectProductsOnSale():
   salesWin = Toplevel(root)
   saleScroll = Scrollbar(salesWin, orient="vertical")
   saleScroll.pack(side=RIGHT, fill=Y)

   sales = Listbox(salesWin, yscrollcommand=saleScroll.set)
   # Hacer select de los productos en oferta
   for x in range(20):
      sales.insert(x,"Oferta numero "+str(x))
   sales.pack()
   saleScroll.config(command=sales.yview)


   
root = Tk()
menubar = Menu(root)

almacenar = Button(root, text ="Almacenar Productos", command = donothing)
almacenar.grid(row=0, column=0, columnspan=2, sticky=E+W, pady=5)

marca = Button(root, text ="Mostrar Marca", command = selectProductsFromBrand)
marca.grid(row=1, column=0, sticky=E+W, pady=5)

ofertas = Button(root, text ="Buscar Ofertas", command = selectProductsOnSale)
ofertas.grid(row=2, column=0, columnspan=2, sticky=E+W, pady=5)

brandsSpin = Spinbox(root,values=getBrands(), wrap=True)
brandsSpin.grid(row=1, column=1)


root.config(menu=menubar)
root.mainloop()