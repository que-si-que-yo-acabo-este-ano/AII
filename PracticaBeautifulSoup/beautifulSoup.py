#encoding:utf-8

import dataBase
import urllib.request, re
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding
from test.test_importlib.namespace_pkgs.both_portions.foo.one import attr


def open_url(url,file):
    try:
        urllib.request.urlretrieve(url,file)
        return file
    except:
        print  ("Error al conectarse a la página")
        return None
    
def beautifulRead(html):
    return BeautifulSoup(html,"html.parser")


def lecturaWeb():
    file="peliculas"
    open_url("https://www.elseptimoarte.net/estrenos/",file)
    html_doc = open(file,"r")
    soup = beautifulRead(html_doc)
    head = "https://www.elseptimoarte.net"
    listaFinal = []
    for li in soup.find(attrs={"class":"elements"}).find_all("li"):
        pel = li.find('a',href=True).get("href")
        link = head + pel
        
        file2="peliculasAux"
        open_url(link,file2)
        html_doc = open(file2,"r")
        soup2 = beautifulRead(html_doc)
        
        titulo = soup2.find(attrs={"class":"highlight"}).find_all("dd")[0].get_text().lstrip()
        titulo_original = soup2.find(attrs={"class":"highlight"}).find_all("dd")[1].get_text().lstrip()
        pais = soup2.find(attrs={"class":"highlight"}).find_all("dd")[2].get_text().lstrip().strip()
        if "," in pais:
            paises = pais.split(",")
            pais= ""
            for p in range(len(paises)):
                pais = pais + ", " + paises[p].lstrip()   
        fecha = ""
        director = ""
        
        if "España" in pais:
            fecha = soup2.find(attrs={"class":"highlight"}).find_all("dd")[3].get_text().lstrip().lstrip()
            director = director = soup2.find(attrs={"class":"highlight"}).find_all("dd")[5].get_text().lstrip()
        else:
            fecha = soup2.find(attrs={"class":"highlight"}).find_all("dd")[4].get_text().lstrip().lstrip()
            director = director = soup2.find(attrs={"class":"highlight"}).find_all("dd")[8].get_text().lstrip()
        generos = []
        for gen in soup2.find(attrs={"class":"categorias"}).find_all('a'):
            generos.append(gen.get_text().lstrip())
        lista = [titulo,titulo_original,pais,fecha,director,generos]
        listaFinal.append(lista)
        
    return listaFinal


print(lecturaWeb())
        
    #dataBase.startDataBase()
        
        
       
        