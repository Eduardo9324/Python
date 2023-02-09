# Guardo en la variable "archivo" el metodo ope, que recibe como argumento la ruta donde esta ubicado el archivo que se quiere leer, al final de la direccion de la ruta se especifica el nombre del achivo con su extension.
# Agrega como segundo argumento (encoding="UTF-8") para asegurarnos que la codificacion de los caracteres sea correcta, esto hace que funsiones correctamente las comas, tides, y demas caracteres especiales, etc.

# Abre el archivo asignando codificacion universal
archivo = open("Archivos_externos\Archivos\conversacion.txt", encoding="UTF-8")

# Lee el archivo completo
""" print(archivo.read()) """


# Leer linea por linea
#readlines() retorna un arreglo con todas las lineas, no es muy apto para leer archivos muy grandes debido al consumo de memoria
""" lineas = archivo.readlines()
print(lineas) """


# Leer una sola linea, el numero que se para como argumento representa la cantidad de caracteres que se van a leer de la linea
linea = archivo.readline()
print(linea)


# Depues de manipular el archivo siempre hay que cerrarlo
archivo.close()
# SIEMPRE HAY QUE CERRAR LOS ARCHIVOS, EL NO HACERLO PUEDE CONLLEVAR A POSIBLE PERDIDA DE INFORMACION A CAUSA DE CIEERES INESPERADOS O DE MANERA BRUSCA 

# Si se qiere volver a leer y/o manipular el archivo despues de haberlo cerrado, hay que usar de nuevo la funsion open()