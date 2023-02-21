
def arithmetic_arranger(problems, solve=False):
    # Verificar que no hay más de 5 problemas
    if len(problems) > 5:
      return "Error: Too many problems."

    # Inicializar las listas para los operandos y operadores
    first_operands = []
    second_operands = []
    operators = []
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # Separar cada problema en sus componentes y verificar que estén bien formados
    for problem in problems:
      components = problem.split()
      if components[1] != "+" and components[1] != "-":
        return "Error: Operator must be '+' or '-'."
      try:
        first_operand = int(components[0])
        second_operand = int(components[2])
      except ValueError:
        return "Error: Numbers must only contain digits."
      if len(str(first_operand)) > 4 or len(str(second_operand)) > 4:
        return "Error: Numbers cannot be more than four digits."
      first_operands.append(str(first_operand))
      second_operands.append(str(second_operand))
      operators.append(components[1])

    # Construir las líneas del arreglo
    for i in range(len(problems)):
        # Calcular el resultado si se solicita
        if solve:
          if operators[i] == "+":
            result = int(first_operands[i]) + int(second_operands[i])
          else:
            result = int(first_operands[i]) - int(second_operands[i])
          result_str = str(result)
          width = max(len(first_operands[i]), len(second_operands[i]), len(result_str))
        else:
          width = max(len(first_operands[i]), len(second_operands[i]))
        line1 += first_operands[i].rjust(width + 2) + "    "
        line2 += operators[i] + " " + second_operands[i].rjust(width) + "    "
        line3 += "-" * (width + 2) + "    "
        if solve:
          line4 += result_str.rjust(width + 2) + "    "

    # Combinar las líneas en un solo string
    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if solve:
      arranged_problems += "\n" + line4.rstrip()

    return arranged_problems
