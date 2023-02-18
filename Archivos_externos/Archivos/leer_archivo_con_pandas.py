import pandas as pd

""" import pandas importa la biblioteca de Python llamada Pandas. Pandas es una biblioteca de análisis de datos que proporciona estructuras de datos flexibles y herramientas para el análisis y la manipulación de datos.

Pandas es una biblioteca muy popular y ampliamente utilizada en la comunidad de análisis de datos y ciencia de datos de Python, y es una herramienta esencial para muchas tareas de análisis de datos.

Pandas proporciona dos estructuras de datos principales: Series y DataFrame. Una Series es una estructura de datos unidimensional que contiene una serie de valores con etiquetas o índices. Un DataFrame es una estructura de datos bidimensional que consiste en una colección de Series, donde cada Series representa una columna y las etiquetas o índices comparten una estructura común.

Además de estas estructuras de datos, Pandas proporciona una amplia gama de herramientas para la manipulación y análisis de datos, incluyendo funciones para la limpieza y preprocesamiento de datos, agregación y resumen de datos, manipulación de fechas y horas, y mucho más.

En resumen, Pandas es una biblioteca poderosa y versátil para el análisis de datos en Python, y es esencial para muchas tareas de análisis de datos y ciencia de datos. """


df = pd.read_csv("Archivos_externos\Archivos\info.csv")
# Muestra los datos de una sola columna
marcas = df["Marca"]
print(marcas)

# desendente
desendente = df.sort_values("Marca", ascending=False)
print(desendente)

# Tecnica de slackysin 
# el numero a la izquierda de los : indica desde donde inica y a la derecha indica donde termina (NO INCLUSIVO)
""" cadena = "0123456789"
print(cadena[2:8]) """

# accediendo al total de columna, esto retorna una tupla cuyo primer argumento es la cantidad de filas, y el segundo es la cantidad de columnas
filas_y_columnas_totales = df.shape
print(filas_y_columnas_totales)


# info estadistica
estadistica = df.describe()
print(estadistica)