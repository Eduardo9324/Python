#Creando un conjunto con set, debe recibir una lista como parametro
#Los datos de los "sets", no son modificables
conjunto = set(["hola", "manuel"]) #aqui solo pueden ir datos que no se muten, por eso no puede haber una lista dentro de un conjunto 

""" conjunto[0] = 3 """    #esto so se puede hacer con los conjuntos
print(type(conjunto))

#agregando un conjunto dentro de otro conjunto, usando la funsion frozenset() que recibe una lista por parametro
conjunto_uno = frozenset(["hola", "cristian"])

conjunto_dos = set(["milena", "maria", conjunto_uno])
print(conjunto_dos)


#Teoria de conjuntos
conjunto_tres = {1, 3, 5, 7, 9}
conjunto_cuatro = {1, 3, 5}

#Verificar si un conjunto es un SUB-CONJUNTO de otro
#La funsion issubset da True o False, si es o no un sub-conjunto
resultado = conjunto_cuatro.issubset(conjunto_tres)
#otra opcion para hacer lo mismo
""" resultado = conjunto_cuatro <= conjunto_tres """

print(resultado)


#Verificando si es un SUPER-CONJUNTO
""" result = conjunto_tres.issuperset(conjunto_cuatro) """
result = conjunto_tres >= conjunto_cuatro
print(result)


#verificar si hay algun numero en comun, me da False con un solo numero que sea igual en ambos conjuntos, True si no hay ninguno igual 
resul_3 = conjunto_cuatro.isdisjoint(conjunto_tres)
print(resul_3)