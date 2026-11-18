#layout_grid
#Este programa solicita datos principales como nombre,edad y correo. Al guardarlos muestra una ventana
#Idali
#14/11/26
import tkinter as tk 
from tkinter import messagebox 
ventana = tk.Tk() 
ventana.title("LayoutGrid")
ventana.geometry("400x300")
ventana.configure(bg='lightgray')

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    messagebox.showinfo("Datos guardados correctamente", f"Nombre: {nombre}\nEdad: {edad}\nCorreo: {correo}")

entry_nombre = tk.Entry(ventana)
entry_edad = tk.Entry(ventana)
entry_correo = tk.Entry(ventana)
label_nombre = tk.Label(ventana, text="Nombre:")
label_edad = tk.Label(ventana, text="Edad:")
label_correo = tk.Label(ventana, text="Correo:")
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
    
label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)
label_edad.grid(row=1, column=0)
entry_edad.grid(row=1, column=1)
label_correo.grid(row=2, column=0)
entry_correo.grid(row=2, column=1)
boton_guardar.grid(row=3, column=1)

ventana.mainloop()
