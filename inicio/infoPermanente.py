import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas=[]

    def __init__(self):
        ListadePersonas=open("FicheroPersonas", "ab+")
        ListadePersonas.seek(0)
        try:
            self.personas=pickle.load(ListadePersonas)
            print(" -----  Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("----- ----- El fichero esta vacio ------ ------")

        finally:
            ListadePersonas.close()
            del(ListadePersonas)

    def AgregarPersonas(self, p):
        self.personas.append(p)
        self.GuardarPersona()

    def MostrarPersonas(self):
        for p in self.personas:
            print(p)

    def GuardarPersona(self):
        ListadePersonas=open("FicheroPersonas", "wb")
        pickle.dump(self.personas, ListadePersonas)
        ListadePersonas.close()
        del(ListadePersonas)

    def MostrarInfoFichero(self):
        print(" ----- ------ La info del fichero es: ----- -----")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()

#p=Persona("Sandra", "Femenino", 29)
#miLista.AgregarPersonas(p)

#p=Persona("Migue", "Masculino", 30)
#miLista.AgregarPersonas(p)

#p=Persona("Ney", "Masculino", 50)
#miLista.AgregarPersonas(p)

miLista.MostrarPersonas()
miLista.MostrarInfoFichero()
