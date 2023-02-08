#Paquete para serializar
import pickle

class Vehiculos():
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):
    self.enmarcha = True

  def acelerar(self):
    self.acelera = True

  def frenar(self):
    self.frena = True

  def estado(self):
    #El "\n" significa un salto de linea
    print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)
    
    
coche_uno = Vehiculos("Mazda", "MX5")
coche_dos = Vehiculos("Seat", "Leon")
coche_tres = Vehiculos("Renault", "Megane")

#Creo una lista
coches = [coche_uno, coche_dos, coche_tres]

fichero = open("los coches", "wb")

""" El método pickle.dump es una forma de serializar objetos de Python y guardarlos en un archivo binario. La serialización es el proceso de convertir un objeto en una secuencia de bytes que se puede almacenar o transmitir a otra parte. """
# El primer parametro es la informacion que se quiere serializar, el segundo es el documento que recibe la info
pickle.dump(coches, fichero)

#Ya esta guardada la informacion, ahora cierro el fichero
fichero.close()
#Elimino el fichero de la memoria
del(fichero)

print("----------------------------------------------------------------------------------")


# PROCESO PARA DESERIALIZAR LA INFORMACION 

#Creo una variables que tiene el metodo "open", el cual recibe como parametro dos argumentos, el primero es el nombre del archivo que se quere deserializar, y el segundo argumento es el metodo de lectura y/o escritura del archivo

fichero_apertura = open("los coches", "rb")

#En esta variable guardo la info del archivo

mis_coches = pickle.load(fichero_apertura)

# Ya almacenada la info en la variable "mis_coches", proceso a cerra el fichero
fichero_apertura.close()

# Recooro la informacion con un bucle for

for i in mis_coches:
  print(type(i))
  print(i.estado())