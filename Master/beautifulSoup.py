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
    for li in soup.find_all("li",attrs={"class": "threadbit"}):
        print(li.find(attrs={"class": "title"}).get("title"))
        #aa ver si sale este comentario.
        for m in li.find(attrs={"class":"threadstats td alt"}).find_all("li"):
            print(m.get_text())
        print("--------------------------------------------------------------------")
       
        
        
        
       
        