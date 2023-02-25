import random
import time

# Busqueda sencilla
""" def naiev_search(lists, target):
  for i in range(len(lists)):
    # Compara cada elemento de la lista con el target, si coincide retorna su indice, de lo contrario -1
    if lists[i] == target:
      return i
  return -1 """

""" lists = [1, 3, 5, 10, 12]
print(naiev_search(lists, 8)) """



# Busqueda binaria
# Esta funsion recibe como primer parametro una lista que debe estar ordenada de forma ascendente, el segundo parametro es el objetivo a buscar, y un limite inferior y superior
def binary_search(listss, target, lower_limit = None, upper_limit = None):
  # Marca el inicio de la lista
  if lower_limit is None:
    lower_limit = 0
    
    # Marca el final de la lista
  if upper_limit is None:
    upper_limit = len(listss) - 1
    
  # Aqui comprobamos que el rango de la lista es valido
  if upper_limit < lower_limit:
    return -1
  
  # Defino el punto medio de la lista como un numero entero
  middle_point = (lower_limit + upper_limit) // 2
  
  if listss[middle_point] == target:
    return middle_point
  elif target < listss[middle_point]:
    return binary_search(listss, target, lower_limit, middle_point - 1)
  else:
    return binary_search(listss, target, middle_point + 1, upper_limit)
  
  
if __name__ == '__main__':
  # Crear una lista ordenada de numeros
  size = 10000
  set_initial = set()
  
  while len(set_initial) < size:
    set_initial.add(random.randint(-3 * size, 3 * size))
    
  # my_list es una lista de numeros ordenados ascendentemente
  my_list_order_asc = sorted(list(set_initial))
  
  
# MEDICION DE TIEMPOS

# Busqueda sencilla
""" start_one = time.time()
for i in my_list_order_asc:
  naiev_search(my_list_order_asc, i)
end_one = time.time()
print(f"El tiempo de la busqueda sencilla es: {round(end_one - start_one)} segundos...") """

# Busqueda binaria
start_two = time.time()
for j in my_list_order_asc:
  binary_search(my_list_order_asc, j)
end_two = time.time()
print(f"El tiempo de la busqueda binaria es: {round(end_two - start_two)} segundos...")