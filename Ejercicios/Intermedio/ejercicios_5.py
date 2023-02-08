# Crea una funsion que devuelve la serie de Fibonacci desde el 1 hasta el numero dado

# fibonacci que toma un número "num" como argumento 
""" def fibonacci(num):
  
  # a, b = 0, 1: Se inicializan dos variables a y b con los valores 0 y 1, respectivamente. Estos son los dos primeros números en la serie de Fibonacci.
  a, b = 0, 1
  
  # lista_fibonacci = []: Se crea una lista vacía llamada lista_fibonacci que almacenará los números de la serie de Fibonacci generados.
  lista_fibonacci = []
  
  # for i in range(num):: Se itera sobre un rango de números desde 0 hasta num.
  for i in range(num):
    
    # if b > num:: Si b es mayor que num, entonces se ejecuta el código dentro del if.
    if b > num:
      
      # return lista_fibonacci: Se devuelve la lista lista_fibonacci que contiene los números de la serie de Fibonacci generados hasta el momento.
      return lista_fibonacci
    else:
      # lista_fibonacci.append(b): Se agrega b a la lista lista_fibonacci.
      lista_fibonacci.append(b)
      
      # a, b = b, a + b: Se actualiza los valores de a y b para que a tome el valor de b y b tome el valor de a + b. Esto genera el siguiente número en la serie de Fibonac
      a, b = b, a + b
      
  # return lista_fibonacci: Finalmente, se devuelve la lista lista_fibonacci que contiene los num primeros números de la serie de Fibonacci.
  return lista_fibonacci """

""" result = fibonacci(1100)
print(result) """

print("================================")

""" Este código es una expresión lambda en Python que define una función anónima llamada primos_hasta que toma un número num como argumento y devuelve una lista de números primos hasta num.

lambda num :: Se define una expresión lambda que toma un argumento num.

list(filter(: Se utiliza la función filter para filtrar los elementos de una secuencia basándose en una condición.

lambda x : all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)): Esta es la condición que se utiliza para filtrar los elementos. Se define otra expresión lambda que toma un argumento x y devuelve True si todos los números en el rango 2 hasta int(x ** 0.5) + 1 no son divisores de x.

, range(2, num)): La secuencia que se filtra es un rango de números desde 2 hasta num.

): Finaliza la llamada a la función filter.

La expresión lambda devuelve una lista de números primos hasta num generados mediante un filtro sobre un rango de números. """

primos_hasta = lambda num : list(filter(lambda x : all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta(22))


def fibonacci(num):
  a, b = 0, 1
  lista_fibonacci = []

  while b <= num:
    lista_fibonacci.append(b)
    a, b = b, a + b

  return lista_fibonacci