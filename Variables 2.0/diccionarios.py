#Creando diccionario con la funcion dict
#Ej:
diccionario = dict(nombre = "lucas", edad = 32)

print(diccionario)


diccionario_2 = {("hola", "cris"): 2}

print(diccionario_2)

#Las tuplas pueden ser claves de los diccionarios, pero las listas no


#Esta función construye un diccionario con valores en None, el primer argumento que recibe es un iterable, para que no itere se pasan todos los datos en []
diccionario_3 = dict.fromkeys(["nombre", "apellido", "edad"])
print(diccionario_3)