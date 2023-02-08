# Funsiones con parametros por defecto
def frase(nombre = "eduardo", apellido = "toro", adjetivo = "linda"):
  return f"{nombre} {apellido}, eres muy {adjetivo}."

frase_resultado = frase("marcela", "castro")
print(frase_resultado)