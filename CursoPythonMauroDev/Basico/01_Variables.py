# Variables
from operator import le

my_string_variable = "My String Variable"
#print(my_string_variable)

my_int_variable = 5
#print(my_int_variable)

my_bool_variable = False
#print(my_bool_variable)

# funciones del sistemas
print("Total de caracteres:",len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = 'miguel','fernandez', 'migue', 35
print(name,surname,alias,age)

#name = input('Cual es tu nombre?: ')
#age = int(input('Cual es tu edad?: '))
print(name,age)

# Fuerte tipado Python
address : str = 'mi direccion'
print(address)
print(type(address))

# Formateo de cadenas
print('Mi nombre es {} y mi edad es {}'.format (name,age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
print(f'Mi nombre es {name} y mi edad es {age}')

# Desempaquetado de cadenas
language = 'Python'
a,b,c,d,e,f = language

print(a)
print(b)

# Division de cadenas
language_slice = language[1:3]
print(language_slice) 

# Revertir cadenas
reversed_language = language[::-1]
print(reversed_language) 

# Funciones de cadenas
print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower())
print(language.lower().isupper())
