from tkinter import *
from tkinter import messagebox



def infoAdicional():
    messagebox.showinfo("Acerca de", "Gestor BBDD \n Version 0.1")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Licencia GPL 3")

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "Imposible cerrar, intente de Nuevo")


def limpiarCampos(miID, nombre, apellidos, password, direccion, cuadroTexto):
    miID.set("")
    nombre.set("")
    apellidos.set("")
    password.set("")
    direccion.set("")
    cuadroTexto.delete("1.0", END)

'''

def limpiarCampos(miID, nombre, apellidos, password, direccion, cuadroTexto): # mover la funcion a MVC
    miID.set("")
    nombre.set("")
    apellidos.set("")
    password.set("")
    direccion.set("")
    cuadroTexto.delete("1.0", END)


def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿ Deseas salir de la Aplicacion ?")
    valor=messagebox.askokcancel("Salir", "¿ Deseas salir de la Aplicacion ?")
    if valor==True:
        root.destroy()
'''
