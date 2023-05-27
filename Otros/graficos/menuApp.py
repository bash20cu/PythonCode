from tkinter import *
from tkinter import messagebox, filedialog

root=Tk()

def infoAdicional():
    messagebox.showinfo("Acerca de", "Procesador de miguel \n Version 0.1")
def avisoLicencia():
    messagebox.showwarning("Licencia", "Licencia GPL 3")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿ Deseas salir de la Aplicacion ?")
    valor=messagebox.askokcancel("Salir", "¿ Deseas salir de la Aplicacion ?")
    if valor==True:
        root.destroy()
def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "Imposible cerrar, intente de Nuevo")

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="/home/")


barraMenu=Menu(root)
root.config(menu=barraMenu, width=640, height=480)


#-------Barra menu -----
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()
