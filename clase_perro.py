class NombreDeLaClase:
    # Atributos de la clase
    # Métodos de la clase
    pass


""" Por ejemplo, podríamos crear una clase llamada "Perro" que tenga atributos como "nombre" y "edad", y métodos como "ladrar" y "comer": """

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("Woof woof!")

    def comer(self, comida):
        print("El perro está comiendo", comida)
        
        
""" Una vez que se ha definido una clase, se pueden crear objetos (instancias de la clase) utilizando el nombre de la clase seguido de paréntesis: """


fido = Perro("Fido", 3)

""" Ahora fido es un objeto de la clase Perro con atributos "nombre" y "edad" y métodos "ladrar" y "comer". """
