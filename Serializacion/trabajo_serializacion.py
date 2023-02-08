#La serializacion es el procoso mediante el cual se codifican datos a binario
#La biblioteca de Python que importa todos los metodos para dicha tarea es "pickle"

#"Pickle" es un módulo de Python para serializar y deserializar objetos de Python. Le permite convertir objetos complejos de Python en un formato que se puede almacenar, transmitir y reconstruir fácilmente más tarde, incluso en una máquina diferente con un software diferente.

import pickle

nosbres_amigos = ["Alejandro", "Daniel", "Juan", "David", "Jordan", "Camilo", "Oscar"]

#Aqui creo el fichero externo para guardar la data
#"w" de wirte t "b" de binary
fichero_binario = open("lista_nombres", "wb")

#Agrega la info al fichero, dump recibe dos argumentos, primero la info que se quiere agregar, y el segundo es el nombre del fichero donde se va agregar
#El fichero en memoria, en esta caso es la variable en cuestion
pickle.dump(nosbres_amigos, fichero_binario)

fichero_binario.close()

#Acceder a la info codificada
fichero = open("lista_nombres", "rb")
lista = pickle.load(fichero)
print(lista)
