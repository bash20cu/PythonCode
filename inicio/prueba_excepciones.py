def suma(num1, num2):
	 return num1+num2

def resta(num1, num2):
	 return num1-num2

def multiplica(num1, num2):
	 return num1*num2

def divide(num1,num2):
	 try:
		return num1/num2
	 except ZeroDivisionError:
		print("no se puede dividir por 0")
		return "Operacion Erronea"



op1=(int(input("Introduce el primer numero:")))

op2=(int(input("Introduce el segundo numero:")))

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,div):")

if operacion=="suma":
	 print(suma(op1,op2))

elif operacion=="resta":
	 print(resta(op1,op2))

elif operacion=="multiplica":
	 print(multiplica(op1,op2))

elif operacion=="div":
	 print(divide(op1,op2))

else:
	 print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")
