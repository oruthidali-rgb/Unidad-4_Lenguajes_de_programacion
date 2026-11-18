import tkinter as tk #importa la libreria
def cambiar_texto():
    # Función que se ejecuta al presionar el botón; cambia el texto de la etiqueta
    label.config(text='¡Botón presionado!')
ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Ejercicio Etiqueta y Botón")  # Define el título de la ventana
ventana.geometry('400x200')  # Establece el tamaño de la ventana
label = tk.Label(ventana, text='Haz clic en el botón', font=('Arial', 12))  # Crea un widget Label (texto estático) asociado a la ventana
label.pack(pady=20)  # Coloca y empaqueta la etiqueta en la ventana con un margen vertical (pady)
boton = tk.Button(ventana, text='Cambiar', command=cambiar_texto)  # Crea un botón que al hacerle clic invoca la función cambiar_texto (sin paréntesis)
boton.pack()  # Coloca y empaqueta el botón en la ventana
ventana.mainloop()  # Mantiene la ventana abierta en un bucle de ejecución