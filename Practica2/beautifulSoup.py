#encoding:utf-8

import dataBase
import urllib.request, re
from bs4 import BeautifulSoup
from idlelib.iomenu import encoding


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
    file="singluten"
    open_url("https://www.ulabox.com/campaign/productos-sin-gluten#gref",file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    listaFinal = []
    for li in soup.find_all("div",attrs={"class": "grid__item m-one-whole t-one-third d-one-third dw-one-quarter | js-product-grid-grid"}):
        #print(li)
        url = li.find(attrs={"class": "product-item__main"}).find(attrs={"class": "product-item__image nauru js-pjax js-article-link"}).get("href")
        marca = li.find(attrs={"class": "product-item__main"}).find(attrs={"class": "product-item__title"}).find(attrs="product-item__brand micro | push-half--bottom").get_text().lstrip()
        marca = marca.rstrip(' ')
        marca = marca.rstrip("\n")  
        nombre = li.find(attrs={"class": "product-item__main"}).find(attrs={"class": "product-item__title"}).find(attrs="product-item__name zeta face-normal | flush--bottom").find("a").get_text().lstrip()
        nombre = nombre.rstrip(' ')
        nombre = nombre.rstrip("\n")
        # print(marca)
        
        precio = li.find(attrs={"class": "delta"}).get_text()
        precio2 = li.find(attrs={"class": "milli"}).get_text()
        precioFinal = (precio + precio2[:-2]).replace(",",".")
        precioFinal = float(precioFinal)
#         print(precio)
#         print(precio2)
        lista=[]
        oferta = li.find(attrs={"class": "product-item__price product-item__price--old product-grid-footer__price--old nano | flush--bottom"})
        if(oferta!=None):
            oferta = str(oferta).replace("<del class=\"product-item__price product-item__price--old product-grid-footer__price--old nano | flush--bottom\">","")[:-8]   
            lista.append(marca)
            lista.append(nombre)
            lista.append(url)
            lista.append(oferta)
            lista.append(precioFinal)
        else:
            lista.append(marca)
            lista.append(nombre)
            lista.append(url)
            lista.append(precioFinal)
            lista.append(None)
            
        listaFinal.append(lista)
    return listaFinal

# for x in lecturaWeb():
#     print(x)
# print(lecturaWeb())
        
    #dataBase.startDataBase()
        
        
       
        