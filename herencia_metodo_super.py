#FUNCTION super(), llama al metodo de la clase padre

#Defino primera clase
class Persona():
  
  #Defino constructor, es un estado inicial, aqui me pregunto que caracteristicas va a tener mi clase en cuestion, y se los paso como parametros
  def __init__(self, name, age, address):
    #Aqui se definen variables de clase
    self.name = name
    self.age = age
    self.address = address
    
  #Defino metodo - recibe self como argumento
  def description(self):
    print("Nombre:", self.name, "- " "Edad:", self.age, "- " "Address:", self.address)
    
    
    
    #Entre la primera y la segunda clase puedo pensar que caracteristicas pueden tener en comun y asi hacer que mi segunda clase herede atributos y metodos de la primera clase: EJ: un empleado tambien es una persona, por lo cual la clase "Empleado", puede heredar de la clase "Persona"
    
#Defino segunda clase, y hereda de la clase "Persona", ahora "Empleado a demas de sus propios atirbutos cuenta tambien con los atributos de la clase "Persona"

class Empleado(Persona):
  #Constructor con las caracteristicas que tendra la clase
  def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, recidencia_empleado):
    #sper() esta llamando almetodo __init__ de la clase padre, una vez se ejecute el constructor de la clase "Empleado", se llamara al constructor de la clase "Persona"
    super().__init__(nombre_empleado, edad_empleado, recidencia_empleado)
    #Variables de clase
    self.salario = salario
    self.antiguedad = antiguedad
    
  def description(self):
    super().description()
    print("Salario:", self.salario, "- " "Antiguedad:", self.antiguedad)
    
    
#Construyo un objeto de tipo persona, y en los (), le paso como argumentos los valores de los parametros definidos en el constructor de la clase "Persona"

""" antonio = Persona("Antonio", 55, "España")
antonio.description() """


#Construyo un objeto de tipo "Empleado"
manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
#Es codigo da error, porque si bien la clase "Empleado" esta herendando de la clase "Persona" incluido el metodo descripción, este no tiene definidos los argumentos que se quieren mostrar en consola, EJ: en "name", este eroor se puede solucionar con super() en la clase "Empleado"
manuel.description()


#isinstance() se utiliza para saber si un objeto es instancia de una clase determinada, devuelve True si lo es, si no devuelve False, recibe dos argumentos, el primero es la instancia y el segundo es la clase

print(isinstance(manuel, Persona))