

# Crea un conjunto de números enteros
mi_conjunto = {1, 2, 3, 4, 5}

# Itera a través del conjunto
for numero in mi_conjunto:
    print(numero)

# Salida:
# 1
# 2
# 3
# 4
# 5


""" El bucle for itera a través de cada elemento en el conjunto y los muestra uno por uno. De esta manera, puedes hacer algo con cada elemento individualmente, como hacer un cálculo o agregarlo a otra estructura de datos.

Recuerda que los conjuntos no son secuencias ordenadas, por lo que los elementos pueden aparecer en cualquier orden al iterarlos. Si necesitas iterar a través de un conjunto en un orden específico, puedes convertir el conjunto a una lista o tupla antes de iterarlo. """


""" No puedes iterar un conjunto en Python usando for y range() juntos, ya que los conjuntos no son secuencias indexadas y, por lo tanto, no tienen un índice que pueda ser iterado por range(). En su lugar, debes iterar a través de los elementos del conjunto directamente usando un bucle for """