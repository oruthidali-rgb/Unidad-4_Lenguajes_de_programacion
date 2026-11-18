#calculadora_suma
#Este programa solicita dos numeros y los suma
#Idali
#09/11/26
import tkinter as tk  # Importa la librería tkinter
from tkinter import messagebox  # Importa messagebox para mostrar alertas emergentes en caso de error

def sumar():
    try:
        # Intenta convertir los valores de las cajas de texto a números de tipo float
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        suma = num1 + num2  # Realiza la operación matemática de suma
        label_resultado.config(text=f"Resultado: {suma}")  # Muestra el resultado formateado en la etiqueta
    except ValueError:
        # Maneja la excepción si el usuario ingresa letras u otros caracteres no numéricos
        messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Calculadora de Suma")  # Define el título
ventana.geometry('400x300')  # Establece las dimensiones de la ventana

entrada1 = tk.Entry(ventana, font=('Arial', 11))  # Crea la primera caja de texto para el número 1
entrada1.pack(pady=10)  # Empaqueta la primera caja de texto

entrada2 = tk.Entry(ventana, font=('Arial', 11))  # Crea la segunda caja de texto para el número 2
entrada2.pack(pady=10)  # Empaqueta la segunda caja de texto

boton_sumar = tk.Button(ventana, text='Sumar', command=sumar)  # Crea el botón que ejecuta la función 'sumar'
boton_sumar.pack(pady=5)  # Empaqueta el botón

label_resultado = tk.Label(ventana, text='Resultado: ', font=('Arial', 12))  # Crea la etiqueta para mostrar la suma
label_resultado.pack(pady=10)  # Empaqueta la etiqueta de resultado

ventana.mainloop()  # Inicia el bucle principal de la GUI