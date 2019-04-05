#encoding:utf-8
import urllib.request, re
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding


def open_url(url,file):
    try:
        urllib.request.urlretrieve(url,file)
        return file
    except:
        print  ("Error al conectarse a la pagina")
        return None
    
def beautifulRead(html):
    return BeautifulSoup(html,"html.parser")


def lecturaWeb():
    file="noticias"
    open_url("https://www.meneame.net/",file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    head = "https://www.meneame.net/"
    listaFinal = []
    
    for div in soup.find_all(attrs={"class":"news-summary"}):
        
        link = div.find(attrs={"class":"center-content"}).find('a').get("href")
        titulo = div.find(attrs={"class":"center-content"}).find('a').get_text().strip()
        fuente_noticia = div.find(attrs={"class":"news-submitted"}).find(attrs={'class': "showmytitle"}).get_text()
        autor = div.find(attrs={"class":"news-submitted"}).find('a',attrs={'class': None}).get_text()
        fechaHora = None
        for fecha in div.find(attrs={"class":"news-submitted"}).find_all(attrs={'class':"ts visible"}):
            comprueba = fecha.get("title")
            if("publicado" in comprueba):
                fechaHora = fecha
                break
        # la fecha no sale! 
        contenido = div.find(attrs={"class":"news-content"}).get_text().strip()
        
        lista =[link,autor,fuente_noticia,link,fechaHora,contenido]
        listaFinal.append(lista)
#         print(link)
#         print(titulo)
#         print(fuente_noticia)
#         print(autor)
#         print(fechaHora)
#         print(contenido)
#         print("------------")
    
    return listaFinal

print(lecturaWeb())