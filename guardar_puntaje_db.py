import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# --- Módulo Backend / Base de Datos ---
def inicializar_db():
    conn = sqlite3.connect('juego.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS puntajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jugador TEXT,
            puntaje INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def guardar_puntaje(nombre, puntaje):
    conn = sqlite3.connect('juego.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO puntajes (jugador, puntaje) VALUES (?, ?)', (nombre, puntaje))
    conn.commit()
    conn.close()

def obtener_top5():
    # Consulta los 5 mejores puntajes ordenados de mayor a menor
    conn = sqlite3.connect('juego.db')
    cursor = conn.cursor()
    cursor.execute('SELECT jugador, puntaje FROM puntajes ORDER BY puntaje DESC LIMIT 5')
    top = cursor.fetchall()
    conn.close()
    return top

# Inicializa la base de datos al arrancar
inicializar_db()

# --- Interfaz Gráfica (GUI) ---
def accion_guardar():
    nombre = entry_nombre.get().strip()
    puntaje_str = entry_puntaje.get().strip()

    if not nombre or not puntaje_str:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    try:
        puntaje = int(puntaje_str)
        guardar_puntaje(nombre, puntaje)  # Llama a la función del backend
        messagebox.showinfo("Éxito", "¡Puntaje guardado en la base de datos con éxito!")
        entry_nombre.delete(0, tk.END)
        entry_puntaje.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "El puntaje debe ser un número entero.")

def abrir_ventana_top5():
    # Crea una ventana secundaria (Toplevel) para mostrar la tabla del Top 5
    top_window = tk.Toplevel(ventana)
    top_window.title("Top 5 Mejores Puntajes")
    top_window.geometry('350x250')
    top_window.config(bg='plum')

    tk.Label(top_window, text="🏆 Top 5 Jugadores", font=('Arial', 12, 'bold'), bg='plum').pack(pady=10)

    # Configuración del Treeview (Tabla)
    columnas = ('Jugador', 'Puntaje')
    tree = ttk.Treeview(top_window, columns=columnas, show='headings')
    tree.heading('Jugador', text='Jugador')
    tree.heading('Puntaje', text='Puntaje')

    tree.column('Jugador', width=180, anchor='w')
    tree.column('Puntaje', width=100, anchor='center')

    # Obtiene los datos de la base de datos e insértalos en la tabla
    registros = obtener_top5()
    for reg in registros:
        tree.insert('', tk.END, values=reg)

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Ventana Principal
ventana = tk.Tk()
ventana.title("Guardar Puntaje en SQLite")
ventana.geometry('400x320')
ventana.config(bg='plum')

tk.Label(ventana, text='Nombre del Jugador:', bg='plum', font=('Arial', 10, 'bold')).pack(pady=5)
entry_nombre = tk.Entry(ventana, font=('Arial', 11))
entry_nombre.pack(pady=5)

tk.Label(ventana, text='Puntaje:', bg='plum', font=('Arial', 10, 'bold')).pack(pady=5)
entry_puntaje = tk.Entry(ventana, font=('Arial', 11))
entry_puntaje.pack(pady=5)

# Botón para guardar
tk.Button(ventana, text='Guardar en BD', command=accion_guardar, bg='white', font=('Arial', 10)).pack(pady=10)

# Botón para ver el Top 5
tk.Button(ventana, text='Ver Top 5 🏆', command=abrir_ventana_top5, bg='lightyellow', font=('Arial', 10)).pack(pady=5)

ventana.mainloop()