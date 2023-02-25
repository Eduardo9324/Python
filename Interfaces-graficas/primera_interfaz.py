""" Tkinter es una biblioteca de Python que permite crear interfaces gráficas de usuario (GUI) fácilmente. Es una de las bibliotecas más comunes para la creación de aplicaciones GUI en Python y se utiliza para crear ventanas, botones, menús y otras características de una interfaz de usuario. """
# Buena practica para importar modulos
import tkinter as tk

root = tk.Tk()

# Modificando la ventana
# Añade titulo
root.title("Ventana de prueba")


#Este metodo permite al usuario modificar el alto y/o ancho de la ventana con los parametros que recibe en True, si estan en False no se podra modificar la ventana, el primer argumento corresponde al ancho, y el segundo al alto
root.resizable(True, True)


# Modificando el icono de la ventana
root.iconbitmap()
""" es un método en Tkinter que permite establecer un icono para una ventana. El icono es un archivo en formato .ico o en otro formato compatible con Tkinter que se mostrará en la barra de título de la ventana y en cualquier otro lugar donde se muestre el icono de la aplicación.

El método root.iconbitmap() toma como argumento la ruta al archivo de icono: root.iconbitmap("icon.ico") """


# Este metodo modifica y tamaño que la ventana tiene por defecto
root.geometry("800x640")


root.config(bg="green") # es un método en Tkinter que permite modificar las propiedades de un widget.
""" El método config() toma uno o más pares clave-valor que representan las propiedades que se desean modificar y sus nuevos valores respectivos.

Es posible modificar cualquier propiedad soportada por el widget en cuestión. Algunas propiedades comunes incluyen el tamaño, la posición, el color, la fuente, el contenido y otros atributos visuales. """


# mainloop siempre debe ir al final
root.mainloop() # root.mainloop() es un método utilizado en la biblioteca tkinter de Python para mantener la ventana abierta y en funcionamiento hasta que el usuario la cierre. Por lo general, es la última línea de código en un programa tkinter y garantiza que todos los widgets y elementos de la ventana permanezcan visibles e interactivos hasta que el usuario decida cerrarla. (Mantiene escuchando los cambios que se van generando)