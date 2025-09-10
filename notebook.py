# Importación de librerías
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
 
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
 
    if fechaN.get() !=formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)
 
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year - fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
def guardar_en_archivo():
    with open("pacientes.txt", "w", encoding="utf-8") as archivo:
        for paciente in pacientes_data:
            archivo.write(
                f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                f"{paciente['Género']}|{paciente['Grupo Sanguíneo']}|"
                f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}\n"
            )
# Guardar doctores en archivo
def guardar_doctores_en_archivo():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
                f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|{doctor['Teléfono']}\n"
            )



#lista de pacientes
pacientes_data=[]
#funcion para registrar pacientes
def registrarPaciente():
    #crear un diccionario con los datos del paciente
    paciente={
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Género": genero.get(),
        "Grupo Sanguíneo": entryGrupoS.get(),
        "Tipo de Seguro": tipoSeguro.get(),
        "Centro Médico": centroM.get()
}
    #agregar pacientes a la lista
    pacientes_data.append(paciente)
    #linea modificada 07/09/2025
    guardar_en_archivo()
    #cargar al treeview

def cargar_treeview():
    #limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #insertar cada paciente
    for i, item in enumerate(pacientes_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Género"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"]
            )
        )
       
def cargar_desde_archivo_paciente():
    try:
        with open("pacientes.txt", "r", encoding="utf-8") as archivo:
            pacientes_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Género": datos[3],
                        "Grupo Sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6]
                    }
                    pacientes_data.append(paciente)
            cargar_treeview()
    except FileNotFoundError:
        open
def eliminar_paciente():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar paciente",f"¿Estás seguro de que deseas eliminar este paciente '{treeview.item(id_item, 'values')[0]}?"):
            del pacientes_data[indice]
            guardar_en_archivo()   #guarda los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente")
    else: #este elsees del if seleccionado
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente.")
        return





# Lista de doctores
doctores_data = []
# Función para registrar doctores
def registrarDoctor():
    # Crear un diccionario con los datos del doctor
    doctor = {
        "Nombre": entryNombreD.get(),
        "Especialidad": especialidadD.get(),
        "Edad": entryEdadD.get(),
        "Teléfono": entryTelefonoD.get()
    }
    # Agregar doctor a la lista
    doctores_data.append(doctor)
    # Guardar en archivo
    guardar_doctores_en_archivo()
    # Cargar al treeview de doctores
    cargar_treeview_doctores()
def cargar_treeview_doctores():
    # Limpiar el treeview de doctores
    for item in treeviewD.get_children():
        treeviewD.delete(item)
    # Insertar cada doctor
    for i, item in enumerate(doctores_data):
        treeviewD.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Teléfono"]
            )
        )

def cargar_desde_archivo_doctor():
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Teléfono": datos[3]
                    }
                    doctores_data.append(doctor)
    except FileNotFoundError:
        open

# Función para eliminar doctor seleccionado con confirmación
def eliminar_doctor():
    selected = treeviewD.selection()
    if selected:
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este doctor?")
        if respuesta:
            for item in selected:
                treeviewD.delete(item)
                # Eliminar del listado de datos
                index = int(item)
                if 0 <= index < len(doctores_data):
                    doctores_data.pop(index)
            guardar_doctores_en_archivo()
            messagebox.showinfo("Eliminado", "Doctor eliminado")

# Crear ventana principal
# Ventana principal con fondo negro
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("890x600")
ventanaPrincipal.configure(bg="black")
# Crear contenedor NoteBook (pestañas)
pestañas = ttk.Notebook(ventanaPrincipal)
# Crear frames
# Frames con fondo negro
framePacientes = tk.Frame(pestañas, bg="black")
frameDoctores = tk.Frame(pestañas, bg="black")
# Agregar pestañas al NoteBook
pestañas.add(framePacientes, text="Pacientes")
pestañas.add(frameDoctores, text="Doctores")
# Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
# Nombre
labelNombre = tk.Label(framePacientes, text=" Nombre Completo:", font=("Old English Text MT", 14), fg="white", bg="black")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP = tk.Entry(framePacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Fecha de nacimiento
labelFechaN = tk.Label(framePacientes, text=" Fecha de Nacimiento:", font=("Old English Text MT", 14), fg="white", bg="black")
labelFechaN.grid(row=1, column=0, padx=5, pady=5, sticky="w")
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
fechaN = ttk.Entry(framePacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
# Edad (readonly)
labelEdad = tk.Label(framePacientes, text=" Edad:", font=("Old English Text MT", 14), fg="white", bg="black")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadVar=tk.StringVar()
edadP = tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")
# Género
labelGenero = tk.Label(framePacientes, text=" Género:", font=("Old English Text MT", 14), fg="white", bg="black")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")
genero = tk.StringVar()
genero.set("Masculino") # Valor por defecto
radioMasculino = ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, sticky="w")
radioFemenino = ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, padx=5, sticky="w")
# Grupo sanguíneo
labelGrupoS = tk.Label(framePacientes, text=" Grupo Sanguíneo:", font=("Old English Text MT", 14), fg="white", bg="black")
labelGrupoS.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entryGrupoS = tk.Entry(framePacientes)
entryGrupoS.grid(row=5, column=1, padx=5, pady=5, sticky="w")
# Tipo de seguro
labelTipoS = tk.Label(framePacientes, text=" Tipo de Seguro:", font=("Old English Text MT", 14), fg="white", bg="black")
labelTipoS.grid(row=6, column=0, padx=5, pady=5, sticky="w")
tipoSeguro = tk.StringVar()
tipoSeguro.set("Público") # Valor por defecto
comboTipoS = ttk.Combobox(framePacientes, values=["Público", "Privado","Ninguno"], textvariable=tipoSeguro)
comboTipoS.grid(row=6, column=1, padx=5, pady=5, sticky="w")
# Tipo de centro médico
labelCentroM = tk.Label(framePacientes, text=" Centro Médico:", font=("Old English Text MT", 14), fg="white", bg="black")
labelCentroM.grid(row=7, column=0, padx=5, pady=5, sticky="w")
centroM = tk.StringVar()
centroM.set("Hospital Central") # Valor por defecto
comboCentroM = ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte","Centro Salud Sur"], textvariable=centroM)
comboCentroM.grid(row=7, column=1, padx=5, pady=5, sticky="w")
# Frame para los botones
btnFrame = tk.Frame(framePacientes)
btnFrame.grid(row=8, column=1, columnspan=2, pady=5, sticky="w")
# Botón registrar
btnRegistrar = tk.Button(btnFrame, text="Registrar",bg="green", fg="white", command=registrarPaciente)
btnRegistrar.grid(row=0, column=0, padx=5)
# Botón Eliminar
btnEliminar = tk.Button(btnFrame, text="Eliminar", bg="red", fg="White", command=eliminar_paciente)
btnEliminar.grid(row=0, column=1, padx=5)
# Crera Treeview para mostrar los pacientes
treeview = ttk.Treeview(framePacientes, columns=("Nombre","FechaN","Edad", "Género", "GrupoS", "TipoS", "CentroM"), show="headings")
# Definir encabezados
treeview.heading("Nombre", text="Nombre")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
#definir ancho de columnas
treeview.column("Nombre", width=200)    
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50)
treeview.column("Género", width=100)
treeview.column("GrupoS", width=100)
treeview.column("TipoS", width=100)
treeview.column("CentroM", width=150)
#ubicar el treeview en la cuadricula
treeview.grid(row=9, column=0, columnspan=4, padx=5, pady=5)
#Escrolbar vertical
scrollbar = ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=9, column=4, sticky="ns")
# Nombre
labelNombreD = tk.Label(frameDoctores, text="Nombre:", font=("Old English Text MT", 14), fg="white", bg="black")
labelNombreD.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entryNombreD = tk.Entry(frameDoctores)
entryNombreD.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Especialidad
labelEspecialidadD = tk.Label(frameDoctores, text="Especialidad:", font=("Old English Text MT", 14), fg="white", bg="black")
labelEspecialidadD.grid(row=1, column=0, padx=5, pady=5, sticky="w")
especialidadD = tk.StringVar()
comboEspecialidadD = ttk.Combobox(frameDoctores, values=["Cardiología", "Dermatología", "Neurología", "Pediatría", "Ginecología", "Ortopedia"], textvariable=especialidadD, state="readonly")
comboEspecialidadD.grid(row=1, column=1, padx=5, pady=5, sticky="w")
# Edad
labelEdadD = tk.Label(frameDoctores, text="Edad:", font=("Old English Text MT", 14), fg="white", bg="black")
labelEdadD.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entryEdadD = tk.Spinbox(frameDoctores,from_=0,to=100, width=5)
entryEdadD.grid(row=2, column=1, padx=5, pady=5, sticky="w")
# Teléfono
labelTelefonoD = tk.Label(frameDoctores, text="Teléfono:", font=("Old English Text MT", 14), fg="white", bg="black")
labelTelefonoD.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entryTelefonoD = tk.Entry(frameDoctores)
entryTelefonoD.grid(row=3, column=1, padx=5, pady=5, sticky="w")
# Frame para botones
btnFrameD = tk.Frame(frameDoctores)
btnFrameD.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")
btnRegistrarD = tk.Button(btnFrameD, text="Registrar", bg="green", fg="white", command=registrarDoctor)
btnRegistrarD.grid(row=0, column=0, padx=5)
btnEliminarD = tk.Button(btnFrameD, text="Eliminar", bg="red", fg="white", command=eliminar_doctor)
btnEliminarD.grid(row=0, column=1, padx=5)
# Treeview para mostrar doctores
treeviewD = ttk.Treeview(frameDoctores, columns=("Nombre", "Especialidad", "Edad", "Teléfono"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Teléfono", text="Teléfono")
treeviewD.column("Nombre", width=180)
treeviewD.column("Especialidad", width=140)
treeviewD.column("Edad", width=60)
treeviewD.column("Teléfono", width=120)
treeviewD.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
# Scrollbar vertical para treeview doctores
scrollbarD = ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscroll=scrollbarD.set)
scrollbarD.grid(row=5, column=4, sticky="ns")
 



cargar_desde_archivo_paciente() #carga datos desde archivo al iniciar la aplicacion
cargar_desde_archivo_doctor()
cargar_treeview_doctores()
ventanaPrincipal.mainloop()