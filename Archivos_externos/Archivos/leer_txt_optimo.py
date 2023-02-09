# Sintaxis para asignar el archivo a una variable
with open("Archivos_externos\Archivos\conversacion.txt", encoding="UTF-8") as archivo:
  # Este codigo solo se ejecuta si el archivo se abrio correctamente y despues se cierra
  print(archivo.read())
  
  
""" with open() es una estructura de control en Python que se utiliza para abrir y manipular archivos. Esta estructura es especialmente útil porque garantiza que el archivo se cierre correctamente, incluso si ocurre una excepción durante la manipulación del archivo. """

""" with open(filename, mode) as file:
    # manipulate file """
    
""" Donde filename es el nombre del archivo y mode es el modo en el que se abrirá el archivo (lectura, escritura, añadir, etc.). Por ejemplo, si quieres abrir un archivo para lectura, puedes hacer lo siguiente: """

""" with open("example.txt", "r") as file:
    content = file.read()
    print(content) """

""" Una vez que termina el bloque with, el archivo se cierra automáticamente, sin importar si todo fue bien o hubo algún error durante la manipulación del archivo. Esto es útil para evitar errores de memoria y otros problemas relacionados con el manejo de archivos. """
