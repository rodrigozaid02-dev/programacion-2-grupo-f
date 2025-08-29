# importacion de librerias 
import tkinter as tk
from tkinter import ttk, messagebox
#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
# crear contenedor notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al notebook
pestañas.add(frame_pacientes, text="Pacientes")
#mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
#Nombre 
LabelNombre=tk.Label(frame_pacientes,text="Nombre Completo:")
LabelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#fecha de nacimiento
LabelFecha=tk.Label(frame_pacientes,text="Fecha de Nacimiento (DD/MM/AAAA):")
LabelFecha.grid(row=1,column=0,padx=5,pady=5,sticky="w")
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#edad (readonly)
LabelEdad=tk.Label(frame_pacientes,text="Edad:")
LabelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#genero
LabelGenero=tk.Label(frame_pacientes,text="Genero:")
LabelGenero.grid(row=3,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,padx=5,sticky="w")
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,sticky="w")
#grupo sanguineo
LabelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:")
LabelGrupoSanguineo.grid(row=4,column=0,padx=5,pady=5,sticky="w")
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5,column=0,padx=5,pady=5,sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico","Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#centro medico
LabelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:")
LabelCentroMedico.grid(row=6,column=0,padx=5,pady=5,sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central","Clinica Norte","Centro Salud Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6,column=1,padx=5,pady=5,sticky="w")
















# crear contenedor notebook (Doctores)
pestañas=ttk.Notebook(ventana_principal)
#crear frames (uno por pestaña)
frame_doctores=ttk.Frame(pestañas)
#Agregar pestañas al notebook
pestañas.add(frame_doctores, text="Doctores")
#mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")

#Nombre
LabelNombre=tk.Label(frame_doctores,text="Nombre Completo:")
LabelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#fecha de nacimiento
LabelFecha=tk.Label(frame_doctores,text="Fecha de Nacimiento (DD/MM/AAAA):")
LabelFecha.grid(row=1,column=0,padx=5,pady=5,sticky="w")
fechaN=tk.Entry(frame_doctores)
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#edad (readonly)
LabelEdad=tk.Label(frame_doctores,text="Edad:")
LabelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Entry(frame_doctores,state="readonly")
edadP.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#genero
LabelGenero=tk.Label(frame_doctores,text="Genero:")
LabelGenero.grid(row=3,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
radioMasculino=ttk.Radiobutton(frame_doctores,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,padx=5,sticky="w")
radioFemenino=ttk.Radiobutton(frame_doctores,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,sticky="w")
#grupo sanguineo
LabelGrupoSanguineo=tk.Label(frame_doctores,text="Grupo Sanguineo:")
LabelGrupoSanguineo.grid(row=4,column=0,padx=5,pady=5,sticky="w")
entryGrupoSanguineo=tk.Entry(frame_doctores)
entryGrupoSanguineo.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#tipo de seguro
labelTipoSeguro=tk.Label(frame_doctores,text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5,column=0,padx=5,pady=5,sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_doctores, values=["Publico","Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5,column=1,padx=5,pady=5,sticky="w")

#centro medico
LabelCentroMedico=tk.Label(frame_doctores,text="Centro de salud:")
LabelCentroMedico.grid(row=6,column=0,padx=5,pady=5,sticky="w")
centro_medicoD=tk.StringVar()
centro_medicoD.set("Hospital Central") #valor por defecto
comboCentroMedico=ttk.Combobox(frame_doctores, values=["Hospital Central","Clinica Norte","Centro Salud Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6,column=1,padx=5,pady=5,sticky="w")










ventana_principal.mainloop()