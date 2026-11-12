import _sqlite3
import tkinter as tk
ventana=tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x300") 
ventana.configure(bg='lightgray')
def cambiar_texto():
    etiqueta.config(text="¡Botón presionado!")
etiqueta = tk.Label(text="¡Haz clic en el botón!")
etiqueta.pack()
boton = tk.Button(text="Cambiar", command=cambiar_texto)
boton.pack()
tk.mainloop()