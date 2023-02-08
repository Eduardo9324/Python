mi_diccionario = {
  "nombre": "Cristian",
  "apellido": "Eduardo",
  "edad": 29
}

print(type(mi_diccionario))

#Keys me muesta solo las claves de los diccionarios, (tambien sirve para iterar)
claves = mi_diccionario.keys()
print(claves)

#get nos devuelve el valor de la clave que le pasamos por parametro, si no lo encuentra lanza "None", pero la ejecucion continua
#None indica que no tiene valor, es parecido a undefined en JavaScript
obtiene_valor = mi_diccionario.get("nombre")
print(obtiene_valor)
#Otra opcion, de esta manera, si no encuentra el elemento lanza una eception (ERROR) y el programa cae
""" obtiene_valor = mi_diccionario["cel"]
print(obtiene_valor) """


#Clear elimina todo del diccionario 
""" mi_diccionario.clear()
print(mi_diccionario) """


#pop elimina un solo elemento del diccionario, se debe pasar por argumento
mi_diccionario.pop("edad")
print(mi_diccionario)

#items devuelve una lista de pares de tuplas, se usa para iterar los diccionarios
items = mi_diccionario.items()
print(items)
