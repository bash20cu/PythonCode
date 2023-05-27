# Listas #
my_list = list()
my_other_list = []

# tamanno de la lista 
print (len(my_list))

my_list = [ 35,24,15,'miguel','fernandez']
print (len(my_list))

print(my_list[0])

# Insertar al final 
my_list.append('Edad-32')
print(my_list)

# Insertar con indice
my_list.insert(1,'insertado-indice-1') 
print(my_list)

# Copiar la lista en una nueva referencia 
my_new_list =  my_list.copy()

# Borrado primera coincidencia
my_list.remove(24)
print(my_list)

# Borrado de elemento
del my_list[0]
print(my_list)

# Borrado del ultimo elemento con retorno del elemento
print(my_list.pop())

# Borrado de elemento con indice con retorno del elemento
print(my_list.pop(2))

print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)



