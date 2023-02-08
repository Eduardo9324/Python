#Iterando una lista
animales = ["gato", "perro", "loro", "cocodrilo"]

""" for i in animales:
  print(i) """
  
  
#Otro Ej:


#Funsion itera con un bucle for una lista pasada como argumento, y multiplica cada elemento de la lista por 5, devuelve una nueva lista convertida a tupla
def multiplyca_secuencia(numero):
  multiplicados = []
  for i in numero:
    multiplicados.append(i * 5)
  return tuple(multiplicados)

numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(f"El resultado es: {multiplyca_secuencia(numero)}" )


#Recorriendo dos listas al mismo tiempo, (se podia hacer con la opcion de for anidados), o, mediante el uso de un solo bucle for y con el uso de la funsion "zip", pero ambas listas debe tener la misma cantidad de elementos

numbers = [1, 2, 3,]
names = ["mateo", "carlos", "miguel"]

for i, j in zip(numbers, names):
  print(f"{i}: {j}")
  
  
""" En teoría, puedes iterar sobre cualquier número de listas con la función zip en Python. La función zip toma como argumento una cantidad variable de secuencias (por ejemplo, listas, tuplas, etc.) y las combina en una sola secuencia de pares. Cada par incluye un elemento de cada secuencia, y se crean tantos pares como el número de elementos en la secuencia más corta.

Por ejemplo, si quieres iterar sobre tres listas al mismo tiempo, puedes hacer algo como esto: """

lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']
lista3 = [10, 20, 30, 40]

for element1, element2, element3 in zip(lista1, lista2, lista3):
    print(element1, element2, element3)
    
print("\n================================")
#Usando la función "enumerate"

""" La función enumerate es útil si necesitas acceder tanto al elemento como a su índice en la lista, mientras que el bucle for es más sencillo y adecuado para la mayoría de los casos en los que solo necesitas acceder al elemento. """

fruits = ["apple", "banana", "cherry"]
#De esta manera me devuelve una tupla con los valores "(indice y elemento)"
for i in enumerate(fruits):
    print(type(i))
    print(i)
    
#Asi me devuelve los tipos de datos por separado "int", "str", etc.
for i, fruit in enumerate(fruits):
    print(i, fruit)

print("----------------------------------------------------------------")
#Usando for else, el ese se ejecuta siempre una vez al final del bucle a ecepcion que halla un break, si el break se cumple no ejecuta el else
frutas = ["apple", "banana", "cherry"]
for i in frutas:
    if i == "cherrys":
        break
    print(i)
else:
    print("The loop completed successfully")

#Todo lo anterior funsiona tambien para tuplas