# Que son los modulos ?: (Cualquier archivo) son archivos con extension .py, .pyc (Python compilado), un modulo puede contener variables, funsiones, clases, incluso otros modulos.

#Para que sirven ?: para organizar y reutilizar el codigo (MODULARIZACION Y REUTILIZACION)

#Como se crea un modulo en Python ?: es solo crear un archivo .py y guardarlo donde convenga

#Ej:
# modulo_saludar lo importa como un objeto, con el "as" puedo asignar otro nombre al modulo
""" import modulo_saludar as saludo """

# para importar uns funsion especifica de un modulo puedo usar esta sintaxis, desde ese modulo importamos dos funsiones, tambien se puede asignar un nuevo nombre a las funsiones con el "as"
""" from modulo_saludar import saludar, saludar_raro """

# Para importar todas las funsionalidades de un modulo se usa, no es recomendable ya que hace muy pesado a los programas (MALA PRACTICA)
from modulo_saludar import *

def sum(num1, num2):
  """ resul = num1 + num2 """
  print(f"el resultado de la suma es: {num1 + num2}")
  
sum(5, 8)


def rest(num1, num2):
  """ resul = num1 + num2 """
  print(f"el resultado de la resta es: {num1 - num2}")
  
  
rest(16, 10)
  
  
def mult(num1, num2):
  """ resul = num1 + num2 """
  print(f"el resultado de la multiplicacion es: {num1 * num2}")
  
mult(7, 5)

# Funsion saludar importada


# Guardo en variables la llamada a las funsiones
hey = saludar("cris")
holis = saludar_raro("juan")

# Mostrar resultados
print(hey)
print(holis)


# ENRUTAMIENTO DE MODULOS
# Para acceder a un modulo en ptras rytas se debe usar la notacion del "." punto
# Ej:

# import carpeta.carpeta.modulo 

# accdiendo a los modulos de pytho
# import sys