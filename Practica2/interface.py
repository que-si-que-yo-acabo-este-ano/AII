#!/usr/bin/python
#encoding:utf-8

from tkinter import *
from tkinter import messagebox
import dataBase
import beautifulSoup

almacenado = False

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def importProducts():
   dataBase.startDataBase()
   dataBase.insertDataBase(beautifulSoup.lecturaWeb())
   global almacenado
   almacenado = True



def getBrands():
   brands = dataBase.selectDataBaseMarcas()
   return brands



def selectProductsFromBrand(win):
   productsWin = Toplevel(root)
   prodScroll = Scrollbar(productsWin, orient="vertical")
   prodScroll.pack(side=RIGHT, fill=Y)

   products = Listbox(productsWin, yscrollcommand=prodScroll.set)
   # Hacer select de los productos de una marca
   blev = dataBase.selectDataBaseMarca("Blevit")
   aux = []
   for x in blev:
      aux.append(str(x[0]) + " " + str(x[1]))
   for y in aux:
      products.insert(END, y)
   products.pack()
   prodScroll.config(command=products.yview)
   win.destroy()



def importAndClose(win):
   dataBase.startDataBase()
   dataBase.insertDataBase(beautifulSoup.lecturaWeb())
   global almacenado
   almacenado = True
   win.destroy()



def selectBrand():
   brandWin = Toplevel(root)
   if almacenado:
      brandsSpin = Spinbox(brandWin,values=getBrands, wrap=True)
      brandsSpin.grid(row=0)
      brandsButton = Button(brandWin, text="Elegir marca", command= lambda : selectProductsFromBrand(brandWin))
      brandsButton.grid(row=1)

   else:
      alertLabel = Label(brandWin, text="No se han almacenado productos todavia")
      alertLabel.grid(row=0)
      alertButton = Button(brandWin, text="Almacenar productos", command= lambda : importAndClose(brandWin))
      alertButton.grid(row=1)




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

almacenar = Button(root, text ="Almacenar Productos", command = importProducts)
almacenar.grid(row=0, column=0, columnspan=2, sticky=E+W, pady=5)

marca = Button(root, text ="Mostrar Marca", command = selectBrand)
marca.grid(row=1, column=0, sticky=E+W, pady=5)

ofertas = Button(root, text ="Buscar Ofertas", command = selectProductsOnSale)
ofertas.grid(row=2, column=0, columnspan=2, sticky=E+W, pady=5)



root.config(menu=menubar)
root.mainloop()