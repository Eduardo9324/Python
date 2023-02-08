#Function List: Crea una lista, creando una lista con List(), (No es muy comun usar esta manera para crear una lista)
listas = list(["hola", "Cristian", 82])
print(type(listas))

#Function Len() aplicado a una lista me devuelve la cantidad de elememntos dentro de la lista 
mi_lista = ["hola", 2, 6, True]
print(len(mi_lista))

#append agrega un elemento al final de la lista, (ELEMENTOS POR SEPARADO)
mi_lista.append("jajajaja")
print(len(mi_lista))

#insert agrega un elemento a la lista en un indice especifico, recibe dos argumentos, el primero es el indice, y el segundo el elemento a agregar 
mi_lista.insert(1, False)
print(mi_lista)

#extend agrega varios elementos a la lista, los deja todos al final, se pasa en forma de lista con los []
mi_lista.extend(["cris", 56, 74, 5.2])
print(mi_lista)

#pop permite eliminar un elemento de la lista usando el indice, si no se pasa ningun indice, elimina el ultimo elemento de la lista
mi_lista.pop(1)
print(mi_lista)


#remove, quita un elemento de la lista por su valor, se le pasa como argumento el elemento especifico que se quiere eliminar de la lista
mi_lista.remove(74)
print(mi_lista)


#clear, elimina todos los elemento de la lista, (DEJA LA LISTA VACIA)
""" mi_lista.clear()
print(mi_lista) """


#sort ordena los elementos de una lista, (PASAR COMO ARGUMENTO reverse=True INVIERTE EL ORDEN DE LA LISTA)
lista = [65, 25, 20, 785, 366, 52, 2, 65, 74]
print("Lista original:", lista)
lista.sort()
print("Lista ordenada:", lista)

lista.sort(reverse=True)
print("Lista invertida:", lista)


#reverse invierte el orden de los elementos de la lista tal cual esten, no admite referencia a otras variables, en ese caso muestra None
print(mi_lista)
mi_lista.reverse()
print(mi_lista)

""" print(dir(list)) """


#index en listas, me devuelve el indice del elemento buscado 
encuentra = mi_lista.index(6)
print(encuentra)


#la funsion dir() me muestra las cosas que puedo hacer con algo especifico, me muestra en consola los metodos

#Tupla
""" hhh = (5, 6, "hola")
print(dir(hhh)) """

#conjunto, no se puede usar index en los conjuntos
conj = set(["a", "b", "c", "d", "e"])
print(conj)