"""
print("nota?:")
nota=input()
def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion
print (evaluacion(nota))
"""

print("Acceso")
edad=int(input("edad?:"))
if edad<18:
    print("No puede pasar")
else:
    print("Pase")
