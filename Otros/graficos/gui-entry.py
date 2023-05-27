from tkinter import *
root=Tk()


frame1=Frame(root, width=500, height=400)
frame1.pack()

labelNombre=Label(frame1, text="Teclee su Nombre").grid(row=0, column=0, sticky="w", padx=2)
cuadroNombre=Entry(frame1).grid(row=0, column=1, sticky="w")

labelApellido=Label(frame1, text="Teclee su Apellido").grid(row=1, column=0, sticky="w", padx=2)
cuadroApellido=Entry(frame1).grid(row=1, column=1, sticky="w")

labelDireccion=Label(frame1, text="Teclee su Direccion").grid(row=3, column=0, sticky="w", padx=2)
cuadroDireccion=Entry(frame1, width=25).grid(row=3, column=1, sticky="w")

labelPass=Label(frame1, text="Teclee su Password").grid(row=4, column=0, sticky="w", padx=2)
cuadroPass=Entry(frame1)
cuadroPass.grid(row=4, column=1, sticky="w")
cuadroPass.config(show="-")



root.mainloop()
