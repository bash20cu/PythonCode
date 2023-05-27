# Funciones

def my_function ():
  print('una funcion')

my_function()

def generate_full_name ():
    first_name = 'Miguel'
    last_name = 'Fernandez'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
    
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
    
add_two_numbers()

def sum_two_numbers( num_one :int , num_two :int):
  num = num_one + num_two
  return num
print(sum_two_numbers(10,15))


def print_upper_texts(*texts):
  print(type(texts))
  for text in texts:
    print(text.upper())

print_upper_texts('hola', 'miguel', 'python sucks')