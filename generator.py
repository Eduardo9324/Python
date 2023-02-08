# Funcion que devuelve una lista de numeros pares -- ejemplo con funcion
""" def functionPar(limit):
  num = 1
  listt = []

  while num <= limit:
    listt.append(num * 2)
    num += 1

  return listt

print(functionPar(21)) """


# EJEMPLO CON UN GENERADOR

""" Cda vez que un generador almacena un elemento en una variable, este entra en estado de "suspencion de estado", hasta que se realiza otro llamado a la funcion generadora """

""" def generatorPar(max):
  num = 1

  while num <= max:
    yield num * 2

    num += 1

nums = generatorPar(15)
 """

""" for i in nums:
  print(i) """

#print(next(nums))

def generatorEjem2(*citys):
  for i in citys:
    yield from i
    """ el yield from reemplaza un bucle for anidado, accede a un sub elemento contenido dentro de otro mas grande """

""" el la variable "view_citys" se guarda el objeto iterable que devuelve yield, y esta variable se puede recorrer despues por un bucle while o for segun corresponda"""

view_citys = generatorEjem2("bogota", "medellin", "cali", "ibague")

""" el metodo next() devuelve uno a uno los elemento generador por la funcion """ 
print(next(view_citys))
print(next(view_citys))
print(next(view_citys))