def mensaje():
  print("Aprendiendo python")


def suma():
    num1=5
    num2=10
    print(num1+num2)
def suma_return(num1,num2):
    resultado=num1+num2
    return resultado

mensaje()
suma()
print(suma_return(5,15))

almacena_result=suma_return(5,8)
print(almacena_result)
