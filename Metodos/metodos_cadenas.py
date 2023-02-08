#Convierte a mayusculas
nombre = "cristian toro"
print(nombre.upper())

#Convierte a minusculas
name_two = "MARIA,TORO,hola,como,estas,?"
print(name_two.lower())

#Primera letra en mayuscula, el resto de la palabra queda en minusculas
cosa = "pUERTA"
print(cosa.capitalize())

#Buscar una cadena dentro de otra cadena y me devuelve en indice de su pocision, si no lo encuentra devuelve -1
busqueda = name_two.find("o")
print(busqueda)

#Busca una cadena dentro de otra y me devuelve en indice de su pocision, si no encuentra nada devuelve un error, se produce una eception
busqueda_in = name_two.index("o")
print(busqueda_in)


#Comprueba que todos los caracteres de la cadena sean digitos (NUMEROS) devuelve True, si no devuelve False, verifica numeros en forma de texto
algo = "6524008792136588510"
es_numero = algo.isnumeric()
print(es_numero)


#Comprueba si es alfabetico (SOLO LETRAS DE LA A - Z SIN ESPACIOS), devuelve True, si no False
alafanum = algo.isalpha()
print(alafanum)


#Busca una cadena dentro de otra, devuelve la cantidad de veces que encuentra en elemento, si no lo encuentra devuelve 0
#count() es un método de cadena en Python que devuelve el número de ocurrencias de una subcadena especificada en la cadena.
contar_coincidencias = name_two.count("co")
print(contar_coincidencias)

text = "hello world"
print(text.count("l")) # 3
print(text.count("z")) # 0



#Cuenta la cantidad de caracteres (longitud)
contar_caracteres = len(name_two)
print(contar_caracteres)


#Verifica si una cadena empieza con otra cadena dada, devuelve True, si no devuelve False, se puede verificar con solo una letra o una palabra entera
#es un método de cadena en Python que devuelve True si una cadena comienza con un prefijo específico; de lo contrario, devuelve False.
empieza_con = name_two.startswith("MA")
print(empieza_con)

text = "hello world"
print(text.startswith("hello")) # True
print(text.startswith("world")) # False



#Verifica si una cadena termina con otra cadena dada, devuelve True, si no devuelve False, se puede verificar con solo una letra o una palabra entera
#es un método de cadena en Python que devuelve True si una cadena termina con un sufijo especificado, de lo contrario devuelve False.
termina_con = name_two.endswith(" ?")
print(termina_con)

text = "hello world"
print(text.endswith("world")) # True
print(text.endswith("hello")) # False



#Reemplaza un pedazo de una cadena dada por otro, el primer parametro es el antiguo y el segundo es el nuevo
#replace() es un método de cadena en Python que reemplaza todas las apariciones de una subcadena especificada en la cadena con otra cadena especificada.
cadena_nueva = name_two.replace("MAR", "EUGENIA")
print(cadena_nueva)

text = "hello world"
print(text.replace("l", "x")) # 'hexxo worxd'



#Separa una cadena con lo que le pasemos, este metodo crea una lista
#split() es un método de cadena en Python que divide una cadena en una lista de subcadenas en función de un delimitador específico. Si no se especifica el delimitador, divide la cadena en espacios en blanco de forma predeterminada.
cadena_separada = name_two.split("-")
print(cadena_separada)

text = "hello world"
print(text.split()) # ['hello', 'world']
text = "apple,banana,cherry"
print(text.split(",")) # ['apple', 'banana', 'cherry']



#es una función integrada de Python que devuelve True si todos los caracteres de una cadena son dígitos; de lo contrario, devuelve False.
nums = "65455"
comprueba = nums.isdigit()
print(comprueba)

nnn = "6921"
print(nnn.isdigit())

#La diferencia entre isnumeric() e isdigit() es que isnumeric() devuelve True si todos los caracteres de una cadena son caracteres numéricos, incluidos los de otros sistemas de escritura (por ejemplo, números arábigos hindúes, números romanos, etc.), mientras que isdigit () devuelve True solo si todos los caracteres de una cadena son dígitos ASCII.


#Busca en indice de un caracter contando desde el final de la canena
text = "hola, me llamo eduardo y quiero triunfar"
hacia_atras = text.rfind("o")
print(hacia_atras)


#Borra los espacion sobrantes al principio y final de la cadena
text_2 = "       Era una tarde llena de sol, y yo camniba con una canasta de naranjas por la calle        "
borra_espacios = text_2.strip()
print(borra_espacios)


#Comprueba si es alfanumerico (SOLO LETRAS Y NUMEROS SIN ESPACIOS NI CARACTERES ESPECIALES)
alfa = "vknenvoernv65478kknjv235d8g4f8d5s6d4f1g5f8d2HSND5885UR"
alfa_num = alfa.isalnum()
print(alfa_num)