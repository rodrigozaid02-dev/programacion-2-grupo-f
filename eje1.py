import tkinter as tk 
from tkinter import messagebox
#Funcion para pacientes
def nuevoPaciente():  # sourcery skip: assign-if-exp, simplify-len-comparison
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("600x400")
    ventanaRegistro.configure(bg="blue")  # Azul
    #nombre
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:",bg="blue", fg="white", font=("MS Gothic", 12))
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")
    entryNombre=tk.Entry(ventanaRegistro, font=("MS Gothic", 12))
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")
    #Direccion
    direccionLabel=tk.Label(ventanaRegistro,text="Direccion:",bg="blue", fg="white", font=("MS Gothic", 12))
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")
    entryDireccion=tk.Entry(ventanaRegistro, font=("MS Gothic", 12))
    entryDireccion.grid(row=1, column=1,padx=10,pady=5,sticky="we")
    #Telefono
    telefonoLabel=tk.Label(ventanaRegistro,text="Telefono:",bg="blue", fg="white", font=("MS Gothic", 12))
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")
    entryTelefono=tk.Entry(ventanaRegistro, font=("MS Gothic", 12))
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")
    #enfermedades base(checkbutton)
    enfLabel=tk.Label(ventanaRegistro,text="Enfermedades base:",bg="blue", fg="white", font=("MS Gothic", 12))
    enfLabel.grid(row=5,column=0,padx=10,pady=5,sticky="n")
    diabetes=tk.BooleanVar(value=False)         # Valor inicial desmarcado
    hipertension=tk.BooleanVar(value=False)     # Valor inicial desmarcado
    asma=tk.BooleanVar(value=False)             # Valor inicial desmarcado
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes, bg="blue", fg="white", font=("MS Gothic", 12), selectcolor="blue")
    cbDiabetes.grid(row=6,column=0,columnspan=2,sticky="w", padx=20)
    cbHipertension=tk.Checkbutton(ventanaRegistro,text="Hipertension",variable=hipertension, bg="blue", fg="white", font=("MS Gothic", 12), selectcolor="blue")
    cbHipertension.grid(row=7,column=0,columnspan=2,sticky="w", padx=20)
    cbAsma=tk.Checkbutton(ventanaRegistro,text="Asma",variable=asma, bg="blue", fg="white", font=("MS Gothic", 12), selectcolor="blue")
    cbAsma.grid(row=8,column=0,columnspan=2,sticky="w", padx=20)
    #sexo (radiobutton)
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo:",bg="blue", fg="white", font=("MS Gothic", 12))
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="n")
    sexo=tk.StringVar(value="Masculino")        # Valor inicial seleccionado
    rbMasculino=tk.Radiobutton(ventanaRegistro,text="Masculino",variable=sexo,value="Masculino", bg="blue", fg="white", font=("MS Gothic", 12), selectcolor="blue")
    rbMasculino.grid(row=3,column=1,sticky="n")
    rbFemenino=tk.Radiobutton(ventanaRegistro,text="Femenino",variable=sexo, value="Femenino", bg="blue", fg="white", font=("MS Gothic", 12), selectcolor="blue")
    rbFemenino.grid(row=4,column=1,sticky="n")
#Acción: registrar datos
    def registrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertensión")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades)>0:
            enfermedadesTexto=','.join(enfermedades)
        else:
            enfermedadesTexto='Ninguna'
#cadena para mostrar todos los datos del formulario
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Dirección:{entryDireccion.get()}\n"
            f"Teléfono:{entryTelefono.get()}\n"
            f"Sexo:{sexo.get()}\n"
            f"Enfermedades:{enfermedadesTexto}"
        )
#a la altura de info colocar
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy() #Cierra la ventana tras el mensaje
    #Fuera del def registrarDatos()
    btnRegsitrar=tk.Button(ventanaRegistro,text="Registrar datos",command=registrarDatos, font=("MS Gothic", 12), bg="white", fg="black")
    btnRegsitrar.grid(row=9,column=0,columnspan=2,pady=15)
def buscarPaciente():
    messagebox.showinfo("Buscar Paciente","Espacio para buscar pacientes")
def eliminarPaciente():
    messagebox.showinfo("Eliminar Paciente","Espacio para eliminar pacientes")
#Funcion para doctores
def nuevoDoctor():
    ventanaRegDoc=tk.Toplevel(ventanaPrincipal) 
    ventanaRegDoc.title("Registro de Doctores") 
    ventanaRegDoc.geometry("400x400") 
    ventanaRegDoc.configure(bg="blue")  # Azul
    #nombre 
    nombreLabel=tk.Label(ventanaRegDoc,text="Nombre:",bg="blue", fg="white", font=("MS Gothic", 12)) 
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n") 
    entryNombre=tk.Entry(ventanaRegDoc, font=("MS Gothic", 12)) 
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we") 
    #Direccion 
    direccionLabel=tk.Label(ventanaRegDoc,text="Direccion:",bg="blue", fg="white", font=("MS Gothic", 12)) 
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n") 
    entryDireccion=tk.Entry(ventanaRegDoc, font=("MS Gothic", 12)) 
    entryDireccion.grid(row=1, column=1,padx=10,pady=5,sticky="we") 
    #Telefono 
    telefonoLabel=tk.Label(ventanaRegDoc,text="Telefono:",bg="blue", fg="white", font=("MS Gothic", 12)) 
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n") 
    entryTelefono=tk.Entry(ventanaRegDoc, font=("MS Gothic", 12)) 
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we") 
    #sexo (radiobutton) 
    sexoLabel=tk.Label(ventanaRegDoc,text="Sexo:",bg="blue", fg="white", font=("MS Gothic", 12)) 
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="n") 
    sexo=tk.StringVar(value="Masculino") 
    rbMasculino=tk.Radiobutton(ventanaRegDoc,text="Masculino",variable=sexo,value="Masculino", bg="blue", fg="white", font=("MS Gothic", 12)) 
    rbMasculino.grid(row=3,column=1,sticky="n") 
    rbFemenino=tk.Radiobutton(ventanaRegDoc,text="Femenino",variable=sexo,value="Femenino", bg="blue", fg="white", font=("MS Gothic", 12)) 
    rbFemenino.grid(row=4,column=1,sticky="n") 
    #Especialidad 
    especialidadLabel=tk.Label(ventanaRegDoc,text="Especialidad:",bg="blue", fg="white", font=("MS Gothic", 12)) 
    especialidadLabel.grid(row=5,column=0,sticky="n") 
    entryEspecialidad=tk.Entry(ventanaRegDoc, font=("MS Gothic", 12)) 
    entryEspecialidad.grid(row=5,column=1,padx=10,pady=5,sticky="we") 
def buscarDoctor():
    messagebox.showinfo("Buscar Doctor","Espacio para buscar doctores")
def eliminarDoctor():
    messagebox.showinfo("Nuevo Paciente","Espacio para eliminar doctores")
    
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("1000x600")
ventanaPrincipal.configure(bg="blue")  # Azul
#barra de menu
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)
#menu Pacientes
menuPacientes=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes",menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente",command=nuevoPaciente)
menuPacientes.add_command(label="Buscar Paciente", command=buscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente",command=eliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir",command=ventanaPrincipal.quit)
#Menú Doctores
menuDoc=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoc)
menuDoc.add_command(label="Nuevo Doctor",command=nuevoDoctor)
menuDoc.add_command(label="Buscar Doctor", command=buscarDoctor)
menuDoc.add_command(label="Eliminar Doctor",command=eliminarDoctor)
menuDoc.add_separator()
menuDoc.add_command(label="Salir",command=ventanaPrincipal.quit)
 
#Menú Ayuda
menuAyuda=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de","Sistema de el ala de Ing biomedica v1.0\nDev: Dedalozzz"))
ventanaPrincipal.mainloop()
 