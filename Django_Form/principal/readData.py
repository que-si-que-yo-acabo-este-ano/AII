import os
from Django_Form.settings import STATIC_ROOT
from datetime import datetime

def readMovieFile(file):
    res = []
    with open(file) as File:
        rows = File.readlines()
        for row in rows:
#             if "item" in File:
            row = row.strip().split('|')
            del row[3]
            genres = row[4:]
            row = row[0:4]
            row.append(genres)
#             row = {"idPelicula":row[0],"titulo":row[1],"fechaDeEstreno":row[2]
#                    ,"imdbURL":row[3],"categorias":row[4]}
            res.append(row)
#             elif "user":
#                 row = row.split('|')
#                 row = {"idUsuario":row[0],"edad":row[1],"sexo":row[2],"ocupacion":row[3],"codigoPostal":row[4]}
#                 res.append(row)
    del res[266]
    return res

def readGenreFile(file):
    res = []
    with open(file) as File:
        rows = File.readlines()
        for row in rows:
            row = row.strip().split('|')
            res.append(row)
    return res[:-1]

def readUserFile(file):
    res = []
    with open(file) as File:
        rows = File.readlines()
        for row in rows:
            row = row.split('|')
#             row = {"idUsuario":row[0],"edad":row[1],"sexo":row[2],"ocupacion":row[3],"codigoPostal":row[4]}
            res.append(row)
    return res

def readRatingFile(file):
    res = []
    with open(file) as File:
        rows = File.readlines()
        for row in rows:
            row = row.split()
#             row = {"idUsuario":row[0],"idPelicula":row[1],"puntuacion":row[2],"fecha":row[3]}
            res.append(row)
    return res

def readOccupationFile(file):
    res = []
    with open(file) as File:
        rows = File.readlines()
        for row in rows:
            res.append(row.strip())
    return res
