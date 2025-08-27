#Repasa Python (2–3 horas):
#Tipos de datos (int, float, str, list, dict).

int = 10
float_num = 10.5
string = "Hola, Mundo"
my_list = [1, 2, 3, 4, 5]
my_dict = {"clave1": "valor1", "clave2": "valor2"}

print(type(int), type(float_num), type(string), type(my_list), type(my_dict))

#Operadores básicos (aritméticos, lógicos, de comparación).
a = 10
b = 5
print("Operadores basicos: valor de a:", a,"valor de b: ", b)
print('Suma:',a + b)  # Suma
print('Resta ',a - b)  # Resta 
print('multiplicacion ',a * b)  # Multiplicación
print('División',a / b)  # División
print('Módulo ',a % b)  # Módulo
print("Igualdad ", a == b) # Igualdad
print('Desigualdad ', a != b) # Desigualdad
print("Mayor que ", a > b)  # Mayor que
print("Menor que ", a < b)  # Menor que
print("Mayor o igual que ", a >= b) # Mayor o igual que
print("Menor o igual que ",a <= b) # Menor o igual que
print('Operador lógico AND ',a > 5 and b < 10) # Operador lógico AND
print('Operador lógico OR ',a > 5 or b < 5)   # Operador lógico OR  
print('Operador lógico NOT ',  not(a > b))        # Operador lógico NOT  
#Estructuras de control (if, elif, else).
num = 7
if num > 0:
    print("El número es positivo")
elif num == 0:
    print("El número es cero")  
else:
    print("El número es negativo")



#Bucles for / while.
print("Bucle for")
for i in range(5):
    print(i)

#Funciones (def, argumentos, retorno).

#Ejercicio: escribe una función que reciba una lista de números y devuelva el promedio, el máximo y el mínimo.
def calcular_estadisticas(numeros):
    promedio = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print("Promedio:", promedio)
    print("Máximo:", maximo)  
    print("Mínimo:", minimo)
    return promedio, maximo, minimo

print(calcular_estadisticas([1, 2, 3, 4, 5]))
