from tkinter import *
from tkinter import messagebox



def infoAdicional():
    messagebox.showinfo("Acerca de", "Gestor de BBDD \n Version 0.1")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Licencia GPL 3")

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "Imposible cerrar, intente de Nuevo")
