#Ventana_basica
#Este programa muestra una ventana principal, la cual contiene un saludo y determinadas caracteristicas con respecto a las dimensiones y el color de fondo
#Idali
#05/11/26
import tkinter as tk#importar la libreria tkinter
ventana=tk.Tk()#crear la ventana principal
ventana.title("Mi primera ventana")#titulo de la ventana
ventana.geometry("400x300") #dimensiones de la ventana
ventana.configure(bg='lightblue')#color de la ventana
ventana.mainloop()#iniciar el bucle de la ventana
