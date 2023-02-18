# 1
""" words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split() # Lista con cada palabra
parts = pieces[3].split('-')
n = parts[1]

print(parts) """

# 2
""" dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13 # reemplaza
dict["Sat"] = 2 # añade
dict["Sun"] = 9 # reemplaza

print(dict) """

# 3
""" counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0)) """
""" La función get en Python recibe dos argumentos:

key: La clave para la cual se desea recuperar el valor en el diccionario.

default (opcional): El valor por defecto que se devolverá si la clave no existe en el diccionario. Si no se especifica un valor por defecto, se devolverá None.
"""
# 4
""" counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key]) """
        
# 5
""" d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i) """
    
# 6
""" lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst) """

""" El método sorted en Python es una función built-in que permite ordenar cualquier secuencia (listas, tuplas, etc.) o colección de objetos. La función devuelve una nueva lista con los elementos ordenados.

El método sorted recibe un solo argumento, que es la secuencia o colección que se desea ordenar. Opcionalmente, se pueden especificar varios argumentos adicionales para controlar el orden de los elementos:

key: Una función que se utiliza para obtener el valor a partir del elemento que se desea ordenar.

reverse: Un valor booleano que indica si se debe ordenar en orden ascendente o descendente. Si reverse es True, los elementos se ordenarán en orden descendente; si es False (por defecto), los elementos se ordenarán en orden ascendente. """


# 7
# import re 

""" import re es una instrucción de Python que importa el módulo de expresiones regulares (regular expressions) llamado re. Este módulo proporciona herramientas para trabajar con expresiones regulares, que son patrones utilizados para buscar y manipular cadenas de texto.

Las expresiones regulares son muy útiles para tareas como la validación de direcciones de correo electrónico, la búsqueda y reemplazo de texto, y la identificación de patrones en datos. El módulo re de Python proporciona una variedad de funciones que permiten trabajar con expresiones regulares de manera sencilla y eficiente. """

""" s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst) """

# 8
""" import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close() """


# 9 
# import urllib.request
""" Esta biblioteca es parte de la biblioteca estándar de Python y proporciona una interfaz para interactuar con recursos web, como páginas web y archivos en línea. """

""" fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) """
    
""" fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt'): Esta línea abre una conexión con el archivo de texto "romeo.txt" ubicado en la dirección web "http://data.pr4e.org/romeo.txt" utilizando la función urllib.request.urlopen() de la biblioteca "urllib.request". El resultado de la función se almacena en la variable fhand.

for line in fhand:: Esta línea crea un bucle "for" que recorre cada línea del contenido del archivo "romeo.txt" que se ha almacenado en la variable fhand. En cada iteración, la variable "line" almacena una línea del archivo.

print(line.decode().strip()): Esta línea imprime cada línea del archivo en la consola del programa. Primero, utiliza el método decode() para convertir la línea de bytes que se ha leído a una cadena de caracteres, y luego utiliza el método strip() para eliminar los caracteres en blanco, como saltos de línea, que se encuentran al final de la línea.

En resumen, este código descarga un archivo de texto en línea, recorre cada línea del archivo y muestra su contenido en la consola. """

# 10
""" La biblioteca de Python que se utiliza comúnmente para analizar documentos HTML y extraer datos de ellos es "BeautifulSoup". Esta biblioteca proporciona herramientas para analizar documentos HTML y XML, y permite a los programadores buscar, navegar y manipular la estructura de estos documentos.

Con BeautifulSoup, es posible encontrar y extraer contenido específico de un documento HTML, como títulos, párrafos, tablas, imágenes, enlaces y otros elementos. La biblioteca también admite el uso de expresiones regulares y funciones de Python para realizar búsquedas más complejas.

Para utilizar BeautifulSoup, es necesario instalar la biblioteca en el entorno de desarrollo Python utilizando un administrador de paquetes, como "pip". A continuación, se debe importar la biblioteca en el código Python y utilizar las funciones y métodos proporcionados por la biblioteca para analizar y manipular documentos HTML.

En resumen, la biblioteca "BeautifulSoup" es una herramienta muy útil para analizar documentos HTML y extraer datos de ellos en Python. """


# 11
# import json
""" "import json" es una declaración de importación en Python que permite a un programa acceder a la biblioteca "json". Esta biblioteca proporciona herramientas para codificar y decodificar datos en formato JSON (JavaScript Object Notation).

El formato JSON se utiliza comúnmente para intercambiar datos entre aplicaciones en la web. Es un formato de texto que utiliza una sintaxis similar a la de los objetos en JavaScript y permite representar datos estructurados como listas, diccionarios y cadenas de caracteres.

La biblioteca "json" de Python permite a un programa convertir datos de Python en formato JSON y viceversa. Por ejemplo, se puede utilizar para convertir un objeto Python en una cadena de texto en formato JSON, o para convertir una cadena de texto en formato JSON en un objeto Python.

En resumen, "import json" es una forma de importar y acceder a la biblioteca "json" en un programa Python, lo que permite a dicho programa trabajar con datos en formato JSON. """

# La lista debe ser un string para poder ser leido

""" data = [{ "id" : "001", "x" : "2", "name" : "Quincy"}, { "id" : "009", "x" : "7", "name" : "Mrugesh"}]

info = json.loads(data)
print(info[1]['name']) """


# 12
""" class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party() """


# 13
""" class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party() """


# 14
""" Una clave foránea, también conocida como clave externa, es un tipo de restricción utilizada en las bases de datos relacionales para establecer una relación entre dos tablas.

En una base de datos relacional, las tablas están diseñadas para almacenar diferentes tipos de datos y se relacionan entre sí a través de columnas comunes. Una clave foránea es una columna o conjunto de columnas en una tabla que hace referencia a la clave primaria de otra tabla en la base de datos.

En otras palabras, la clave foránea es una columna en una tabla que establece una relación con otra tabla en la base de datos. Esta relación se basa en la coincidencia de los valores de la columna de clave foránea con los valores de la columna de clave primaria en la otra tabla.

La clave foránea se utiliza para garantizar la integridad referencial de la base de datos, lo que significa que se asegura de que los datos relacionados estén correctamente vinculados entre sí. Por ejemplo, si una tabla de "pedidos" tiene una clave foránea que se refiere a la tabla de "clientes", la clave foránea garantiza que solo se puedan agregar pedidos para clientes que ya existen en la tabla de "clientes".

En resumen, una clave foránea es una columna en una tabla que se utiliza para establecer una relación con otra tabla en la base de datos. Se utiliza para garantizar la integridad referencial de la base de datos y para garantizar que los datos relacionados estén correctamente vinculados entre sí. """


# 15
