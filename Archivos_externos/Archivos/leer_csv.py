# Leer archivo .csv
import csv

""" import csv importa el módulo csv en Python. El módulo csv es un módulo incorporado de Python que proporciona funcionalidad para leer y escribir archivos en formato CSV (Comma-Separated Values).

El formato CSV es un formato de intercambio de datos simple y ampliamente utilizado que consiste en una serie de líneas, donde cada línea es un registro y los valores en cada línea están separados por comas. Estos archivos son fácilmente legibles por personas y se pueden abrir y modificar en programas de hojas de cálculo como Microsoft Excel o Google Sheets.

El módulo csv proporciona dos objetos principales para trabajar con archivos CSV: reader y writer. El objeto reader se utiliza para leer archivos CSV y proporciona una manera fácil de acceder a los valores en cada línea. El objeto writer se utiliza para escribir datos en un archivo CSV y automáticamente separa los valores en líneas y las líneas en el archivo.

En resumen, el módulo csv es una herramienta útil para trabajar con archivos CSV en Python, y es fácil de usar para tareas como leer y escribir archivos CSV y acceder a los datos en ellos. """

with open("Archivos_externos\Archivos\info.csv", "r", encoding="UTF-8") as archivo:
  # Esto se puede recorrer como un iterable
  reader = csv.reader(archivo)
  for i in reader:
    print(i)