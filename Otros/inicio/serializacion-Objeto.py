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

Coche1=coche() #Instanciar una clase
print("El largo del chasis es: ", Coche1.largoChasis)
print("Tiene ", Coche1.ruedas," ruedas")
print(Coche1.arrancar(True))
Coche1.estado()

# segundo objeto

Coche2=coche() #Instanciar una clase
print(Coche2.arrancar(False))
print("El largo coche2 del chasis es: ", Coche2.largoChasis)
print("Tiene ", Coche2.ruedas," ruedas")
#miCoche.arrancar()
Coche2.estado()
