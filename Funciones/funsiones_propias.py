# Creando una funsion simple 

# La palabra def viene de Definition, seguido del nombre de la funsion, los () para los parametros
""" def saludo():
  print("Hola flaco, Como estas ?") """
  
# Ejecucion de la funsion, va a ejecutar la funsion todas las veces que se llama la funsion
""" saludo()
saludo()
saludo()
saludo()
saludo()
saludo()
saludo()
saludo() """


# Funsion con parametros
""" El if es seguido de la condición a evaluar y el else es seguido del valor que se devolverá si la condición es falsa. La evaluación de la condición y la asignación del valor correspondiente se realiza en una sola línea.  """

def saludo(nombre, genero):
  nombre = nombre.capitalize()
  adjetivo = "princesa" if genero.lower() == "femenino" else "rey" if genero.lower() == "masculino" else "amor"
  print(f"Hola {nombre}, mi {adjetivo}, como estas ?")
  
saludo("eduardo", "")


# Crea una funsion que retorna valores

""" Agregué un % 26 a cada una de las operaciones para asegurar que los índices siempre sean válidos para la cadena chars. Esto es importante porque si num es mayor que 26, los índices calculados pueden ser más grandes que la longitud de la cadena, lo que resultaría en un error de índice fuera de rango. Al utilizar el operador módulo %, aseguramos que los índices siempre sean válidos y estén dentro del rango permitido. """

""" def generar_contraseña(num):
  chars = "qzaxwsdcerfvbgtynhujmkiolp"
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
  return contraseña

  
generar_contraseña(564) """

import random
import string

def generar_contraseña(longitud=8):
  caracteres_seguros = string.ascii_letters + string.digits + string.punctuation
  longitud = min(longitud, 10)
  contraseña = ''.join(random.choice(caracteres_seguros) for i in range(longitud))
  print("Tu nueva contraseña es:", contraseña)
  # Usar return lo que permieste es guardar en una variable el resultado de la funsion, permite manipular los resultados de la funsion fuera de funsion
  return contraseña
# Recibe numeros como argumento
generar_contraseña(1121904064)
