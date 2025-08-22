
# Importa la librería de interfaces gráficas y mensajes
import tkinter as tk 
from tkinter import messagebox

def nuevodDoctor():
    # Ventana secundaria para registrar un nuevo doctor
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)  # Crea ventana secundaria
    ventanaRegistro.title("Registro de Doctor")   # Título de la ventana
    ventanaRegistro.geometry("600x600")          # Tamaño de la ventana
    ventanaRegistro.configure(bg="black")        # Fondo negro
    # Campo nombre
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:",bg="black", fg="white", font=("Old English Text MT", 12))
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")
    entryNombre=tk.Entry(ventanaRegistro, font=("Old English Text MT", 12))
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")
    # Campo dirección
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion:",bg="black", fg="white", font=("Old English Text MT", 12))
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")
    entryDireccion=tk.Entry(ventanaRegistro, font=("Old English Text MT", 12))
    entryDireccion.grid(row=1, column=1,padx=10,pady=5,sticky="we")
    # Campo teléfono
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono:",bg="black", fg="white", font=("Old English Text MT", 12))
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")
    entryTelefono=tk.Entry(ventanaRegistro, font=("Old English Text MT", 12))
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")
    # Especialidades (checkbuttons)
    espLabel=tk.Label(ventanaRegistro,text="Especilidades:",bg="black", fg="white", font=("Old English Text MT", 12))
    espLabel.grid(row=5,column=0,padx=10,pady=5,sticky="n")
    pediatria=tk.BooleanVar(value=False)         # Variable para pediatría
    cardiologia=tk.BooleanVar(value=False)       # Variable para cardiología
    neurologia=tk.BooleanVar(value=False)        # Variable para neurología
    cbPediatria=tk.Checkbutton(ventanaRegistro,text="Pediatría",variable=pediatria, bg="black", fg="white", font=("Old English Text MT", 12), selectcolor="black")
    cbPediatria.grid(row=6,column=0,columnspan=2,sticky="w", padx=20)
    cbCardiologia=tk.Checkbutton(ventanaRegistro,text="Cardiología",variable=cardiologia, bg="black", fg="white", font=("Old English Text MT", 12), selectcolor="black")
    cbCardiologia.grid(row=7,column=0,columnspan=2,sticky="w", padx=20)
    cbNeurologia=tk.Checkbutton(ventanaRegistro,text="Neurología",variable=neurologia, bg="black", fg="white", font=("Old English Text MT", 12), selectcolor="black")
    cbNeurologia.grid(row=8,column=0,columnspan=2,sticky="w", padx=20)
    # Disponibilidad (checkbuttons)
    dispLabel=tk.Label(ventanaRegistro,text="Disponibilidad:",bg="black", fg="white", font=("Old English Text MT", 12))
    dispLabel.grid(row=9,column=0,padx=10,pady=5,sticky="n")
    manana=tk.BooleanVar(value=False)        # Variable para mañana
    tarde=tk.BooleanVar(value=False)         # Variable para tarde
    noche=tk.BooleanVar(value=False)         # Variable para noche
    cbManana=tk.Checkbutton(ventanaRegistro,text="Mañana",variable=manana, bg="black", fg="white", font=("Old English Text MT", 12), selectcolor="black")
    cbManana.grid(row=10,column=0,columnspan=2,sticky="w", padx=20)
    cbTarde=tk.Checkbutton(ventanaRegistro,text="Tarde",variable=tarde, bg="black", fg="white", font=("Old English Text MT", 12), selectcolor="black")
    cbTarde.grid(row=11,column=0,columnspan=2,sticky="w", padx=20)
    cbNoche=tk.Checkbutton(ventanaRegistro,text="Noche",variable=noche, bg="black", fg="white", font=("Old English Text MT", 12), selectcolor="black")
    cbNoche.grid(row=12,column=0,columnspan=2,sticky="w", padx=20)

    # Función para mostrar los datos ingresados y cerrar la ventana
    def registrarDatos():
        especialidades = []
        if pediatria.get():
            especialidades.append("Pediatría")
        if cardiologia.get():
            especialidades.append("Cardiología")
        if neurologia.get():
            especialidades.append("Neurología")
        if len(especialidades) > 0:
            especialidadesTexto = ', '.join(especialidades)
        else:
            especialidadesTexto = 'Ninguna'

        disponibilidad = []
        if manana.get():
            disponibilidad.append("Mañana")
        if tarde.get():
            disponibilidad.append("Tarde")
        if noche.get():
            disponibilidad.append("Noche")
        if len(disponibilidad) > 0:
            disponibilidadTexto = ', '.join(disponibilidad)
        else:
            disponibilidadTexto = 'Ninguna'

        info = (
            f"Nombre: {entryNombre.get()}\n"
            f"Dirección: {entryDireccion.get()}\n"
            f"Teléfono: {entryTelefono.get()}\n"
            f"Especialidades: {especialidadesTexto}\n"
            f"Disponibilidad: {disponibilidadTexto}"
        )
        messagebox.showinfo("Datos Registrados", info)
        ventanaRegistro.destroy()

    # Botón para registrar los datos
    btnRegistrar = tk.Button(ventanaRegistro, text="Registrar datos", command=registrarDatos, font=("Old English Text MT", 12), bg="white", fg="black")
    btnRegistrar.grid(row=13, column=0, columnspan=2, pady=15)

# Menú principal para registro de doctores

# Ventana principal del sistema
ventanaPrincipal=tk.Tk()  # Crea la ventana principal
ventanaPrincipal.title("Sistema de Registro de Doctores")  # Título
ventanaPrincipal.geometry("1000x600")  # Tamaño
ventanaPrincipal.configure(bg="black")  # Fondo negro
# Barra de menú principal
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)

# Menú de opciones para doctores
menuDoctores=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor",command=nuevodDoctor)  # Opción para registrar
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir",command=ventanaPrincipal.quit)  # Opción para salir

ventanaPrincipal.mainloop()  # Inicia la aplicación