import random


def guess_the_number_pc(x):
  
  print("================================================")
  print("            Bienvenido(a) al juego!             ")
  print("================================================")
  print(f"Selecciona un numero entre 1 y {x} para que el PC lo adivine...")
  print("================================================")
  
  try:
    lower_limit = 1
    upper_limit = x
    answer = ""
    
    while answer != "c":
    # Generar una prediccion
      if lower_limit != upper_limit:
        prediction = random.randint(lower_limit, upper_limit)
      else:
        prediction = lower_limit # Tambien podria ser upper_limit ya que en este caso serian iguales
      
    # Obtener respuesta por parte del usuario
      answer = input(f"Mi prediccion es {prediction}; Si es muy alta ingresa (A). Si es muy baja ingresa (B). Si es correcto ingresa (C; Tu respuesta aqui: ").lower()
    
      if answer == "a":
        upper_limit = prediction - 1
      # Ej: Intervalo inicia: [1, 10]
      # prediction: 6
      # answer: "a", el usuario indica que es muy alto
      # nuevo intervalo: [1, 5]
      elif answer == "b":
        lower_limit = prediction + 1
      # Ej: Intervalo inicia: [1, 10]
      # prediction: 6
      # answer: "a", el usuario indica que es muy alto
      # nuevo intervalo: [7, 10]
  except ValueError as e:
    print("Ocurrio un error", e)
      
  print(f"Genial !!!, El PC adivino tu numero correctamente, era {prediction}")
  
  
guess_the_number_pc(2000)