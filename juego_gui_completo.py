import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import random

# IMPORTAMOS LAS CLASES DIRECTAMENTE DESDE TU ARCHIVO BACKEND
from juego_completo import Jugador, Ranking, PreguntaMultiple, PreguntaVF, cargar_preguntas

class QuizAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game Completo - Unidad 4")
        self.root.geometry('600x450')
        
        self.jugador = None
        self.preguntas_partida = []
        self.indice_actual = 0
        self.puntaje_ronda = 0
        
        self.inicializar_db()
        self.crear_menu()
        self.mostrar_inicio()

    def inicializar_db(self):
        self.conn = sqlite3.connect('quiz_juego.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jugador TEXT,
                puntaje INTEGER
            )
        ''')
        self.conn.commit()

    def crear_menu(self):
        barra_menu = tk.Menu(self.root)
        
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Inicio", command=self.mostrar_inicio)
        menu_opciones.add_command(label="Ver Ranking", command=self.mostrar_ranking)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=self.salir_aplicacion)
        
        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.root.config(menu=barra_menu)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_ventana()
        
        tk.Label(self.root, text="¡Bienvenido al Quiz Game!", font=('Arial', 18, 'bold')).pack(pady=20)
        
        frame_nombre = tk.Frame(self.root)
        frame_nombre.pack(pady=10)
        tk.Label(frame_nombre, text="Nombre del Jugador: ", font=('Arial', 11)).pack(side=tk.LEFT, padx=5)
        self.entry_nombre = tk.Entry(frame_nombre, font=('Arial', 11), width=20)
        self.entry_nombre.pack(side=tk.LEFT, padx=5)
        if self.jugador:
            self.entry_nombre.insert(0, self.jugador.nombre)

        tk.Button(self.root, text="📁 Cargar Preguntas (JSON)", font=('Arial', 11), width=25, command=self.cargar_archivo_json).pack(pady=8)
        tk.Button(self.root, text="▶ Comenzar a Jugar", font=('Arial', 11), bg='lightgreen', width=25, command=self.iniciar_juego).pack(pady=8)
        tk.Button(self.root, text="🏆 Ver Ranking", font=('Arial', 11), width=25, command=self.mostrar_ranking).pack(pady=8)
        tk.Button(self.root, text="❌ Salir", font=('Arial', 11), bg='lightcoral', width=25, command=self.salir_aplicacion).pack(pady=8)

    def cargar_archivo_json(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de preguntas", 
            filetypes=[("Archivos JSON", "*.json"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.preguntas_cargadas = cargar_preguntas(ruta)
            if self.preguntas_cargadas:
                messagebox.showinfo("Éxito", f"Se cargaron {len(self.preguntas_cargadas)} preguntas correctamente.")
            else:
                messagebox.showerror("Error", "No se pudieron cargar las preguntas o el archivo está vacío.")

    def iniciar_juego(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Atención", "Debe ingresar el nombre del jugador para comenzar.")
            return
        
        if not hasattr(self, 'preguntas_cargadas') or len(self.preguntas_cargadas) == 0:
            messagebox.showwarning("Atención", "Primero debe cargar un archivo JSON con preguntas.")
            return

        self.jugador = Jugador(nombre)
        self.puntaje_ronda = 0
        self.indice_actual = 0
        self.preguntas_partida = random.sample(self.preguntas_cargadas, min(3, len(self.preguntas_cargadas)))
        self.mostrar_siguiente_pregunta()

    def mostrar_siguiente_pregunta(self):
        self.limpiar_ventana()

        if self.indice_actual < len(self.preguntas_partida):
            pregunta_obj = self.preguntas_partida[self.indice_actual]
            
            tk.Label(self.root, text=f"Pregunta {self.indice_actual + 1} de {len(self.preguntas_partida)}", font=('Arial', 11, 'italic')).pack(pady=10)
            tk.Label(self.root, text=pregunta_obj.texto, font=('Arial', 13, 'bold'), wraplength=500).pack(pady=15)

            self.opcion_seleccionada = tk.StringVar(value="")

            if isinstance(pregunta_obj, PreguntaMultiple):
                for opcion in pregunta_obj.opciones:
                    tk.Radiobutton(self.root, text=opcion, variable=self.opcion_seleccionada, value=opcion, font=('Arial', 11)).pack(anchor='w', padx=100, pady=3)
            elif isinstance(pregunta_obj, PreguntaVF):
                tk.Radiobutton(self.root, text="Verdadero", variable=self.opcion_seleccionada, value="Verdadero", font=('Arial', 11)).pack(anchor='w', padx=100, pady=5)
                tk.Radiobutton(self.root, text="Falso", variable=self.opcion_seleccionada, value="Falso", font=('Arial', 11)).pack(anchor='w', padx=100, pady=5)

            tk.Button(self.root, text="Responder", font=('Arial', 11), width=15, command=lambda: self.evaluar_respuesta(pregunta_obj)).pack(pady=25)
        else:
            self.finalizar_juego()

    def evaluar_respuesta(self, pregunta_obj):
        respuesta = self.opcion_seleccionada.get()
        if not respuesta:
            messagebox.showwarning("Atención", "Seleccione una respuesta antes de continuar.")
            return

        es_correcta = pregunta_obj.esta_correcto(respuesta)
        puntaje_obtenido = pregunta_obj.calcular_puntaje(0)
        self.puntaje_ronda += puntaje_obtenido

        if es_correcta:
            messagebox.showinfo("Correcto", f"¡Respuesta correcta! Puntos obtenidos: {puntaje_obtenido}")
        else:
            messagebox.showerror("Incorrecto", f"Respuesta incorrecta. Puntos obtenidos: {puntaje_obtenido}")

        self.indice_actual += 1
        self.mostrar_siguiente_pregunta()

    def finalizar_juego(self):
        self.limpiar_ventana()
        self.jugador.puntaje = self.puntaje_ronda

        tk.Label(self.root, text="🎉 ¡Partida Finalizada!", font=('Arial', 16, 'bold')).pack(pady=20)
        tk.Label(self.root, text=f"Jugador: {self.jugador.nombre}", font=('Arial', 12)).pack(pady=5)
        tk.Label(self.root, text=f"Puntaje total obtenido: {self.jugador.puntaje}", font=('Arial', 12, 'bold')).pack(pady=10)

        self.cursor.execute('INSERT INTO ranking (jugador, puntaje) VALUES (?, ?)', (self.jugador.nombre, self.jugador.puntaje))
        self.conn.commit()

        tk.Button(self.root, text="Ver Ranking", font=('Arial', 11), width=20, command=self.mostrar_ranking).pack(pady=10)
        tk.Button(self.root, text="Volver al Inicio", font=('Arial', 11), width=20, command=self.mostrar_inicio).pack(pady=5)
        tk.Button(self.root, text="Salir", font=('Arial', 11), bg='lightcoral', width=20, command=self.salir_aplicacion).pack(pady=5)

    def mostrar_ranking(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="🏆 Top 5 Mejores Puntajes (Base de Datos)", font=('Arial', 14, 'bold')).pack(pady=15)

        columnas = ('Jugador', 'Puntaje')
        tree = ttk.Treeview(self.root, columns=columnas, show='headings')
        tree.heading('Jugador', text='Jugador')
        tree.heading('Puntaje', text='Puntaje')

        tree.column('Jugador', width=250, anchor='w')
        tree.column('Puntaje', width=120, anchor='center')

        self.cursor.execute('SELECT jugador, puntaje FROM ranking ORDER BY puntaje DESC LIMIT 5')
        filas = self.cursor.fetchall()

        for fila in filas:
            tree.insert('', tk.END, values=fila)

        tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        tk.Button(self.root, text="Volver al Inicio", font=('Arial', 11), width=20, command=self.mostrar_inicio).pack(pady=15)

    def salir_aplicacion(self):
        if hasattr(self, 'conn'):
            self.conn.close()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizAppGUI(root)
    root.mainloop()