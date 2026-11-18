import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json

def cargar_json():
    # Abre un diálogo de archivos filtrando únicamente por archivos .json
    ruta_archivo = filedialog.askopenfilename(
        title='Seleccionar archivo JSON de preguntas',
        filetypes=[('Archivos JSON', '*.json'), ('Todos los archivos', '*.*')]
    )
    
    if not ruta_archivo:
        return  # Si el usuario cancela, no hace nada

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)  # Carga el contenido del archivo JSON
            
            # Limpia los registros anteriores del Treeview
            for item in tree.get_children():
                tree.delete(item)
                
            # Inserta las preguntas del JSON en la tabla
            for q in datos:
                # Se asume que cada elemento tiene claves como 'texto', 'dificultad', 'tipo'
                tree.insert('', tk.END, values=(q.get('texto'), q.get('dificultad'), q.get('tipo')))
                
        messagebox.showinfo("Éxito", "Preguntas cargadas correctamente.")
    except Exception as e:
        # Maneja excepciones si el archivo está corrupto o no cumple con el formato esperado
        messagebox.showerror("Error", f"No se pudo procesar el archivo:\n{e}")

ventana = tk.Tk()
ventana.title("Cargar Preguntas desde JSON")
ventana.geometry('600x350')
ventana.config(bg='brown')

# Botón para activar el diálogo de apertura de archivo
tk.Button(ventana, text='Cargar Preguntas (JSON)', command=cargar_json, font=('Arial', 11)).pack(pady=10)

# Configuración del Treeview para mostrar las columnas de las preguntas
columnas = ('Texto', 'Dificultad', 'Tipo')
tree = ttk.Treeview(ventana, columns=columnas, show='headings')
tree.heading('Texto', text='Texto de la Pregunta')
tree.heading('Dificultad', text='Dificultad')
tree.heading('Tipo', text='Tipo')

tree.column('Texto', width=350, anchor='w')
tree.column('Dificultad', width=100, anchor='center')
tree.column('Tipo', width=100, anchor='center')

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

ventana.mainloop()