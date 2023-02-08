def sum(num1, num2):
  return num1 + num2

def res(num1, num2):
  return num1 - num2

def mult(num1, num2):
  return num1 * num2

def div(num1, num2):
  """ En caso de no poder realizar lo que esta en el "try", pasa al "except" y maneja el error, si el error que genera la ejecucion del programa es diferente del que esta en el except igual el programa caera """
  try:
    return num1 // num2
  except ZeroDivisionError:
    print("No se puede dividir por 0")
    return "Operacion no valida !!!"

# Esto es un bucle infinito y la "Break" lo detiene
while True:
  try:
    op1 = int(input("Ingresa el primer numero: "))
    op2 = int(input("Ingresa el segundo numero: "))
    break

#Se pueden utilizar varias instrucciones "except" segudas para capturar los errores
  except ValueError:
    print("Valor ingresado no permitido, vuelve a intentarlo.")

operacion = input("Que operacion vas a realizar, (+, -, *, /): ")

if operacion == "+":
  print("El resultado es: " + str(sum(op1, op2)))

elif operacion == "-":
  print("El resultado es: " + str(res(op1, op2)))

elif operacion == "*":
  print("El resultado es: " + str(mult(op1, op2)))

elif operacion == "/":
  print("El resultado es: " + str(div(op1, op2)))

else:
  print("Operacion no completada")

print("Muchas gracias.")