#Importo funcionalidad para poder abrir y/o manipular  un archivo externo
from io import open

#Creando archivo externo, el metodo "open" pide dos argumentos, el primero es el nombre del archivo que queremos abrir, y el segundo es el modo en el que lo vamos a abrir, Ej: modo lectura, escritura, modo append (para agregar info a un archivo que ya existe)

""" #Aqui crea un archivo .txt de escritura
archivo_externo = open("archivo.txt", "w")

#Frase que se va a incluir en el archivo externo
frase = "Es un gran dia para estudiar python \n el miercoles"

#Incluyendo frase en el archivo externo
archivo_externo.write(frase)

#Se procede a cerra el archivo externo
archivo_externo.close() """

#Ej para modo lectura de archivos externos

""" archivo_externo = open("archivo.txt", "r") """

""" #Aqui lo que hace es leer lo que hay en el archivo y lo almacena en la variable "texto"
texto = archivo_externo.read()

#Cierra el archivo
archivo_externo.close()
#Me muestra en pantalla la lectura del archivo incluso despues de cerrarlo, porque esta almacenada en la variable "texto"
print(texto) """


#Para leer un texto linea por linea y generar una lista con las palabras
#Esta linea convierte la variable "lineas_texto" en una lista manipulable
""" lineas_texto = archivo_externo.readlines()
archivo_externo.close()
print(lineas_texto) """

#Esta linea abre el archivo en modo append para añregar indo 
archivo_externo = open("archivo.txt", "r")

archivo_externo.read("\n siempre es una buena ocacion para estudiar python ")

archivo_externo.close()


