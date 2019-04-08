#encoding:utf-8

import urllib.request, re
import os.path
from bs4 import BeautifulSoup
from test.test_inspect import attrs_wo_objs
from datetime import datetime

def abrir_url(url,file):
    try:
        urllib.request.urlretrieve(url,file)
        return file
    except:
        print  ("Error al conectarse a la pagina")
        return None

def leerPagina(file_ulr):
    html_doc = open(file_ulr,"r")
    pagina = BeautifulSoup(html_doc, 'html.parser')
    return pagina

def lecturaWeb():
    fichero1="foros1"
    file_ulr = abrir_url("https://foros.derecho.com/foro/20-Derecho-Civil-General",fichero1)
    soup1 = leerPagina(file_ulr)
    
    fichero2="foros2"
    file_ulr = abrir_url("https://foros.derecho.com/foro/20-Derecho-Civil-General/page2",fichero2)
    soup2 = leerPagina(file_ulr)
    
    fichero3="foros3"
    file_ulr = abrir_url("https://foros.derecho.com/foro/20-Derecho-Civil-General/page3",fichero3)
    soup3 = leerPagina(file_ulr)
    
    res1 = procesar(soup1)
    res2 = procesar(soup2)
    res3 = procesar(soup3)
    
    res = res1 + res2 + res3
    
    return res

def procesar(soup):    
    head = "https://foros.derecho.com/"
    listaFinal =[]


    for n in soup.find_all("li",attrs={"class":"threadbit"}):
        
        titulo =  n.find(attrs={"class":"threadinfo"}).find(attrs={"class":"threadtitle"}).find("a").get_text()
        href = n.find(attrs={"class":"threadinfo"}).find(attrs={"class":"threadtitle"}).find("a").get("href")     
        autor = n.find(attrs={"class":"threadinfo"}).find(attrs={"class":"author"}).find("a").get_text()        
        fecha = n.find(attrs={"class":"threadinfo"}).find(attrs={"class":"author"}).find("span").get_text().strip()[-16:-6]
        hora =  n.find(attrs={"class":"threadinfo"}).find(attrs={"class":"author"}).find("span").get_text().strip()[-5:]
        
        link = head + href        
        fechaHora = fecha + "-" + hora
        
        ac = 0
        respuestas = None
        visitas = None
        calificacion = None
        
        for m in n.find(attrs={"class":"threadstats td alt"}).find_all("li"):
            ac = ac + 1
            if ac==1:
                respuestas = m.get_text()[12:]
            elif ac==2:
                visitas = m.get_text()[9:]
            elif ac ==3:
                calificacion = m.get_text()[12:14].strip()
            else:
                ac = 0
                break
                
        lista = [titulo,link,autor,fechaHora,respuestas,visitas,calificacion]
        listaFinal.append(lista)        
    return(listaFinal)

print(lecturaWeb())