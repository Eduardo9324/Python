# Este modulo permite trabajar con procesos aleatorios
import random
# El modulo string tiene funsiones y/o metodos para trabajar con cadenas de caracteres
import string

from words import words
from diagrama import vidas_diccionario_visual


# Este código es una función que toma una lista de palabras (wor) y selecciona aleatoriamente una de las palabras. El bucle while comprueba si la palabra seleccionada al azar contiene alguno de los caracteres "-", " " o ".". Si lo hace, seleccionará otra palabra de la lista hasta que encuentre una sin esos caracteres. Finalmente, devuelve la palabra en mayúsculas.
def get_valid_word(wor):
  # Selecciona una palabra random de la lista
  word = random.choice(wor)
  
  while "-" in word or " " in word or "." in word:
    word = random.choice(wor)
  return word.upper()


def hanged():
  
  print("================================================")
  print("      Bienvenido(a) al juego del ahorcado       ")
  print("================================================")
  
  word = get_valid_word(words)
  
  # Crea un conjunto con las letras de la palabra
  letters_to_guess = set(word)
  # Crea un conjunto vacio
  guessed_letters = set()
  # Esta linia da acceso a todas las letras de abecedario en mayuscula (no incluye la ñ)
  alphabet = set(string.ascii_uppercase)
  
  lives = 7
  
  while len(letters_to_guess) > 0 and lives > 0:
    print(f"Te quedan {lives} vidas, y has usado estas letras: {' '.join(guessed_letters)} ") #muestra las letras separadas por un espacio 
    
    # Mostrar el estado actual de la palabra
    word_list = [letter if letter in guessed_letters else '-' for letter in word]
    # Muestra estado del ahorcado
    print(vidas_diccionario_visual[lives])
    # Muestra letras separadas por espacio
    print(f"Palabra: {' '.join(word_list)}")
    
    
    letter_user = input("Escoge una letra: ").upper()
    
    # Si la letra escogida por el usuario esta en el abecedario y no estan en el conjunto de letras adivinadas, se añade la trea al conjunto de letras adivinadas
    # Si se restan conjuntos se quitan elementos del conjunto
    if letter_user in alphabet - guessed_letters:
      guessed_letters.add(letter_user)
      
      # La letra esta en la palabra ?
      # si: quita la ltra del conjunto de letras pendientes por adivinar, de lo contrario pierde una vida
      if letter_user in letters_to_guess:
        letters_to_guess.remove(letter_user)
        print("")
      else:
        lives -= 1
        print(f"\nTu letra, {letter_user}, no esta en la palabra")
    # Si la letra escogida por el usuario ya fue ingresada
    elif letter_user in guessed_letters:
      print("\nYa escogiste esa letra, por favor escoge otra")
    else:
      print("\nEsta letra no es valida !!! ")
      
  # Cuando se adivinan todas las letras o cuando se agotan las vidas
  if lives == 0:
    print(vidas_diccionario_visual[lives])
    print(f"Ahorcado !!!, perdiste, la palabra era: '{word}'")
  else:
    print(f"Genial, adivinaste la palabra: {word}; Ganaste !!!")
    
    
hanged()