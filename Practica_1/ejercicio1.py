#encoding:utf-8

import urllib.request, re
import os.path
from bs4 import BeautifulSoup

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

def leerPagina(file_ulr):
    html_doc = open(file_ulr,"r")
    pagina = BeautifulSoup(html_doc, 'html.parser')
    return pagina

if __name__ == "__main__":
    fichero="foros"
    file_ulr = abrir_url("https://foros.derecho.com/foro/20-Derecho-Civil-General",fichero)
    soup = leerPagina(file_ulr)
    for n in soup.find_all("li",attrs={"class":"threadbit"}):
        for m in n.find(attrs={"class":"threadstats td alt"}).find_all("li"):
            print(m.get_text())
        print("--------------------------------")
    