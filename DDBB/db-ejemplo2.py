import sqlite3

conn=sqlite3.connect("GestionProductos")

micursor=conn.cursor()



conn.commit()


conn.close()

"""
micursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')
variosProductos=[
    ("Banano", 1, "Frutas"),
    ("Leche", 2, "Lacteos"),
    ("Queso", 3, "Lacteos")
]
micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",variosProductos)

variosProductos=micursor.fetchall()

for producto in variosProductos:
    print("Nombre Articulo: ", producto[0]," Seccion: ", producto[2])
"""
