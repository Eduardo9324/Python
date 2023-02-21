import random

def play():
  user = input("Escoge una opcion, 'pi' para piedra, 'pa' para papel o 'ti' para tijera; Tu eleccion aqui: \n ").lower()
  
  # Escoge al azar uno de los elementos de la lista
  pc = random.choice(["pi", "pa", "ti"])
  
  print(f"La computadora escogio '{pc}' ")
  print("================================================")
  
  if user == pc:
    return "uyy, empate !!!"
  
  
  if player_wins(user, pc):
    return "Bien, Ganaste !!!"
  return "jajaja, Perdiste, muy salado."


def player_wins(player, opponent):
  # Retorna True si gana el player
  # piedra gana a tijera (pi > ti)
  # tijera gana a papel (ti > pa)
  # papel gana a piedra (pa > pi)
  if ((player == "pi" and opponent == "ti") or (player == "ti" and opponent == "pa") or (player == "pa" and opponent == "pi")):
    return True
  else:
    return False
  
  
print(play())