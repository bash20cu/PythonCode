class coche():  #Nueva Clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    def arrancar(self, arrancamos): #Metodo dentro de la clase
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "En marcha"
        else:
            return "Detenido"
    def estado(self):
        print("el coche tiene ",self.ruedas," ruedas. Un ancho de ", self.anchoChasis," y un largo de ", self.largoChasis)

miCoche=coche() #Instanciar una clase

print("El largo del chasis es: ", miCoche.largoChasis)
print("Tiene ", miCoche.ruedas," ruedas")
print(miCoche.arrancar(True))
miCoche.estado()

# segundo objeto

miCoche2=coche() #Instanciar una clase
print(miCoche2.arrancar(False))
print("El largo coche2 del chasis es: ", miCoche2.largoChasis)
print("Tiene ", miCoche2.ruedas," ruedas")
#miCoche.arrancar()
miCoche2.estado()
