# Clases #

class Person:  
  def __init__(self, name, surname, alias = 'Sin alias'):
    self.name  = name
    self.surname = surname
    self.alias = alias
  
  def  print_name(self):
    print(f'\n Nombre: {self.name} '+ 
          f'\n Apellido: {self.surname} \n Alias: ({self.alias}) \n')
  
  
my_person = Person('migue','fernandez')
my_person.print_name()

my_person2 = Person('alejandro', 'Arteaga', 'El otro Yo')
my_person2.print_name() 

