# Otros ejemplos de iteraciones

frutas = ["Manzana", "Banano", "Pera", "Granadilla", "Fresa", "Maracuya", "Lulo", "Guanabana"]

for i in frutas:
  if i == "Pera" or i == "Granadilla":
    # continue ignora el elemento y sigue iterando los demas
    continue
  print(f"Esta tarde voy a comer {i}")
else:
  print("Ya comio, y esta lleno !!!")
  
print("--------------------------------------------------")

for i in frutas:
  if i == "Banano":
    # break detiene la ejecucion del bucle cuando llegar a un determinado elemento
    break
  print(f"Esta tarde voy a comer {i}")
  
print("------------------------------------------------------------")

# Recorrer una cadena de texto (STRING), las cadenas las itera caracter por caracter
saludo = "Hola Cristian, Como estas mi brother ?"
for i in saludo:
  print(i)
  
print("------------------------------------------------------------")

# For en una sola linea de codigo
numeros = [5, 6, 10, 8]
#Multiplica cada elemento de la lista x 2, sintaxis opcional, puedo hacer cualquier operacion de esta manera para cada elemento
numeros_duplicados = [x**2 for x in numeros]
print(numeros_duplicados)