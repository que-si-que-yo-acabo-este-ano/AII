#encoding:utf-8
import sqlite3
from datetime import datetime
def startDataBase():
    conn = sqlite3.connect('cine.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    
    conn.execute("DROP TABLE IF EXISTS PELICULAS") 
    conn.execute("DROP TABLE IF EXISTS GENEROS") 
    
    conn.execute('''CREATE TABLE IF NOT EXISTS GENEROS
        (GENERO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        GENERO            TEXT NOT NULL,
        PELICULA_ID        INTEGER NOT NULL,
        CONSTRAINT FK_PELICULA
            FOREIGN KEY (PELICULA_ID)
            REFERENCES PELICULAS(PELICULA_ID) 
        );''')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS PELICULAS
        (PELICULA_ID INTEGER PRIMARY KEY  AUTOINCREMENT,
        TITULO              TEXT       NOT NULL,
        TITULO_ORIGINAL     TEXT       NOT NULL,
        PAIS                TEXT       NOT NULL,
        FECHA_ESTRENO       DATE     NOT NULL,
        DIRECTOR            TEXT       NOT NULL
        );''')
    
    
    conn.close()
    

def insertPeliculas(peliculas):
    conn = sqlite3.connect('cine.db')
    for i,pelicula in enumerate(peliculas,1):
        pelicula[3] = pelicula[3].replace("/","-")
        pelicula[3] = datetime.strptime(pelicula[3], '%d-%m-%Y')
        #print(pelicula[3].strftime('%d-%m-%Y'))
        
        conn.execute("""INSERT INTO PELICULAS 
            (TITULO,TITULO_ORIGINAL,PAIS,FECHA_ESTRENO,DIRECTOR) VALUES (?,?,?,?,?)""",(pelicula[0],pelicula[1],pelicula[2],pelicula[3],pelicula[4]))
        
        for genero in pelicula[5]:
            conn.execute("""INSERT INTO GENEROS (GENERO,PELICULA_ID) VALUES (?,?)""",(genero,i))
    
    conn.commit()
    conn.close()

def selectCount():
    conn = sqlite3.connect('cine.db')
    num = conn.execute("""SELECT COUNT(*) FROM PELICULAS""")
    return num.fetchone()[0]

def selectTiposGeneros():
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT GENERO FROM GENEROS""")
    res = []
    for genero in rows.fetchall():
        res.append(genero[0])
    conn.close()
    return set(res)
    
def selectPeliculaPorGenero(genero):
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT TITULO,strftime('%d-%m-%Y',FECHA_ESTRENO) FROM PELICULAS WHERE PELICULA_ID IN (SELECT PELICULA_ID FROM GENEROS WHERE GENERO=(?))""",(genero,))
    res = []
    for pelicula in rows.fetchall():
        res.append(pelicula)
    conn.close()
    return res

def selectPorTitulo(titulo):
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT TITULO,PAIS,DIRECTOR FROM PELICULAS WHERE TITULO LIKE '%{0}%'""".format(titulo))
    res = []
    for pelicula in rows.fetchall():
        res.append(pelicula)
    conn.close()
    return res
    
def selectPorFecha(fecha):
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT TITULO,PAIS,DIRECTOR FROM PELICULAS WHERE TITULO LIKE '%{0}%'""".format(fecha))
    res = []
    for pelicula in rows.fetchall():
        res.append(pelicula)
    conn.close()
    return res

startDataBase()
pelicula1 = ["p1 p2","p1_vo","españita",'22/07/2019',"DIR1",["MIEDO","INTRIGA"]]
insertPeliculas([pelicula1])
print(selectCount())
print(selectTiposGeneros())
print(selectPeliculaPorGenero("MIEDO"))
print(selectPorTitulo("p1"))