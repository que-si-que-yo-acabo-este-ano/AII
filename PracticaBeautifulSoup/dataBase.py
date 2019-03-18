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

def selectDataBaseMarcas():
    conn = sqlite3.connect('cine.db')
    ##rows = conn.execute("""SELECT MARCA FROM PRODUCTO""")
    ##res = []
    ##for producto in rows.fetchall():
    ##    res.append(producto[0])
    rows = conn.execute("""SELECT * FROM GENEROS""")
    print(rows.fetchone())
    conn.close()
    
    
def selectDataBaseMarca(marca):
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""
    SELECT NOMBRE,
        CASE PRECIO_OFERTA
            WHEN PRECIO_OFERTA is not NULL 
                THEN 
                    PRECIO_OFERTA 
            ELSE 
                    PRECIO 
        END PRECIO_FINAL 
    FROM 
        PRODUCTO
    WHERE
        MARCA = '{0}'""".format(marca))
    res = []
    for producto in rows.fetchall():
        print(producto) ##### print
        res.append(producto)
    conn.close()
    return res
    
def selectDataBaseOfertas():
    conn = sqlite3.connect('cine.db')
    rows = conn.execute("""SELECT NOMBRE,PRECIO,PRECIO_OFERTA FROM PRODUCTO WHERE PRECIO_OFERTA is not null""")
    res = []
    for producto in rows.fetchall():
        res.append(producto)
    conn.close()
    return res

startDataBase()
pelicula1 = ["p1","p1_vo","españita",'22/07/2019',"DIR1",["MIEDO","INTRIGA"]]
insertPeliculas([pelicula1])