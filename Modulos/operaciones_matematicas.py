#Para usar funsionalidades que estan en otros arcivos se usa la palabre import y el nombre del archivo
#EJS:
""" import modulos
modulos.sum(2, 6) """

#De esta manera solo importa una funsionalidad especifica
""" from modulos import rest
rest(25, 10) """

#De esta manera importa todas las funsionalidades del archivo
""" from modulos import *
sum(2, 6)
rest(23, 3)
mult(8, 8) """

#Python por defecto busca el modulo en la misma carpeta donde esta el archivo que lo esta requiriendo, si no lo encuentra lo busca en la ruta de instalacion de python, para importar funsionalidades de un archivo que esta en cualquier ruta, es necesario el uso de los PAQUETES