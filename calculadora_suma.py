import tkinter as tk
def sumar():
    numero1 = int(entry1.get())
    numero2 = int(entry2.get())
    resultado = numero1 + numero2
    label_resultado.config(text=f"Resultado: {resultado}")
ventana=tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("400x300")
ventana.configure(bg='lightgray')
entry1 = tk.Entry(ventana)
entry1.pack(pady=10)
entry2 = tk.Entry(ventana)
entry2.pack(pady=10)

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack(pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=10)
ventana.mainloop()