# Sets >> Diccionarios

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_set = {'banana', 'orange', 'mango', 'lemon'}

print(my_set)

my_dict = dict()
my_other_set = {}

my_dict = {
    'first_name':'migue',
    'last_name':'fernandez',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(my_dict)