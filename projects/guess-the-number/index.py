import random
# Este modulo le permite a Python trabajar con procesos aleatorios


def guess_the_number(x):
  
  print("================================================")
  print("            Bienvenido(a) al juego!             ")
  print("================================================")
  print("Tu meta es adivinar el numero generado por la computadora.")
  
  # generar numero aleatorio en un rango que va desde 1 hasta x (ambos inclusivos)
  random_number = random.randint(1, x)
  
  # Inicializa la variable en 0 para que no tenga posibilidad de coincidir con el numero random
  prediction = 0
  
  while prediction != random_number:
    # El usuario ingresa un numero
    prediction = int(input(f"Adivina un numero entre 1 y {x}: "))
    
    if prediction < random_number:
      print("Intentalo otra vez, el numero es muy pequeño.")
    elif prediction > random_number:
      print("Intentalo otra vez, el numero es muy grande.")
      
  print(f"Felicitaciones, adivinaste el numero, era el {random_number} correcto !!!")
  
  
guess_the_number(100)