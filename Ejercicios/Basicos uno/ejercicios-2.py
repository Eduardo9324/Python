#EJERCICIO 2
#Calculo tiempo y cantidad de palabras dichas

frase = input("Escribe una frase, y yo calculo cuantas palabras son y cuanto tiempo tardarias diciendola: ")

palabras_separadas = frase.split(" ")

total_palabras = len(palabras_separadas)
if total_palabras > 120:
  print("Papi calmao !!!")

print(f"Dijiste {total_palabras}, y tardarias {total_palabras / 2} segundos en decirlas.")

print("----------------------------------------------------------")

print(f"Esas {total_palabras} palabras, Dalto las diria en {(total_palabras * 100 // 2) * 0.3 / 100} segundos.")

