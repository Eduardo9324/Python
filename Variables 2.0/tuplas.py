#Creando tuplas con Tuple, recibe una lista 
tupla = tuple(["dato,", "dato2"])
print(tupla)

#Segunda forma para crear tuplas, sin () ni nada forma una tupla
tupla_dos = "carlos", "rocio"
print(type(tupla_dos))

#Tuplas con UN SOLO DATO, puede o no llevar los (), debe llevar una "," al final porque si no se agrega la "," sera un string comun y corriente

tupla_tres = ("eduardo",)
print(type(tupla_tres))


#Las tuplas deberian usarse cuando son datos de solo lectura, ya que manejan mejor la memoria, las listas al poder ser mutables utilizan dos espacios de memoria mediante variables, es por eso que las tuplas son mas eficientes para solo lectura de datos (FIJOS), que no requeriran modificaciones, la lista debe usarse cuando los datos deben cambiar constantemente


mi_tuplas = ["bien", 2, {"nombre":"juan"}]
print(mi_tuplas)