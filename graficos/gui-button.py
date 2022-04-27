from tkinter import *
import tkinter.scrolledtext as scrolledtext
root=Tk()

nombre=StringVar()

def codigoBoton():
    nombre.set("Migue")

frame1=Frame(root, width=500, height=400)
frame1.pack()

labelNombre=Label(frame1, text="Nombre").grid(row=0, column=0, sticky="w", padx=2)
cuadroNombre=Entry(frame1, textvariable=nombre).grid(row=0, column=1, sticky="w")

labelComentarios=Label(frame1, text="Comentarios").grid(row=1, column=1, sticky="w", padx=2)
cuadroTexto=scrolledtext.ScrolledText(frame1, width=100, height=5).grid(row=2, column=1, sticky="w", padx=5, pady=5)

botonEnvio=Button(frame1, text="Enviar!", command=codigoBoton)
botonEnvio.grid(row=3, column=0, sticky="w", padx=2)



root.mainloop()
