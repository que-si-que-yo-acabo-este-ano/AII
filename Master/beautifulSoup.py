#encoding:utf-8

import urllib.request, re
import os.path
from bs4 import BeautifulSoup

def open_url(url,file):
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
    
def beautifulRead(html):
    return BeautifulSoup(html,"html.parser")


if __name__ == "__main__":
    file="foros"
    open_url("https://foros.derecho.com/foro/20-Derecho-Civil-General",file)
    html_doc = open(file,"r")
    soup = beautifulRead(html_doc)
    linkRaiz = str(soup.find("base").get("href"))
    for li in soup.find_all("li",attrs={"class": "threadbit"}):
        titulo = li.find(attrs={"class": "title"}).get("title")
        link = linkRaiz + str(li.find(attrs={"class": "title"}).get("href"))
        autor = li.find(attrs={"class": "username understate"}).get_text()
        fechaHora = li.find(attrs={"class":"label"}).get_text().split(",")
        respvis = []
        for m in li.find(attrs={"class":"threadstats td alt"}).find_all("li",limit=2):
            respvis.append(m.get_text()[-1])
        
        #TODO insertar en bd
        print("Título:",titulo)
        print("Link:",link)
        print("Autor:",autor)
        print("Fecha y Hora:",str(fechaHora[1]).lstrip())
        #Posición 0 respuestas
        print("Respuestas:",respvis[0])
        #Posición 1 visitas
        print("Visitas:",respvis[1])
        print("--------------------------------------------------------------------")
        
        
        
       
        