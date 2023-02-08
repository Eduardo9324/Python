#Puedes iterar a través de un diccionario en Python usando un bucle for. Hay dos formas comunes de hacerlo:

# 1 Iterar a través de las claves del diccionario:

# Crea un diccionario
mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'profesion': 'Ingeniero'}

# Itera a través de las claves del diccionario
for clave in mi_diccionario:
    print(clave)

# Salida:
# nombre
# edad
# profesion


# 2 Iterar a través de las claves y valores del diccionario:

# Crea un diccionario
mi_diccionario_dos = {'nombre': 'Julian', 'edad': 39, 'profesion': 'Deportista'}

# Itera a través de las claves y valores del diccionario, esto devuelve una tupla con el para clave: valor
for clave, valor in mi_diccionario_dos.items():
    print(clave, valor)

# Salida:
# nombre Juan
# edad 30
# profesion Ingeniero

""" El método items() devuelve una vista de los pares clave-valor del diccionario como tuplas, que luego pueden ser iteradas a través de un bucle for. De esta manera, puedes hacer algo con cada par clave-valor individualmente. """


""" Recuerda que los diccionarios en Python no tienen un orden garantizado, por lo que los elementos pueden aparecer en cualquier orden al iterarlos. Si necesitas iterar a través de un diccionario en un orden específico, debes ordenar el diccionario antes de iterarlo. """