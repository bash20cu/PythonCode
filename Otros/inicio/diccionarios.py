dicc={0:"hola","Alemania":"Berlin","Francia":"Paris", "Espanna":"Madrid"}
print(dicc)

dicc["Italia"]="Lisboa"
print(dicc)

dicc["Italia"]="Roma"
print(dicc)


del dicc[0]
print(dicc)

"""Declarando una tupla como clave de dicc"""
paises=("Alemania","Francia","Espanna")
dicc1={paises[0]:"Berlin",paises[1]:"Paris",paises[2]:"Madrid"}

print("Diccionario con tupla")
print(dicc1)

print(dicc1.keys())
print(dicc.values())
print(len(dicc1))
