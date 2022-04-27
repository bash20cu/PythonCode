from tkinter import *
root=Tk()


frame1=Frame(root, width=500, height=400)
frame1.pack()

label1=Label(frame1, text="Digame su Nombre").place(x=0, y=50)
cuadroTexto=Entry(frame1)
cuadroTexto.place(x=150, y=50)


root.mainloop()
