#encoding:utf-8

from idlelib.iomenu import encoding
import urllib.request, re

from bs4 import BeautifulSoup
from whoosh.automata.fsa import find_all_matches


def open_url(url,file):
    try:
        urllib.request.urlretrieve(url,file)
        return file
    except:
        print  ("Error al conectarse a la página")
        return None
    
def beautifulRead(html):
    return BeautifulSoup(html,"html.parser")


def lecturaSpells():
    file = "listaSpells3"
    open_url("http://beta.hardcodex.ru/spells/get/all/_/_/_/front/_#",file)
    html_doc = open(file,"r",encoding="utf-8")
    soup = beautifulRead(html_doc)
    listaFinal = []
    

    i = 0
    for spell in soup.find(attrs={"class":"pages col-xs-12 col-sm-12 col-lg-9 pull-right"}).select('div[class*="card cardBlock"]'):
        listaHechizos = []
        nombre = spell.find(attrs = {"class":"name lined srname"})
        if(nombre!=None):
            name = nombre.get_text()
            if  not name in listaHechizos:
                i=i+1
                resultado = {
                    "name":[],
                    "level":[],
                    "school":[],
                    "castingTime":[],
                    "range":[],
                    "components":[],
                    "duration":[],
                    "text":[],
                    "class":[]
                    }
                
                resultado["name"] = name
                listaHechizos.append(name)
                
                j=0
                for ul in spell.find(attrs={"class":"body"}).find_all("ul"):
                    for li in ul.find_all("li"):
                        parameter = li.get_text()
                        if j==0 :
                            finalParameter= parameter[12:]
                            resultado["castingTime"] = finalParameter
                        elif j == 1:
                            finalParameter = parameter[5:]
                            resultado["range"] = finalParameter
                        elif j==2:
                            finalParameter = parameter[10:]
                            finalParameter=finalParameter.replace(", ","-")
                            resultado["components"] = finalParameter
                        elif j==3:
                            finalParameter = parameter[8:]
                            resultado["duration"] = finalParameter
                        
                        j=j+1
                clases = spell.find("b", attrs={"class":"class srclass"}).get_text().replace(" ","").split(",")
                resultado["class"] = clases
                
                nivelEscuela = spell.find("b", attrs={"class":"type srtype"}).get_text()
                nivelEscuela = re.findall(r"[1-9]|\bc[a-z]*|[A-Z][a-z]*", nivelEscuela)
                nivel=""
                escuela=""
                if("cantrip" in nivelEscuela):
                    nivel = "0"
                    escuela = nivelEscuela[0]
                else:
                    nivel = nivelEscuela[0]
                    escuela = nivelEscuela[1]
                
                resultado["level"] = nivel
                resultado["school"] = escuela
                
                for p in spell.find(attrs={"class":"body" }).find_all("p"):
                    resultado["text"] = p.get_text().strip()
                    
                listaFinal.append(resultado)
                    
    return listaFinal

spells = lecturaSpells()

for spell in lecturaSpells():
    print(spell["class"])
