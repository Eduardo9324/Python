class Coche():
  def desplazamiento(self):
    print("Me desplazo utilizando cuantro ruedas")
    
    
#Dos clases con un mismo metodo pero comportamientos distintos
    
    
class Moto():
  def desplazamiento(self):
    print("Me desplazar utilizando dos ruedas")
    
    
class Camion():
  def desplazamiento(self):
    print("Me desplazar utilizando seis ruedas")
    
    
""" #Creo una instancia de la clase "Moto"
mi_vehiculo = Moto()
mi_vehiculo.desplazamiento()


#Creo una instancia de la clase "Coche"
mi_vehiculo_2 = Coche()
mi_vehiculo_2.desplazamiento()


#Creo una instancia de la clase "Camion"
mi_vehiculo_3 = Camion()
mi_vehiculo_3.desplazamiento() """


#Todo lo comentado se puede reemplazar con el polimorfismo de esta manera
def desplazamiento_vehiculo(vehiculo):
  vehiculo.desplazamiento()
  
#Creo una instancia de la clase
mi_vehiculo = Coche()
#Ejecuto la funsion y le paso como argumento la instancia recien creada
desplazamiento_vehiculo(mi_vehiculo)
