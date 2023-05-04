from tkinter import *
from modulos.func import *
from modulos.conn import *
from modulos.crud import *
#import tkinter.scrolledtext as scrolledtext
#from mvc_App.modulos import *


#-------Funciones ----------
def salirAplicacion():
    valor = messagebox.askokcancel("Salir", "¿ Deseas salir de la Aplicacion ?")
    if valor == True:
        root.destroy()

root = Tk()
root.title("Base de Datos GUI")

barraMenu = Menu(root)
root.config(menu=barraMenu, width=640, height=480)


#-------Barra menu ----------------------------------
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Crear DB", command=CrearDB)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=lambda: CrearMvc(nombre, apellidos, password, direccion, cuadroTexto))
crudMenu.add_command(label="Leer", command=lambda: LeerMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))
crudMenu.add_command(label="Actualizar", command=lambda: ActualizarMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))
crudMenu.add_command(label="Borrar", command=lambda: EliminarMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)


barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#----- Frame Campos  -------------------------
frameCampos=Frame(root)
frameCampos.pack()

miID = StringVar()
nombre = StringVar()
apellidos = StringVar()
password = StringVar()
direccion = StringVar()
#comentarios=StringVar()

labelID = Label(frameCampos, text="ID: ").grid(row=0, column=0, sticky="w", padx=10, pady=10)
cuadroID = Entry(frameCampos, textvariable=miID) #state='disable'
cuadroID.grid(row=0, column=1, padx=10, pady=10, sticky="w")

labelNombre = Label(frameCampos, text="Nombre: ").grid(row=1, column=0, sticky="w", padx=10, pady=10)
cuadroNombre = Entry(frameCampos, textvariable=nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10, sticky="w")
cuadroNombre.config(fg="red", justify="right")

labelPass = Label(frameCampos, text="Password: ").grid(row=2, column=0, sticky="w", padx=10, pady=10)
cuadroPass = Entry(frameCampos, textvariable=password)
cuadroPass.grid(row=2, column=1, padx=10, pady=10, sticky="w")
cuadroPass.config(show="*")

labelApellidos = Label(frameCampos, text="Apellidos: ").grid(row=3, column=0, sticky="w", padx=10, pady=10)
cuadroApellidos = Entry(frameCampos, width=30, textvariable=apellidos)
cuadroApellidos.grid(row=3, column=1, padx=10, pady=10, sticky="w")

labelDireccion = Label(frameCampos, text="Direccion: ").grid(row=4, column=0, sticky="w", padx=10, pady=10)
cuadroDireccion = Entry(frameCampos, width=30, textvariable=direccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10, sticky="w")

labelComentarios = Label(frameCampos, text="Comentarios").grid(row=5, column=0, sticky="w", padx=10, pady=10)
cuadroTexto = Text(frameCampos, width=25, height=10)
cuadroTexto.grid(row=5, column=1, sticky="w", padx=10, pady=10)
scrollVert = Scrollbar(frameCampos, command=cuadroTexto.yview)
scrollVert.grid(row=5, column=1, sticky="e")
cuadroTexto.config(yscrollcommand=scrollVert.set)



#--------------Frame Botones --------------------
frameBotones = Frame(root)
frameBotones.pack()
botonCrear = Button(frameBotones, text="Crear", command=lambda: CrearMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)
botonLeer = Button(frameBotones, text="Leer", command=lambda: LeerMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)
botonActualizar = Button(frameBotones, text="Actualizar", command=lambda: ActualizarMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)
botonBorrar = Button(frameBotones, text="Borrar", command=lambda: EliminarMvc(miID, nombre, apellidos, password, direccion, cuadroTexto))
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
