import pickle

""" La clase Persona define un objeto que representa una persona con un nombre, un género y una edad. El método __init__ es el constructor de la clase y se llama automáticamente cuando se crea una nueva persona. El método __str__ devuelve una representación en forma de cadena de la persona.

La clase Lista_personas define una lista de objetos Persona. El método agregar_persona añade una persona a la lista y el método mostrar_persona muestra todas las personas en la lista.

El código crea un objeto mi_lista de la clase Lista_personas y luego crea un objeto p de la clase Persona con los valores "Sandra", "Femenino", 29. Finalmente, añade el objeto p a la lista mi_lista y muestra todas las personas en la lista. """


class Persona():
  def __init__(self, nombre, genero, edad):
    self.nombre = nombre
    self.genero = genero
    self.edad = edad
    print(f"Una persona con el nombre '{self.nombre}' ha sido creada.")
    
  def __str__(self):
    return "{} {} {}".format(self.nombre, self.genero, self.edad)
  
  
class Lista_personas():
  #Creo la lista de persosnas
  personas = []
  # Define un constructor para agregar info al fichero "ab+" quiere decir que agrega informacion binaria al fichero, y se almacena en la variable "lista_de_personas"
  def __init__(self):
    lista_de_personas = open("fichero_externo", "ab+")
    # Este metodo "seek" lo que hace es desplazar el cursor al inicio del fichero pasandole como argumento el indice "0" para que pueda leer toda la informacion
    lista_de_personas.seek(0)
    
    # Ahora cargo toda la informacion pasando como argumento la variable del fichero
    try:
      self.personas = pickle.load(lista_de_personas)
      print("Se han cargado {} personas del fichero externo".format(len(self.personas)))
    except:
      print("No hay informacion en el momento") #La primera vez se ejecuta el except porque aun no hay info guardada en el fichero
    finally:
      lista_de_personas.close()
      del(lista_de_personas)
  
  def agregar_persona(self, p):
    self.personas.append(p)
    self.guardar_personas_en_fichero_externo()
    
  def mostrar_persona(self):
    for i in self.personas:
      print(i)
      
  def guardar_personas_en_fichero_externo(self):
    Lista_personas = open("fichero_externo", "wb")
    pickle.dump(self.personas, Lista_personas)
    Lista_personas.close()
    del(Lista_personas)
    
  def mostrar_info_fichero_externo(self):
    print("La informacion del fichero externo es la siguiente: ")
    for j in self.personas:
      print(j)
      
mi_lista = Lista_personas()

persona = Persona("Ana", "Femenino", 19)
mi_lista.agregar_persona(persona)
mi_lista.mostrar_info_fichero_externo()

""" p = Persona("Antonio", "Masculino", 39)
mi_lista.agregar_persona(p)
p = Persona("Ana", "Femenino", 19)
mi_lista.agregar_persona(p)

mi_lista.mostrar_persona() """






""" El método format() en Python es una manera de formatear y concatenar cadenas de texto. Es una manera flexible y eficiente de crear cadenas de texto complejas a partir de varios componentes.

El método format() se puede aplicar a una cadena de texto con llaves {} que representan lugares donde se deben insertar valores. Por ejemplo: """

""" name = "John"
print("Hello, {}!".format(name)) """
# Resultado: Hello, John!


""" Además de insertar valores simples, también se pueden especificar formatos para números, fechas y otros tipos de datos. Por ejemplo: """

""" price = 4.99
print("The price is ${:.2f}".format(price)) """
# Resultado: The price is $4.99


""" El método format() también se puede utilizar con variables de tipo str, int, float, bool, list, tuple y dict, entre otros.

En resumen, el método format() es una manera poderosa y flexible de formatear y concatenar cadenas de texto en Python, que permite un control preciso sobre el formato de la salida y la inclusión de valores dinámicos. """
