#!/usr/bin/python
# encoding:utf-8

from tkinter import *
from tkinter import messagebox
import dataBase
import beautifulSoup


def importProducts():
    dataBase.removeTable()
    dataBase.startDataBase()
    dataBase.insertDataBase(beautifulSoup.lecturaWeb())
    global almacenado
    almacenado = True


def getBrands():
    brands = dataBase.selectDataBaseMarcas()
    return brands


def selectProductsFromBrand(win,brand):
    productsWin = Toplevel(root)
    productsWin.geometry("300x150")
    prodScroll = Scrollbar(productsWin, orient="vertical")
    prodScroll.pack(side=RIGHT, fill=Y)

    products = Listbox(productsWin, yscrollcommand=prodScroll.set)
    blev = dataBase.selectDataBaseMarca(brand)
    aux = [] ## Hacer esta parte (esta línea y los dos bucles) más fácil de entender
    for x in blev:
        aux.append(str(x[0]) + ". - Precio: " + str(x[1]))
    for y in aux:
        products.insert(END, y)
    products.pack(fill=BOTH)
    prodScroll.config(command=products.yview)
    win.destroy()


def importAndClose(win):
    dataBase.removeTable()
    dataBase.startDataBase()
    dataBase.insertDataBase(beautifulSoup.lecturaWeb())
    global almacenado
    almacenado = True
    win.destroy()


def selectBrand():
    brandWin = Toplevel(root)
    if almacenado:
        brandsSpin = Spinbox(brandWin, values=getBrands(), wrap=True)
        brandsSpin.grid(row=0)
        brandsButton = Button(brandWin, text="Elegir marca", command=lambda: selectProductsFromBrand(brandWin,brandsSpin.get()))
        brandsButton.grid(row=1)

    else:
        alertLabel = Label(brandWin, text="No se han almacenado productos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(brandWin, text="Almacenar productos", command=lambda: importAndClose(brandWin))
        alertButton.grid(row=1)


def selectProductsOnSale():
    salesWin = Toplevel(root)
    
    if almacenado:
        salesWin.geometry("400x150")
        saleScroll = Scrollbar(salesWin, orient="vertical")
        saleScroll.pack(side=RIGHT, fill=Y)
        sales = Listbox(salesWin, yscrollcommand=saleScroll.set)
        salesSelect = dataBase.selectDataBaseOfertas()
        salesList = []
        for s in salesSelect:
            salesList.append(s[0] + ". - Precio: " + str(s[1]) + " - Oferta: " + str(s[2]))
        for l  in salesList:
            sales.insert(END, l)
        sales.pack(fill=BOTH)
        saleScroll.config(command=sales.yview)

    else:
        alertLabel = Label(salesWin, text="No se han almacenado productos todavia")
        alertLabel.grid(row=0)
        alertButton = Button(salesWin, text="Almacenar productos", command=lambda: importAndClose(salesWin))
        alertButton.grid(row=1)



almacenado = False

dataBase.removeTable()

root = Tk()
menubar = Menu(root)

almacenar = Button(root, text="Almacenar Productos", command=importProducts)
almacenar.grid(row=0, column=0, columnspan=2, sticky=E + W, pady=5)

marca = Button(root, text="Mostrar Marca", command=selectBrand)
marca.grid(row=1, column=0, sticky=E + W, pady=5)

ofertas = Button(root, text="Buscar Ofertas", command=selectProductsOnSale)
ofertas.grid(row=2, column=0, columnspan=2, sticky=E + W, pady=5)


root.config(menu=menubar)
root.mainloop()

    
if __name__ == "__main__":
    pass
