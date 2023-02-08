# Crea una funsion que retorna los numeros primos entre 0 y el numero que pasamos

def es_primo(num):
  if num <= 1:
    return False
  
  for i in range(2, num - 1):
    if num % i == 0:
      return False
  return True

def primo_hasta(num):
  # primos = []: Se crea una lista vacía llamada primos que almacenará los números primos encontrados.
  primos = []
  
  # for i in range(2, num + 1):: Se itera sobre un rango de números desde 2 hasta num + 1.
  for i in range(2, num + 1):
    
    # resultado = es_primo(i): Se llama a una función externa llamada es_primo que determina si i es un número primo.
    resultado = es_primo(i)
    
    # if resultado:: Si la función es_primo devuelve True, entonces se ejecuta el código dentro del if.
    if resultado:
      #primos.append(i): Se agrega i a la lista primos.
      primos.append(i)
  # return primos: Finalmente, se devuelve la lista primos que contiene los números primos encontrados.
  return primos

""" resultado = primo_hasta(45)
print(resultado) """