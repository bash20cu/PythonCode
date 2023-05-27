import sqlite3
from tkinter import messagebox

global cursor

def Conn():
    conn=sqlite3.connect("Usuarios")

def CrearDB():
    conn = sqlite3.connect("Usuarios")
    micursor = conn.cursor()
    try:
        micursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        conn.commit()
        messagebox.showinfo("Informacion", "Base de datos creada con exito")
    except:
        messagebox.showwarning("Alerta","Base datos ya creada")