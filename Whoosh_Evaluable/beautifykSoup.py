#encoding:utf-8

#import dataBase
import urllib.request, re
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding
from test.test_importlib.namespace_pkgs.both_portions.foo.one import attr
from test.test_inspect import attrs_wo_objs


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
    file="peliculas2"
    open_url("https://www.elseptimoarte.net/estrenos/",file)
    html_doc = open(file,"r")
    soup = beautifulRead(html_doc)
    head = "https://www.elseptimoarte.net"
    listaFinal = []
    lista = []
    for li in soup.find(attrs={"class":"elements"}).find_all("li"):
        pel = li.find('a',href=True).get("href")
        link = head + pel
        
        file2="peliculasAux"
        open_url(link,file2)
        html_doc = open(file2,"r")
        soup2 = beautifulRead(html_doc)
        
        titulo = ""
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Título"):
                    titulo = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
       
        titulo_original = ""
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Título original"):
                    titulo_original = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
                   
        fecha = ""
        director = ""   
       
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Director"):
                    director = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
        
        
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Estreno en España"):
                    fecha = soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].get_text().lstrip()
                acc = acc + 1
            
        repart = ""
        acc = 0
        for dt in soup2.find(attrs={"class":"highlight"}).find_all("dt"):
                if(dt.get_text() == "Reparto"):
                    for actor in soup2.find(attrs={"class":"highlight"}).find_all("dd")[acc].find_all("a"):
                        repart = repart + ", " + actor.find(attrs={"itemprop":"name"}).get_text()
              
                acc = acc + 1

        reparto = repart.replace(",", "", 1).lstrip()
    
        sinopsis = ""
        acc=0
        for sip in soup2.find_all(attrs={"class":"highlight"}):
            if(acc==1):
                sinopsis = sip.find("div").get_text().strip()
                break
            acc = acc + 1
                
        lista = [titulo,titulo_original,fecha,director,reparto,sinopsis]
    
        listaFinal.append(lista)
        
    return listaFinal


print(lecturaWeb())
        
    #dataBase.startDataBase()
        