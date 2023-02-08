#EJERCICIO 1
#ejercicio A

#Tiempos de cursos
otros_cursos_max = 7
otros_cursos_min = 2.5
otros_cursos_promedio = 4
curso_de_dalto = 1.5

# FORMULA CALCULO DE DIFERENCIAS DE PORCENTAJES

#Multiplicar por 1000 y despues dividir entre 10 es una manera de mover la , de los numeros decimales, y en la medida que se agregan "0" la "," se sigue corriendo

#min
#El primer numero 100 se indica para que me de la diferencia de porcentaje en numero positivo
diferencia_con_min = 100 - (curso_de_dalto * 1000 // otros_cursos_min / 10)
print(f"El curso de dalto dura un {diferencia_con_min} % menos que el cuso mas corto.")

#max
diferencia_con_max = 100 - (curso_de_dalto * 10000 // otros_cursos_max / 100)
print(f"El curso de dalto dura un {diferencia_con_max} % menos que el cuso mas largo.")

#promedio
diferencia_con_promedio = 100 - (curso_de_dalto * 1000 // otros_cursos_promedio / 10)
print(f"El curso de dalto dura un {diferencia_con_promedio} % menos que el cuso promedio.")

print("-----------------------------------------------------")


#EJERCICIO B
#Duracion cursos sin editar - TIEMPO REAL DE GRABACION 
sin_edicion_promedio = 5
sin_edicion_dalto = 3.5
#Calculando tiempo removido
promedio_tiempo_vacio = 100 - (otros_cursos_promedio * 1000 // sin_edicion_promedio / 10)
promedio_tiempo_dalto = 100 - (curso_de_dalto * 1000 // sin_edicion_dalto / 10)

print(f"Un curso promedio elimina un {promedio_tiempo_vacio} % de tiempo total de grabacion.")
print(f"Este curso elimina un {promedio_tiempo_dalto} % de tiempo total de grabacion.")
print("--------------------------------------")

#EJERCICIO C
#Mostrando diferencias si los cursos duraran 10 horas 
print(f"Ver 10 horas de este curso equivale a {otros_cursos_promedio * 100 // curso_de_dalto / 10} horas de otros cursos")

print(f"Ver 10 horas de otros cursos equivale a {curso_de_dalto * 1000 // otros_cursos_promedio / 10} horas del curso de dalto")