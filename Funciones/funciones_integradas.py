""" Las funciones integradas en Python son aquellas que vienen preconstruidas en el lenguaje y están disponibles para ser usadas sin la necesidad de importar módulos adicionales. Algunos ejemplos de funciones integradas en Python incluyen:

print(): Imprime una cadena de texto o valor en la consola.
len(): Devuelve la longitud de un objeto, como una lista o una cadena de texto.
str(): Convierte un objeto a una cadena de texto.
int(): Convierte un objeto a un entero.
float(): Convierte un objeto a un número con decimales.
sum(): Devuelve la suma de los elementos en un objeto iterable, como una lista o un rango.
min(): Devuelve el elemento mínimo en un objeto iterable.
max(): Devuelve el elemento máximo en un objeto iterable.
sorted(): Devuelve una lista ordenada de un objeto iterable.
abs(): Devuelve el valor absoluto de un número. """

# Encuentra el numero mayor de una lista, (Aplica para cualquier iterable)
numeros = [16, 28, 30, 45, 57, 689, 74, 83]
# Funcion max()
numero_mas_alto = max(numeros)
print(numero_mas_alto)

""" La función max() también se puede usar con cadenas de texto en Python. Cuando se utiliza con cadenas, la función devuelve la cadena de texto con la mayor ordenación lexicográfica. """

cadena_max = max('apple', 'banana', 'cherry')
#'cherry'
print(cadena_max)

""" En este ejemplo, la función max() devuelve la cadena de texto 'cherry', ya que es la cadena con la mayor ordenación lexicográfica. """



print("----------------------------------------------------------------")

# Numero mas bajo con la funcion min()
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

print("----------------------------------------------------------------")

# Redondeando un numero, puedo escoger cuantos decimales va a tener, lo redonde hacia arriba o hacia abajo dependiendo de su primer decimal
# El segundo parametro que se pasa representa "LA CANTIDAD DE NUMEROS DECIMALES QUE QUIERO O NECESITO MOSTRAR "
numero = 14.486534588
print(round(numero, 4))

print("----------------------------------------------------------------")

# La funsion bool retorna False si se le pasa como argumento un False, un 0 o vacio, cualquier numero diferente de 0, un string, o una estructura de datos que no este vacia retorna True 
resultado_bool = bool(5)
print(resultado_bool)

print("----------------------------------------------------------------")
# Retorna True si todos los valores son True, recibe una lista como argumento
""" La función all() en Python se utiliza para determinar si todos los elementos de un objeto iterable son verdaderos. La función devuelve True si todos los elementos son verdaderos, y False en caso contrario. Un elemento se considera verdadero si es distinto de False, None, 0, 0.0, [], (), {}, o una cadena vacía ''. """
resultado_all = all([[5, 6], "hola", True])
print(resultado_all)

print("----------------------------------------------------------------")
# sum suma todos los valores de un iterable
""" La función sum() en Python se utiliza para sumar los elementos de un objeto iterable, como una lista o un rango de números. La sintaxis de la función es la siguiente: """

""" sum(iterable, start) """

""" iterable: Es un objeto iterable, como una lista, un rango, una tupla, etc.
start: Es un valor opcional que se utiliza como valor inicial para la suma. Si no se especifica, el valor inicial es 0. """

sum([1, 2, 3, 4, 5])
#15
sum([1, 2, 3, 4, 5], 10)
#25

""" En este ejemplo, la función sum() devuelve 15 al sumar los elementos de la lista [1, 2, 3, 4, 5] y 25 al sumar los elementos de la lista [1, 2, 3, 4, 5] con un valor inicial de 10. """

