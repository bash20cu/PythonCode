import sqlite3
from tkinter import *
from tkinter import messagebox
from modulos.func import limpiarCampos


def CrearMvc(miID, nombre, apellidos, password, direccion, cuadroTexto):
    DatosUsuarios = [
        nombre.get(),
        password.get(),
        apellidos.get(),
        direccion.get(),
        cuadroTexto.get("1.0", END)
    ]
    conn = sqlite3.connect("Usuarios")
    micursor = conn.cursor()
    try:
        micursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", DatosUsuarios)
        conn.commit()
        limpiarCampos(miID, nombre, apellidos, password, direccion, cuadroTexto)
        messagebox.showinfo("Informacion", "Registro insertado con exito en la Base de datos")
    except:
        messagebox.showwarning("Aviso", "Algo salio mal")


def LeerMvc(miID, nombre, apellidos, password, direccion, cuadroTexto):
    cuadroTexto.delete("1.0", END)
    DatosUsuarios = [miID.get()]
    conn = sqlite3.connect("Usuarios")
    micursor = conn.cursor()

    try:
        micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=?", DatosUsuarios)
        elUsuario = micursor.fetchall()
        for usuario in elUsuario:
            miID.set(usuario[0])
            nombre.set(usuario[1])
            password.set(usuario[2])
            apellidos.set(usuario[3])
            direccion.set(usuario[4])
            cuadroTexto.insert(1.0, usuario[5])
        conn.commit()
    except:
        messagebox.showwarning("Aviso", "Algo salio mal")


def ActualizarMvc(miID, nombre, apellidos, password, direccion, cuadroTexto):
    DatosUsuarios = [
        nombre.get(),
        password.get(),
        apellidos.get(),
        direccion.get(),
        cuadroTexto.get("1.0", END),
        miID.get()
    ]
    conn = sqlite3.connect("Usuarios")
    micursor = conn.cursor()
    try:
        micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=?", DatosUsuarios)
        conn.commit()
        messagebox.showinfo("Informacion", "Registro Actualizado con exito en la Base de datos")
    except:
        messagebox.showwarning("Aviso", "Algo salio mal")

def EliminarMvc(miID, nombre, apellidos, password, direccion, cuadroTexto):
    DatosUsuarios = [miID.get()]
    conn = sqlite3.connect("Usuarios")
    micursor = conn.cursor()
    valor = messagebox.askokcancel("Borrar", "¡ Se Sorrara el Registro Seleccionado !")
    if valor == True:
        try:
            micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=?", DatosUsuarios)
            conn.commit()
            messagebox.showinfo("Informacion", "Registro Eliminado con exito en la Base de datos")
            limpiarCampos(miID, nombre, apellidos, password, direccion, cuadroTexto)
        except:
            messagebox.showwarning("Alerta", "Algo salio mal")


'''

        #try:
    micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=?", DatosUsuarios)
    conn.commit()
    messagebox.showinfo("Informacion", "Registro Actualizado con exito en la Base de datos")
        #except:
            #messagebox.showwarning("Aviso", "Algo salio mal")

'''


'''
        try:
        
        limpiarCampos(miID, nombre, apellidos, password, direccion, cuadroTexto)
        messagebox.showinfo("Informacion", "Regristro insertado con exito en la Base de datos")
    except:
        messagebox.showwarning("Aviso", "Algo salio mal")

    '''



''' 
micursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'" + nombre1 +
                         "','" + password1 + "','" + apellidos1 + "','" + direccion1 + "','" + comentarios + "' )")
'''
