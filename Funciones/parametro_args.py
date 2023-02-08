# Forma no optima de sumar valores
""" def suma(lista):
  numeros_sumados = 0
  for i in lista:
    numeros_sumados += i
  return numeros_sumados
  
  
resultado = suma([5, 6, 8, 10, 1, 10, 6])
print(resultado) """


# Forma optima, utiliza el parametro args el * permite que "numeros" acepte un numero indeterminado de argumentos, (*args) debe ser el ultimo parametro
# (*args) es infinito al recibir multiples valores, por esa razon debe ir al ultimo
def suma(nombre, *numeros):
  return f"{nombre}, la suma de tus numeros es: {sum(numeros)}" 

resultado_dos = suma("Cris", 5, 8, 7)
print(resultado_dos)