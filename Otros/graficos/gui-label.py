from tkinter import *
root=Tk()

frame1=Frame(root, width=500, height=400)
frame1.pack()

label1=Label(frame1, text="Hola mundo").place(x=0, y=50)
#label1.place(x=0, y=50)

root.mainloop()
