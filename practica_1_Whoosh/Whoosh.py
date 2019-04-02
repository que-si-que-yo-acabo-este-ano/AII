from whoosh.index import create_in
from whoosh.fields import *
#from test.test_readline import readline
from whoosh.qparser import QueryParser
from re import search
import os.path
from idlelib.iomenu import encoding
from datetime import datetime
from _io import open
import copy
from numpy.core.defchararray import strip
from asyncore import read

def insertWhoosh():
    schema = Schema(emailRem=TEXT(stored=True),emailDst=KEYWORD(stored=True),
                    fecha=DATETIME(stored=True),asunto=TEXT(stored=True),
                    cuerpo=TEXT(stored=True))
    
    if not os.path.exists("index"):
        os.mkdir("index")
    ix = create_in("index", schema)
    
    writer = ix.writer()
    
    ficheros = os.listdir("datos/Correos/")
    for f in ficheros:
        with open("datos/Correos/"+f,"r",encoding="utf-8") as file:
            
            remitente = file.readline().strip()
            destino = file.readline().strip()
            dia = file.readline().strip()
            dia = datetime.strptime(dia,"%Y%m%d")
            tema = file.readline().strip()
            texto = file.read()
    #        res.append(("".join(file.readlines()))) 
            
            file.close()
        
            writer.add_document(emailRem=remitente,emailDst=destino,
                    fecha=dia,asunto=tema,
                    cuerpo=texto)
    writer.commit()
    
    return ix

#     with ix.searcher() as searcher:
#         query = QueryParser("cuerpo", ix.schema).parse("contrato")
#         results = searcher.search(query)
#         print(results[0])


def readAgenda():
    with open("datos/Agenda/agenda.txt","r",encoding="utf-8") as file:
        dic = {}
        email=file.readline()
        while email:
            nombre=file.readline()
            dic[email.strip()]=nombre.strip()
            email=file.readline()
    
        return dic

 
def apartado_a(palabra):
    
    ix = insertWhoosh()
    
    with ix.searcher() as searcher:
        query = QueryParser("cuerpo", ix.schema).parse(palabra)
        results = searcher.search(query)
        agenda = readAgenda()
        
        for res in results:
            print(agenda[res["emailRem"]] + "\n" + res["fecha"].strftime("%d-%m-%Y"))
            print("----------------------------")
            
            
        
    return results

# apartado_a("contrato")


def apartado_b(palabra):
    
    ix = insertWhoosh()
    
    with ix.searcher() as searcher:
        query = QueryParser("asunto", ix.schema).parse(palabra)
        results = searcher.search(query)
        agenda = readAgenda()
        
        for res in results:
            print(agenda[res["emailRem"]] + "\n" + res["fecha"].strftime("%d-%m-%Y"))
            print("----------------------------")
            
            
        
    return results

# apartado_b("Contrato cuerpo:realizado cuerpo:importe") esto es un &&
