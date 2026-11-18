#ranking_treeview
#Este programa muestra puntuaciones y los organiza en un top de mejores puntuaciones
#Idali
#15/11/26
import tkinter as tk  # Importa la librería tkinter
from tkinter import ttk  # Importa ttk para acceder al widget Treeview (tablas)

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Ranking - Treeview")
ventana.geometry('450x250')
ventana.config(bg='lightblue')

# Define las columnas del Treeview
columnas = ('Posición', 'Jugador', 'Puntaje')
tree = ttk.Treeview(ventana, columns=columnas, show='headings')  # show='headings' oculta la columna técnica inicial vacía

# Configura los encabezados de las columnas
tree.heading('Posición', text='Posición')
tree.heading('Jugador', text='Jugador')
tree.heading('Puntaje', text='Puntaje')

# Ajusta el ancho de las columnas de la tabla
tree.column('Posición', width=80, anchor='center')
tree.column('Jugador', width=200, anchor='w')
tree.column('Puntaje', width=100, anchor='center')

# Datos de ejemplo (hardcodeados) a insertar en la tabla
registros = [
    (1, 'Ana', 150),
    (2, 'Carlos', 120),
    (3, 'Sofía', 95),
    (4, 'Luis', 80),
    (5, 'Elena', 60)
]

# Inserta los registros fila por fila en el Treeview
for reg in registros:
    tree.insert('', tk.END, values=reg)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Empaqueta y expande el Treeview en la ventana

ventana.mainloop()  # Inicia el bucle principal