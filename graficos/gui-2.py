from tkinter import *
raiz=Tk()
raiz.title("Nueva Ventana")
#raiz.resizable(0,0)
raiz.geometry("640x480")
raiz.config(bg="blue")

#Creando un Frame
frame1=Frame()
frame1.pack()
frame1.config(bg="red")
frame1.config(width="600",height="400")
frame1.config(relief="sunken")
frame1.config(cursor="hand2")

raiz.mainloop()
