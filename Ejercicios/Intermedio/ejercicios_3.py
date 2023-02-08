# El profesor no esta y la clase la van a dar los alumnos

# Pedir el nombre y la edad de los compañeros que vinieron a la clase 


# def cantidad_alumnos(cantidad):: Esta línea define la función cantidad_alumnos y toma un argumento cantidad.
def catidad_alumnos(cantidad):
  
  # alumnos = []: Aquí se crea una lista vacía llamada "alumnos" para almacenar la información de cada alumno.
  alumnos = []
  
  # for i in range(cantidad):: Este es un bucle for que itera cantidad veces.
  for i in range(cantidad):
    
    # nombre = input("Ingresa el nombre del alumno: "): En esta línea se pide al usuario que ingrese el nombre de un alumno y se almacena en la variable nombre.
    nombre = input("Ingresa el nombre del alumno: ")
    
    # edad = int(input("Ingresa la edad: ")): Aquí se pide al usuario que ingrese la edad de un alumno y se almacena en la variable edad.
    edad = int(input("Ingresa la edad: "))
    
    # alumno = (nombre, edad): Aquí se crea una tupla llamada alumno que contiene el nombre y la edad de un alumno.
    alumno = (nombre, edad)
    
    # alumnos.append(alumno): En esta línea se agrega la tupla alumno a la lista alumnos.
    alumnos.append(alumno)
    
    # alumnos.sort(key = lambda e : e[1]): Aquí se ordena la lista alumnos por la edad de los alumnos usando la función lambda e : e[1] como la clave para la comparación.
    alumnos.sort(key = lambda e : e[1])
    
    # asistente = alumnos[0][0]: Aquí se almacena el nombre del alumno más joven en la variable asistente.
    asistente = alumnos[0][0]
    
    # profesor = alumnos[-1][0]: En esta línea se almacena el nombre del alumno más viejo en la variable profesor.
    profesor = alumnos[-1][0]
    
    #return asistente, profesor: Finalmente, la función devuelve los nombres del alumno más joven y el más viejo.
  return asistente, profesor

# Desempaqueta 
asistente, profesor = catidad_alumnos(3)
print(f"El profesor es {profesor}, y el asistente es {asistente}.")

