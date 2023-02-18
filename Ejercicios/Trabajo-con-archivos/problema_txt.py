# Dos lista, una con nombres y otra con apellidos

nombres = ["Cristian", "Eduardo", "Juan", "Jose", "Marcela"]
apellidos = ["Cruz", "Toro", "Gomez", "Vargas", "Castro"]

# registrar info en un TXT
# Creando el archivo
with open("Ejercicios\Trabajo-con-archivos/nombres_completos.txt", 'w') as archivo:
  archivo.writelines("Los datos son: \n\n")
  # Para crear un bucle en una sola linea es importante hacerlo dentro de una lista, es una forma de simplificar la sintaxis, de los contario habria que poner todo el codigo directamente dentro del bucle
  [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n, a in zip(nombres, apellidos)]