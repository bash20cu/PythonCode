class coche():  #Nueva Clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    def arrancar(self): #Metodo dentro de la clase
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "En marcha"
        else:
            return "Detenido"

miCoche=coche() #Instanciar una clase

print("El largo del chasis es: ", miCoche.largoChasis)
print("Tiene ", miCoche.ruedas," ruedas")
miCoche.arrancar()
print(miCoche.estado())

# segundo objeto

miCoche2=coche() #Instanciar una clase

print("El largo coche2 del chasis es: ", miCoche2.largoChasis)
print("Tiene ", miCoche2.ruedas," ruedas")
#miCoche.arrancar()
print(miCoche2.estado())
