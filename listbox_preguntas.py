import tkinter as tk  # Importa la librería tkinter

def mostrar_seleccion(event):
    # Función que captura el evento de selección en la lista
    seleccion = listbox.curselection()  # Obtiene la tupla con el índice del elemento seleccionado
    if seleccion: 
        indice = seleccion[0]  # Extrae el índice numérico
        pregunta_texto = listbox.get(indice)  # Obtiene el texto correspondiente a ese índice en el Listbox
        label_pregunta.config(text=pregunta_texto)  # Muestra la pregunta seleccionada en la etiqueta grande

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Listbox de Preguntas")  # Define el título
ventana.geometry('400x300')  # Establece las dimensiones

label_pregunta = tk.Label(ventana, text='Selecciona una pregunta', font=('Arial', 12, 'bold'), wraplength=350)
label_pregunta.pack(pady=20)  # Crea y empaqueta la etiqueta grande

listbox = tk.Listbox(ventana, font=('Arial', 11), width=45, height=5)  # Crea el widget Listbox
preguntas = [
    '¿Cuál es la capital de Francia?',
    '¿Cuánto es 2 + 2?',
    '¿Cuál es el lenguaje de programación principal en este curso?',
    '¿Qué significa GUI?',
    '¿Qué extensión usa una base de datos de SQLite?'
]

for p in preguntas:
    listbox.insert(tk.END, p)  # Inserta cada pregunta al final (tk.END) del Listbox

listbox.pack(pady=10)  # Empaqueta el Listbox en la ventana
listbox.bind('<<ListboxSelect>>', mostrar_seleccion)  # Vincula el evento de selección de la lista con la función mostrar_seleccion

ventana.mainloop()  # Inicia el bucle de eventos