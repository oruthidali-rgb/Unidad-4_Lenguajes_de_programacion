#caja_texto
#Este programa permite al usuario escribir una linea de texto en una caja y se muestra.
#Idali
#06/11/26
import tkinter as tk  # Importa la librería tkinter

def mostrar_texto():
    # Función que recupera el texto ingresado en el Entry y lo coloca en la Label
    texto = entrada.get()  # Obtiene el valor actual escrito dentro de la caja de texto
    etiqueta_resultado.config(text=texto)  # Actualiza la propiedad 'text' de la etiqueta con el valor obtenido

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Ejercicio Caja de Texto")  # Define el título
ventana.geometry('400x300')  # Define el tamaño de la ventana

entrada = tk.Entry(ventana, font=('Arial', 12))  # Crea una caja de texto de una sola línea (Entry)
entrada.pack(pady=15)  # Muestra el Entry en la ventana con un espacio vertical

boton_mostrar = tk.Button(ventana, text='Mostrar', command=mostrar_texto)  # Crea el botón vinculado a la función mostrar_texto
boton_mostrar.pack(pady=5)  # Muestra el botón en la ventana

etiqueta_resultado = tk.Label(ventana, text='', font=('Arial', 12))  # Crea una etiqueta vacía inicialmente para mostrar el resultado
etiqueta_resultado.pack(pady=15)  # Muestra la etiqueta de resultado

ventana.mainloop()  # Inicia el bucle principal de la aplicación