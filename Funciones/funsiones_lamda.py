# Una función lambda en Python es una pequeña función anónima que puede tomar cualquier número de argumentos, pero solo tiene una expresión. Es una forma conveniente de crear funciones de una sola línea.

# Sintaxis de una funsion que estoy guardando en una variable, las lambda son aptas para usos pequeños, se retornan solas
suma = lambda a, b : a + (b * 3)
print(suma(5, 3))


# Funsion comun para saber si es par o no
""" def es_par(num):
  if num % 2 == 0:
    return True """


# Usando filter con una funsion comun
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

""" numeros_pares = filter(es_par, numbers)
print(tuple(numeros_pares)) """


# Filter con funsion lambda
numeros_pares = filter(lambda num : num % 2 == 0, numbers)
print(tuple(numeros_pares))

