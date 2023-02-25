# pandas permite a python trabajar con analisis de datos
import pandas as pd
# matplotlib es una biblioteca para visualizacion de datos (creador de graficos)
import matplotlib.pyplot as plt
# seaborn se usa principalmente pra la visualizacion de datos estadisticos
import seaborn as sns

# Leer la informacion del archivo
df = pd.read_csv("Interfaces-graficas\Ej-info-muestra\sales.csv")
# Crea un grafico de lineas
sns.lineplot(x = "fecha", y = "ventas", data = df)
# Indica el punto mas alto
plt.plot("01-11", 95, "o")
# Muestra el grafico
plt.show()