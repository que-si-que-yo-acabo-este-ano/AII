#!/usr/bin/python
#encoding:utf-8

import urllib.request
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import sqlite3
import os


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
datamenu.add_command(label="Salir", command=root.quit)
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

##############################################################################################

def abrir_url(url,file):
    try:
        if os.path.exists(file):
            recarga = input("La página ya ha sido cargada. Desea recargarla (s/n)?")
            if recarga == "s":
                urllib.request.urlretrieve(url,file)
        else:
            urllib.request.urlretrieve(url,file)
        return file
    except:
        print  ("Error al conectarse a la página")
        return None


def extraer_datos():
    fichero="forum"
    if abrir_url("https://foros.derecho.com/foro/20-Derecho-Civil-General",fichero):
        f = open (fichero)
        soup = BeautifulSoup(f, 'html.parser')
        l = 
        f.close()
        return l


def almacenar_bd():
    conn = sqlite3.connect('test.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    conn.execute("DROP TABLE IF EXISTS FORUM")   
    conn.execute('''CREATE TABLE FORUM
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       TITLE        TEXT       NOT NULL,
       LINK         TEXT       NOT NULL,
       AUTHOR       TEXT       NOT NULL,
       DATE         TEXT       NOT NULL,
       ANSWERS      INTEGER    NOT NULL,
       VISITS       INTEGER    NOT NULL);''')

    l = extraer_datos()
    for i in l: # Cambiar los indices de i en la linea de abajo por los correspondientes al hacer el extraer_datos
        conn.execute("""INSERT INTO FORUM (TITLE, LINK, DATE, ANSWERS, VISITS) VALUES (?,?,?,?,?)""",(i[0],i[0],i[3],i[3],i[3]))
    conn.commit()
    cursor = conn.execute("SELECT COUNT(*) FROM FORUM")
    messagebox.showinfo( "Base Datos", "Base de datos creada correctamente \nHay " + str(cursor.fetchone()[0]) + " registros")
    conn.close()
