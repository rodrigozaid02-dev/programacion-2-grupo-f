# importacion de librerias 
import tkinter as tk
from tkinter import ttk, messagebox
#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("1200x900")

# Estilo personalizado para las pestañas
style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background='black', foreground='white', font=('Old English Text MT', 12, 'bold'))
style.map('TNotebook.Tab', background=[('selected', 'black')], foreground=[('selected', 'white')])

# crear contenedor notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al notebook
pestañas.add(frame_pacientes, text="Pacientes")
#mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
#Nombre 
LabelNombre=tk.Label(frame_pacientes,text="Nombre Completo:", font=("Old English Text MT", 11))
LabelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#fecha de nacimiento
# Fecha de nacimiento
LabelFecha=tk.Label(frame_pacientes,text="Fecha de Nacimiento (DD/MM/AAAA):", font=("Old English Text MT", 11))
LabelFecha.grid(row=1,column=0,padx=5,pady=5,sticky="w")
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#edad (readonly)
# Edad
LabelEdad=tk.Label(frame_pacientes,text="Edad:", font=("Old English Text MT", 11))
LabelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Spinbox(frame_pacientes, from_=0, to=120, font=("Old English Text MT", 11), width=5)
edadP.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#genero
# Género
LabelGenero=tk.Label(frame_pacientes,text="Genero:", font=("Old English Text MT", 11))
LabelGenero.grid(row=3,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
# Botones de género en la misma fila
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,padx=5,sticky="w")
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=3,column=2,padx=5,sticky="w")
#grupo sanguineo
# Grupo sanguíneo
LabelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:", font=("Old English Text MT", 11))
LabelGrupoSanguineo.grid(row=4,column=0,padx=5,pady=5,sticky="w")
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#tipo de seguro
# Tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de Seguro:", font=("Old English Text MT", 11))
labelTipoSeguro.grid(row=5,column=0,padx=5,pady=5,sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico","Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#centro medico
# Centro médico
LabelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:", font=("Old English Text MT", 11))
LabelCentroMedico.grid(row=6,column=0,padx=5,pady=5,sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central","Clinica Norte","Centro Salud Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6,column=1,padx=5,pady=5,sticky="w")
#frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8,column=0,columnspan=2,pady=5, sticky="w")
#boton registrar (verde)
btn_registrar=tk.Button(btn_frame, text="Registrar", command="", bg="green", fg="white", activebackground="#228B22", font=("Old English Text MT", 11))
btn_registrar.grid(row=0,column=0,padx=5)
#boton eliminar (rojo)
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="", bg="red", fg="white", activebackground="#8B0000", font=("Old English Text MT", 11))
btn_eliminar.grid(row=0,column=1,padx=5)
#crear TreeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes, columns=("Nombre", "Fecha de Nacimiento", "Edad", "Genero", "Grupo Sanguineo", "Tipo de Seguro", "Centro de Medico"), show="headings")
#definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("Grupo Sanguineo", text="Grupo Sanguineo")
treeview.heading("Tipo de Seguro", text="Tipo de Seguro")
treeview.heading("Centro de Medico", text="Centro de Medico")
#definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("Fecha de Nacimiento", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("Grupo Sanguineo", width=100, anchor="center")
treeview.column("Tipo de Seguro", width=100, anchor="center")
treeview.column("Centro de Medico", width=120)
#ubicar el treeview en la cuadricula
treeview.grid(row=7,column=0,columnspan=2,padx=5,pady=10, sticky="nsew")
#scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7,column=2, sticky="ns")




























# crear contenedor notebook (Doctores)
# (Ya existe el notebook, solo agregar la pestaña de doctores)
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")

#Nombre
# Nombre
LabelNombre=tk.Label(frame_doctores,text="Nombre Completo:", font=("Old English Text MT", 11))
LabelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#fecha de nacimiento
# Fecha de nacimiento
LabelFecha=tk.Label(frame_doctores,text="Fecha de Nacimiento (DD/MM/AAAA):", font=("Old English Text MT", 11))
LabelFecha.grid(row=1,column=0,padx=5,pady=5,sticky="w")
fechaN=tk.Entry(frame_doctores)
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#edad (readonly)
# Edad
LabelEdad=tk.Label(frame_doctores,text="Edad:", font=("Old English Text MT", 11))
LabelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Spinbox(frame_doctores, from_=0, to=120, font=("Old English Text MT", 11), width=5)
edadP.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#genero
# Género
LabelGenero=tk.Label(frame_doctores,text="Genero:", font=("Old English Text MT", 11))
LabelGenero.grid(row=3,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
# Botones de género en la misma fila
radioMasculino=ttk.Radiobutton(frame_doctores,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,padx=5,sticky="w")
radioFemenino=ttk.Radiobutton(frame_doctores,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=3,column=2,padx=5,sticky="w")
#grupo sanguineo
# Grupo sanguíneo
LabelGrupoSanguineo=tk.Label(frame_doctores,text="Grupo Sanguineo:", font=("Old English Text MT", 11))
LabelGrupoSanguineo.grid(row=4,column=0,padx=5,pady=5,sticky="w")
entryGrupoSanguineo=tk.Entry(frame_doctores)
entryGrupoSanguineo.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#tipo de seguro
# Tipo de seguro
labelTipoSeguro=tk.Label(frame_doctores,text="Tipo de Seguro:", font=("Old English Text MT", 11))
labelTipoSeguro.grid(row=5,column=0,padx=5,pady=5,sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_doctores, values=["Publico","Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#centro medico
# Centro médico
LabelCentroMedico=tk.Label(frame_doctores,text="Centro de salud:", font=("Old English Text MT", 11))
LabelCentroMedico.grid(row=6,column=0,padx=5,pady=5,sticky="w")
centro_medicoD=tk.StringVar()
centro_medicoD.set("Hospital Central") #valor por defecto
comboCentroMedico=ttk.Combobox(frame_doctores, values=["Hospital Central","Clinica Norte","Centro Salud Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6,column=1,padx=5,pady=5,sticky="w")

#definir encabezados
treeviewD=ttk.Treeview(frame_doctores, columns=("Nombre", "Fecha de Nacimiento", "Edad", "Genero", "Grupo Sanguineo", "Tipo de Seguro", "Centro de Medico"), show="headings")
treeviewD.heading("Nombre", text="Nombre Completo")
treeviewD.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Genero", text="Genero")
treeviewD.heading("Grupo Sanguineo", text="Grupo Sanguineo")
treeviewD.heading("Tipo de Seguro", text="Tipo de Seguro")
treeviewD.heading("Centro de Medico", text="Centro de Medico")
#definir anchos de columnas
treeviewD.column("Nombre", width=120)
treeviewD.column("Fecha de Nacimiento", width=120)
treeviewD.column("Edad", width=50, anchor="center")
treeviewD.column("Genero", width=60, anchor="center")
treeviewD.column("Grupo Sanguineo", width=100, anchor="center")
treeviewD.column("Tipo de Seguro", width=100, anchor="center")
treeviewD.column("Centro de Medico", width=120)
#ubicar el treeview en la cuadricula
treeviewD.grid(row=7,column=0,columnspan=2,padx=5,pady=10, sticky="nsew")
#scrollbar vertical
doc_scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscrollcommand=doc_scroll_y.set)
doc_scroll_y.grid(row=7,column=2, sticky="ns")

#frame para los botones de doctores
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=8,column=0,columnspan=2,pady=5, sticky="w")
#boton registrar (verde)
btn_registrarD=tk.Button(btn_frameD, text="Registrar", command="", bg="green", fg="white", activebackground="#228B22", font=("Old English Text MT", 11))
btn_registrarD.grid(row=0,column=0,padx=5)
#boton eliminar (rojo)
btn_eliminarD=tk.Button(btn_frameD, text="Eliminar", command="", bg="red", fg="white", activebackground="#8B0000", font=("Old English Text MT", 11))
btn_eliminarD.grid(row=0,column=1,padx=5)

























ventana_principal.mainloop()