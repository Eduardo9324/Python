# Esto define la función arithmetic_arranger que toma una lista de problemas y un argumento booleano opcional result.
def arithmetic_arranger(problems, result = False):
  
  # Si la lista de problemas tiene más de 5 elementos, la función devuelve una cadena de caracteres que indica que hay demasiados problemas.
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # Esto define un diccionario ops que asocia los operadores + y - con funciones lambda que toman una lista de dos números y devuelven la suma o la diferencia de los números como una cadena de caracteres.
  ops = {
    '+': lambda pair: str(pair[0] + pair[1]),
    '-': lambda pair: str(pair[0] - pair[1]),
  }
  
  # Esto define cuatro listas vacías que se utilizarán para almacenar la parte superior, inferior y líneas de cada problema, así como los resultados si se incluyen.
  arranged_problems = []
  top = []
  bottom = []
  lines = []
  results = []
  
  # Esto comienza un ciclo for que itera sobre cada problema en la lista problems. El problema se divide en sus partes componentes y se encuentra la longitud máxima de cualquier parte.
  for problem in problems:
      chunks = problem.split()
      max_len = len(max(chunks, key=len))
    
    # Si cualquiera de las partes numéricas de un problema no es una cadena de dígitos, la función devuelve una cadena de caracteres que indica que los números deben contener solo dígitos.
      if not all([i.isnumeric() for i in chunks[::2]]):
        return "Error: Numbers must only contain digits."
    
    # Si el operador no es + o -, la función devuelve una cadena de caracteres que indica que el operador debe ser + o -.
      elif chunks[1] not in ops.keys():
        return "Error: Operator must be '+' or '-'."
    
    # Si cualquiera de los números en un problema tiene más de cuatro dígitos, la función devuelve una cadena de caracteres que indica que los números no pueden tener más de cuatro dígitos.
      elif max_len > 4:
        return "Error: Numbers cannot be more than four digits."
    
    # Aquí se calcula la longitud de línea necesaria para mostrar los números de manera alineada. Se crea una línea de caracteres '-' de esta longitud y se ajusta el primer número a la derecha de esta línea. El segundo número se escribe en una cadena formateada, con suficientes espacios para que los
      line_len = max_len + 2
      
      line = '-' * line_len  # 2 corresponds to the sign and space
      first_num = chunks[0].rjust(line_len, ' ')
      second_num = f"{chunks[1]}{' ' * (line_len - len(chunks[2]) - 1)}{chunks[2]}"

      top.append(first_num)
      bottom.append(second_num)
      lines.append(line)

      if result:
        res = ops[chunks[1]]([int(i) for i in chunks[::2]])
        results.append(f"{res.rjust(line_len, ' ')}")

  arranged_problems = '\n'.join(['    '.join(i)
    for i in (top, bottom, lines)])

  if results:
    arranged_problems += '\n' + '    '.join(results)

  return arranged_problems
    
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))