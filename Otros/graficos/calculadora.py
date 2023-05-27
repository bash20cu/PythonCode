from tkinter import *

root=Tk()

frame1=Frame(root)
frame1.pack()

operacion=""
resultado=0
#--------Pantalla ----------
numeroPantalla=StringVar()
pantalla=Entry(frame1, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1,padx=10,pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#-------Pulsaciones Teclado----------------
def NumeroPulsado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#------funcion suma -------
def Suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeroPantalla.set(resultado)

#------funcion resultado --------
def ElResultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0
#-----Fila 1------
boton7=Button(frame1, text="7", width=3, command=lambda:NumeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(frame1, text="8", width=3, command=lambda:NumeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(frame1, text="9", width=3, command=lambda:NumeroPulsado("9"))
boton9.grid(row=2, column=3)
botonMulti=Button(frame1, text="*", width=3)
botonMulti.grid(row=2, column=4)

#-----Fila 2------
boton4=Button(frame1, text="4", width=3, command=lambda:NumeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(frame1, text="5", width=3, command=lambda:NumeroPulsado("4"))
boton5.grid(row=3, column=2)
boton6=Button(frame1, text="6", width=3, command=lambda:NumeroPulsado("6"))
boton6.grid(row=3, column=3)
botonDiv=Button(frame1, text="/", width=3)
botonDiv.grid(row=3, column=4)

#-----Fila 3------
boton1=Button(frame1, text="1", width=3, command=lambda:NumeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(frame1, text="2", width=3, command=lambda:NumeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(frame1, text="3", width=3, command=lambda:NumeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRestar=Button(frame1, text="-", width=3)
botonRestar.grid(row=4, column=4)

#-----Fila 4------
boton0=Button(frame1, text="0", width=3, command=lambda:NumeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(frame1, text=",", width=3)
botonComa.grid(row=5, column=2)
botonIgual=Button(frame1, text="=", width=3, command=lambda:ElResultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(frame1, text="+", width=3, command=lambda:Suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)



root.mainloop()
