#Solicitando un numero
#con la funcion "int" convierto a entero el numero que recibo del usuario en el input
""" numero_entero = int(input("Ingresa tu numero de telefono: "))
print(f"Te llamare al {numero_entero}") """

#Aqui convierto a numero flotante (DECIMAL) el numero que me pasan por el input
numero_flotante = float(input("Ingresa un numero entre 1 y 100: "))
if numero_flotante < 1 or numero_flotante > 100:
  print("El numero es invalido :(")
else:
  print(f"el numero sera: {numero_flotante * 7.2}")

