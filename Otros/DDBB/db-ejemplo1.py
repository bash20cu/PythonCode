import sqlite3

conn=sqlite3.connect("base-ejemplo")

micursor=conn.cursor()

#micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#micursor.execute("INSERT INTO PRODUCTOS VALUES ('baloon', 15 , 'DEPORTES')")
"""
variosProductos=[
    ("Banano", 1, "Frutas"),
    ("Leche", 2, "Lacteos"),
    ("Queso", 3, "Lacteos")
]
micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)
"""
micursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=micursor.fetchall()
    #print(variosProductos)
for producto in variosProductos:
    print("Nombre Articulo: ", producto[0]," Seccion: ", producto[2])

conn.commit()


conn.close()
