""" convertir tupla a lista """
my_tup = ("cristian", 5, 9) # sintaxis tupla (las tuplas pueden omitir los parentesis, es opcional, pero no es recomendado)

my_list = ["garcia", 45, 852, True] # sintaxis lista

my_tup_convert = tuple(my_list) # convierte una lista en tupla

my_list_convert = list(my_tup) # convierte una tupla en lista

prueba = 3 in my_tup # busca un elemento dentro de una tupla

ejemplo = (5,) # sintaxis tupla unitaria

print(my_list_convert) # print muestra en consola
print(my_tup_convert)
print(prueba)
print(my_tup.count(5))
print(len(ejemplo)) # imprime la longitud


# DESEMPAQUETADO DE TUPLAS  == asigna los valores de la tupla a variavles

ejem = (100, 8, True, "hola")

num, num2, boo, saludo = ejem

print(num)
print(num2)
print(boo)
print(saludo)