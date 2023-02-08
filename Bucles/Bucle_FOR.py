#SINTAXIS
# for "variable" in "elemento a recorrer":
     #cuerpo del bucle

#Range me imprime una secuencia consecutiva partiendo por defecto desde "0", el primer argumento que puedo pasar el el numero desde donde inicia la secuencia, el segundo es hata donde ira la secuenca pero no es incluido (VA HASTA UNO ANTES), y el tercer argumento es es el tamaño del incremento (por defecto es 1)
nums = ["cristian", "juan"]
for i in range(2, 13, 2):
  print(i)
  
""" validate = False

#def mailValidation(mail):
mail = input("Ingresa tu correo:")

for i in range(len(mail)):
  if mail[i] == "@":
    validate = True
    
if validate:
  print("mail valido")
else:
  print("mail no valido")

#mailValidation() """


#Por defecto los elementos iterables son las listas, las tuplas
#Tambien se pueden iterar los strings, los diccionarios, los conjuntos