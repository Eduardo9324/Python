# El argumento "w" es el argumento de escritura, si no encuentra el archivo, lo crea
with open("Archivos_externos\Archivos\conversacion.txt", "w", encoding="UTF-8") as archivo:
  # Aqui sobre escribe el archivo
  #archivo.write("Holaa tu")
  
  # Aqui se debe pasar una lista con todas las lineas que se van a incluir en el archivo, \n es un salto de linea
  archivo.writelines(["Hola tu, como vas ?", " \n", "sisisi"])
  # Si se usan dos o mas "writelines", va agregando linea por linea al archivo