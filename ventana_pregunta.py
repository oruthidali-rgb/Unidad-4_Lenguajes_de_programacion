#Ventana_pregunta
#Este programa muestra una ventana secundatia sobre la ventana principal mostrando una pregunta y permitiendo contestar en una caja de texto
#Idali
#15/11/26
import tkinter as tk  # Importa la librería tkinter
from tkinter import messagebox

# 1. Importamos la clase Pregunta desde el archivo que corregimos antes
from pregunta_basica import Pregunta

def mostrar_pregunta_en_gui(pregunta_obj):
    # Crea una ventana secundaria de tipo Toplevel para la pregunta
    top = tk.Toplevel()
    top.title("Ventana de Pregunta (Unidad 2)")
    top.geometry('300x250')
    top.config(bg='lightblue')
    
    # 2. Muestra el texto utilizando el atributo .texto del objeto que se pasó por parámetro
    tk.Label(top, text=pregunta_obj.texto, font=('Arial', 12, 'bold'), wraplength=350).pack(pady=15)
    
    # Caja de texto para que el usuario escriba su respuesta
    tk.Label(top, text="Escribe tu respuesta:", font=('Arial', 10)).pack(pady=5)
    entrada_usuario = tk.Entry(top, font=('Arial', 11))
    entrada_usuario.pack(pady=5)

    def responder():
        # Obtiene el texto ingresado en la caja de texto
        respuesta = entrada_usuario.get()
        
        # 3. Utiliza el método .verificar() propio de la clase Pregunta de la Unidad 2
        if pregunta_obj.verificar(respuesta):
            messagebox.showinfo("Resultado", "¡Respuesta Correcta!", parent=top)
        else:
            messagebox.showerror("Resultado", "Respuesta Incorrecta. Inténtalo de nuevo.", parent=top)

    # Botón para evaluar la respuesta
    tk.Button(top, text="Responder", command=responder).pack(pady=15)


# --- Código de prueba en la ventana principal ---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana_pregunta")
    ventana_principal.geometry('400x300')
    ventana_principal.config(bg='lightgreen')

    # Creamos un objeto de la clase Pregunta importada (con su respectiva respuesta correcta)
    mi_pregunta = Pregunta("¿Cuál es la capital de Francia?", "Paris")

    # Botón en la ventana principal que abre la GUI pasándole el objeto 'mi_pregunta'
    tk.Button(
        ventana_principal, 
        text="Abrir Pregunta", 
        font=('Arial', 11),
        command=lambda: mostrar_pregunta_en_gui(mi_pregunta)
    ).pack(expand=True)

    ventana_principal.mainloop()