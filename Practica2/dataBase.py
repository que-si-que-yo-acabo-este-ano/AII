#encoding:utf-8
import sqlite3

def startDataBase():
    conn = sqlite3.connect('ulalox.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    # conn.execute("DROP TABLE IF EXISTS FORUM")   
    conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCTO
       (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
       MARCA          TEXT       NOT NULL,
       NOMBRE         TEXT       NOT NULL,
       LINK           TEXT       NOT NULL,
       PRECIO         DOUBLE     NOT NULL,
       PRECIO_OFERTA  DOUBLE);''')
    

def insertDataBase(productos):
    conn = sqlite3.connect('ulalox.db')
    for producto in productos:
        conn.execute("""INSERT INTO PRODUCTO (MARCA,NOMBRE,LINK,PRECIO,PRECIO_OFERTA) VALUES (?,?,?,?,?)""",(producto[0],producto[1],producto[2],producto[3],producto[4]))
    conn.commit()
    conn.close()    

def selectDataBaseMarcas():
    conn = sqlite3.connect('ulalox.db')
    rows = conn.execute("""SELECT MARCA FROM PRODUCTO""")
    res = []
    for producto in rows.fetchall():
        res.append(producto[0])
    conn.close()
    return set(res)


def selectDataBaseMarca(marca):
    conn = sqlite3.connect('ulalox.db')
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
    conn = sqlite3.connect('ulalox.db')
    rows = conn.execute("""SELECT NOMBRE,PRECIO,PRECIO_OFERTA FROM PRODUCTO WHERE PRECIO_OFERTA is not null""")
    res = []
    for producto in rows.fetchall():
        res.append(producto)
    conn.close()
    return res

"""productosPrueba = [['Gluton','Artg','www.gluten.com',2.0,None],['Gluton22323','OFERTON','www.gluten.com',2.0,1.0]]
startDataBase()
insertDataBase(productosPrueba)
print(selectDataBaseMarca("Gluton22323"))"""
