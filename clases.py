""" palabra reservada class, el nombre de la clase en mayuscula primera letra, los metodos son funciones dentro de las clases y llevan como primer parametro OBLIGATORIO la palabre self, equivalente al this en javascript """

""" la palabra self hace referencia a la instancia de la clase """


""" En resumen, "self" es una referencia a la instancia actual de la clase, y se utiliza para acceder a los atributos y métodos de esa instancia. Es el primer argumento de cualquier método en una clase en Python y es pasado automáticamente por el interpretador de python. """

class Persona():
  #PROPIEDADES
  #Las caracteristicas comunes a todos los objetos se llaman "estado inicial"
  #Asi se definine un constructor en python 
  def __init__(self):
    #La sintaxis para encapsular una propiedad es colocar 2 guiones bajos al inicio de su nombre
    self.__nombre = "Juan"
    self.apellido = "Toro"
    self.cel = 32459541027
    self.__animo = False

  #METODOS
  def saludo(self, saludo):
    #Los 2 guiones bajos deben colocarse en el nombre de todas las variables que se desean esten encapsuladas, y en todas las partes del codigo donde se encuentren, EJ: "__animo" es una variable distinta de "animo"
    self.__animo = saludo

    if self.__animo:
      chequeo = self.__comprobando_vida()

    if self.__animo and chequeo:
      return "Esta vivo y feliz"
    elif self.__animo and chequeo == False:
      return "Algo va mal"
    else:
      return "No quiere hablar"

  def estado(self):
    print("El sujeto se llama, " + self.__nombre + " y su numero es: " + str(self.cel))

    #Sintaxis de metodo encapsulado
  def __comprobando_vida(self):
    print("Comprobando que el sujeto este vivo !!!")

    #Declarar variables dentro de un metodo
    self.latidos = "ok"
    self.pulso = "ok"
    self.respiracion = "ok"

    if self.latidos == "ok" and self.pulso == "ok" and self.respiracion == "ok":
      return True
    else:
      return False 



""" instancia de la clase, en python NO es necesaria la palabra "new" """

nueva_persona = Persona()
print(nueva_persona.saludo(True))

nueva_persona.estado()

print("-----------Segundo objeto-----------------")

#Dos instancias no pueden llevar el mismo nombre
persona2 = Persona()

print(persona2.saludo(False))

#Esto no deberia permitirse, porque esta cambiando una propiedad definida en el constructor
#La encapsulacion evita que las propiedades no puedan ser modificadas desde afuera de la clase 
persona2.__nombre = "Jose"

persona2.estado()

# Esta linea no tiene sentido, no se debe acceder a metodos de comprobaciones internas desde fuera de la clase, (encapsular propiedades y/o metodos es criterio del programador, segun el funcionamiento que requiere en el programa)
""" print(persona2.__comprobando_vida()) """



# CLASES - HERENCIA
# El nombre de la clase debe tener coherencia

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
    
#CLASE DE TIPO FURGONETA porque tiene todos los comportamientos de los demas vehiculos, no tiene sentido que herede de la clase moto puesto que una furgoneta no puede hacer el caballito, es cuestion de sentido comun !!!

class Furgoneta(Vehiculos):
  def carga(self, cargar):
    self.cargado = cargar
    if (self.cargado):
      return "La furgoneta esta cargada"
    else:
      return "La furgoneta esta vacia"

# SINTAXIS PARA HEREDAR
#Se construye una clase normal y como parametro se pasa el nombre de la clase padre
#Aqui se esta heredando todo, propiedades y metodos, incluso el constructo
class Moto(Vehiculos): #aqui se hereda el constructor
  hcaballito = ""
  def caballito(self):
    self.hcaballito = "Voy haciendo el caballito"
    
  def estado(self):
    #El "\n" significa un salto de linea
    print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "\nCaballito: ", self.hcaballito)
    
    
class Veh_electrico():
  def __init__(self):
    self.autonomia = 100
  def cargar_energia(self):
    self.cargando = True

miMoto = Moto("Honda", "CET93")
miMoto.caballito()
miMoto.estado()

mi_furgoneta = Furgoneta("Renault", "Kangoo")
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))

#HERENCIA MULTIPLE: es cuando una clase hereda de dos o mas clases
#Aqui hereda todos los metodos y propiedades de ambas clases 
class Bicicleta_electrica(Vehiculos, Veh_electrico):
  pass

#Cuando hay herencia multiple, siempre se da preferencia al heredar de la clase que este ubicada en el primer parametro en este caso "Vehiculos"
#Si hay metodos o atributos con el mismo nombre en ambas clases se da preferencia a la clase que esta en el primer argumento, los demas metodos que no tienen coincidencias en nombres se heredan todos sin conflictos
mi_bici = Bicicleta_electrica("BMW", "2002")

