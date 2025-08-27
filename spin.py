#spinbox de numeros del 1 al 10 para edad
import tkinter as tk
from tkinter import messagebox
def mostrarEdad():
    messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")

# Función para mostrar el género seleccionado
def mostrarGenero():
    messagebox.showinfo("Género", f"El género seleccionado es: {genero.get()}")
Ventana = tk.Tk()
Ventana.geometry("250x100")
label_edad = tk.Label(Ventana, text="Edad")
label_edad.grid(row=0, column=0, padx=5, pady=5, sticky="W")
spin = tk.Spinbox(from_=1, to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
boton = tk.Button(text="Obtener valor", command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)
 
#Genero
labelGenero=tk.Label(Ventana, text="Genero")
labelGenero.grid(row=2, column=0, padx=5, pady=5, sticky="w")
#spinbox de texto para genero
genero=tk.Spinbox(Ventana, values=("Masculino", "Femenino", "Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)
botonGenero=tk.Button(Ventana, text="Obtener genero", command=mostrarGenero)
botonGenero.grid(row=3, column=0, padx=10, pady=10)
















Ventana.mainloop()