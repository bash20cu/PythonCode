def suma(num1,num2):
    result=num1+num2
    return resultado
def resta(num1,num2):
    return num1-num2
def multi(num1,num2):
    return num1*num2
def div(num1,num2):
    try:
        return num1/num2
    except Exception as e:
        Print(e)
        return "Operacion Erronea"
op1=(int(input("numero 1 ?:")))
op2=(int(input("numero 2 ?:")))
operacion=input("operacion? suma, resta, multi, div -> ")

if operacion=="suma":
    print(suma(op1,op2))
