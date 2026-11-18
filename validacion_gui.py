#validacion_gui
#Este programa valida que los datos solicitados cumplan ciertos requerimientos
#Idali
#16/11/26
import tkinter as tk  # Importa la librería tkinter
from tkinter import messagebox  # Importa messagebox para reportar errores o éxitos

def validar_y_guardar():
    nombre = entry_nombre.get().strip()
    edad_str = entry_edad.get().strip()
    correo = entry_correo.get().strip()

    # Validación 1: El nombre no puede estar vacío
    if not nombre:
        messagebox.showerror("Error de Validación", "El campo 'Nombre' no puede estar vacío.")
        return

    # Validación 2: La edad debe ser un número entero entre 1 y 120
    try:
        edad = int(edad_str)
        if not (1 <= edad <= 120):
            raise ValueError()
    except ValueError:
        messagebox.showerror("Error de Validación", "La 'Edad' debe ser un número entero válido entre 1 y 120.")
        return

    # Validación 3: El correo debe contener '@'
    if '@' not in correo:
        messagebox.showerror("Error de Validación", "El 'Correo' electrónico debe contener el carácter '@'.")
        return

    # Si pasa todas las validaciones, muestra un mensaje de éxito
    messagebox.showinfo("Éxito", "¡Datos validados y guardados correctamente!")

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Formulario con Validaciones")
ventana.config(bg='lightgreen')

# Construcción de la interfaz con grid (similar al Ejercicio 5)
tk.Label(ventana, text='Nombre').grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text='Edad').grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text='Correo').grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=2, column=1, padx=10, pady=10)

tk.Button(ventana, text='Guardar', command=validar_y_guardar).grid(row=3, column=1, pady=15, sticky='e')

ventana.mainloop()  # Inicia el bucle de la aplicación