#encoding:utf-8

import urllib.request, re
import os
from bs4 import BeautifulSoup
from datetime import datetime
from whoosh.index import create_in,open_dir
from whoosh.fields import Schema, TEXT, DATETIME, ID, KEYWORD, STORED, NUMERIC
from whoosh.qparser import QueryParser,MultifieldParser
from whoosh import qparser
from whoosh.searching import Searcher
from whoosh.query import *
from whoosh.qparser.dateparse import DateParserPlugin
<<<<<<< HEAD
=======
# from whoosh.qparser.default import MultifieldParser
>>>>>>> master

def crea_index(dirindex):
#     os.mkdir("Datos")
    if not os.path.exists(dirindex):
        os.mkdir(dirindex)
    ## ESTO SE QUITA SI SE HACE EL POP-UP
    if not len(os.listdir(dirindex)) == 0:
        sn = input("Indice no vacio. Desea reindexar? (s/n)")
    else:
        sn="s"
    if sn == "s":
        ix = create_in(dirindex,schema=get_schema())
        writer = ix.writer()
        ##TODO a�adir scraping aqu�
        ##for jornada in lecturaWebWhoosh():
        ##    add_doc(writer,jornada) ## M�todo propio 
        writer.commit()
        
def get_schema():
    return Schema(titulo=TEXT(stored=True),tituloOriginal=TEXT(stored=True),fechaEstreno=DATETIME(stored=True),
                  director=TEXT(stored=True),reparto=TEXT,sinopsis=TEXT)

def add_doc(writer,pelicula):
    writer.add_document(titulo=pelicula[0],tituloOriginal=pelicula[1],fechaEstreno=pelicula[2],director=pelicula[3],reparto=pelicula[4],sinopsis=pelicula[5])

<<<<<<< HEAD

def apartado_a(palabras):
    ix = open_dir("Index")
    queryContent = []
    for palabra in palabras:
        queryContent.append(Term(""))
    query = palabras
    with ix.searcher() as searcher:
        parser = MultifieldParser(["titulo","sinopsis"],ix.schema,group=qparser.OrGroup)
        query = parser.parse(query)
        print(query)
        results = searcher.search(query)
        for r in results:
            print(r)


=======
#Terminar
# def apartado_a(palabras):
#     ix = open_dir("Index")
#     queryContent = []
#     for palabra in palabras:
#         queryContent.append(Term(""))
#     query = palabras
#     with ix.searcher() as searcher:
#         parser = MultifieldParser(["titulo","sinopsis"],ix.schema,group=qparser.OrGroup)
#         query = parser.parse(query)
#         print(query)
#         results = searcher.search(query)
#         for r in results:
#             print(r)
# crea_index()
# apartado_a()
>>>>>>> master
def apartado_mentira(equipo):
    ix = open_dir("Index")
    query = equipo
    with ix.searcher() as searcher:
        parser = QueryParser("local",ix.schema)
        query = query + " OR " + "visitante:" + query
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            print(r)

#Falta probarlo
def apartado_b(date1,date2):
    ix = open_dir("Index")
    ##date1 = datetime.strptime(date1,"%Y/%m/%d")
    ##date2 = datetime.strptime(date2,"%Y/%m/%d")
    dataFromResults = []
    with ix.searcher() as searcher:
        parser = QueryParser("fecha",ix.schema)
        parser.add_plugin(DateParserPlugin())
        query = u"date:[" + date1 + " to " + date2 + "]"
        print(query)
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            dataFromResults.append([r["titulo"],r["fecha"]])
    return dataFromResults

def apartado_c(palabra):
    ix = open_dir("Index")
    query = palabra+","
    dataFromResults = []
    with ix.searcher() as searcher:
        parser = QueryParser("reparto",ix.schema)
        query = parser.parse(query)
        results = searcher.search(query)
        for r in results:
            dataFromResults.append([r["titulo"],r["tituloOriginal"],r["director"]])
    return dataFromResults
