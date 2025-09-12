import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------
# Función para enmascarar fecha (guiones automáticos)
# Se ejecuta cada vez que se escribe en el campo de fecha y pone los guiones automáticamente en formato dd-mm-yyyy.
# -------------------------
def enmascarar_fecha_medicamento(event=None):
    texto = entry_fecha.get()
    limpio = ''.join(filter(str.isdigit, texto))
    formato_final = ""

    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio

    if entry_fecha.get() != formato_final:
        entry_fecha.delete(0, tk.END)
        entry_fecha.insert(0, formato_final)

# -------------------------
# Interfaz gráfica principal
# -------------------------
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x520")
ventana.minsize(700, 450)

# Frame del formulario de entrada de datos
form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)

# Campo para el nombre del medicamento
lbl_nombre = ttk.Label(form_frame, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)

# Campo para la presentación del medicamento
lbl_present = ttk.Label(form_frame, text="Presentación:")
lbl_present.grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_presentacion = ttk.Combobox(form_frame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
combo_presentacion.grid(row=1, column=1, sticky="ew", padx=6, pady=6)

# Campo para la dosis del medicamento
lbl_dosis = ttk.Label(form_frame, text="Dosis:")
lbl_dosis.grid(row=2, column=0, sticky="w", padx=6, pady=6)
entry_dosis = ttk.Entry(form_frame)
entry_dosis.grid(row=2, column=1, sticky="w", padx=6, pady=6)

# Campo para la fecha de vencimiento, con enmascarado automático de guiones
lbl_fecha = ttk.Label(form_frame, text="Fecha Vencimiento (dd-mm-yyyy):")
lbl_fecha.grid(row=3, column=0, sticky="w", padx=6, pady=6)
entry_fecha = tk.Entry(form_frame, fg="black", bg="white")
entry_fecha.grid(row=3, column=1, sticky="w", padx=6, pady=6)
entry_fecha.bind("<KeyRelease>", enmascarar_fecha_medicamento)  # Llama a la función de enmascarado al escribir

# Frame para los botones de registrar y eliminar
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1, 2, 3), weight=1)  # columnas equitativas

# Botón para registrar un medicamento
btn_registrar = ttk.Button(btn_frame, text="Registrar")
btn_registrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Botón para eliminar un medicamento seleccionado
btn_eliminar = ttk.Button(btn_frame, text="Eliminar")
btn_eliminar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Frame para la lista (Treeview) de medicamentos
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

# Treeview para mostrar la lista de medicamentos registrados
treeview = ttk.Treeview(list_frame,
                        columns=("nombre", "presentacion", "dosis", "fecha"),
                        show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fecha", text="Fecha Vencimiento")
treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fecha", width=120, anchor="center")

# Scrollbar vertical para el Treeview
scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)

# -------------------------
# Lógica de persistencia y Treeview para medicamentos
# -------------------------

# Lista en memoria de los medicamentos
medicamentos_data = []

# Guarda todos los medicamentos en el archivo medicamento.txt
def guardar_en_archivo_medicamentos():
    with open("medicamento.txt", "w", encoding="utf-8") as archivo:
        for med in medicamentos_data:
            archivo.write(
                f"{med['Nombre']}|{med['Presentación']}|{med['Dosis']}|{med['Fecha']}\n"
            )

# Registra un nuevo medicamento y lo agrega a la lista y al archivo
def registrarMedicamento():
    medicamento = {
        "Nombre": entry_nombre.get(),
        "Presentación": combo_presentacion.get(),
        "Dosis": entry_dosis.get(),
        "Fecha": entry_fecha.get()
    }
    medicamentos_data.append(medicamento)
    guardar_en_archivo_medicamentos()
    cargar_treeview_medicamentos()
    entry_nombre.delete(0, tk.END)
    combo_presentacion.set("")
    entry_dosis.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)

# Carga los medicamentos en el Treeview desde la lista en memoria
def cargar_treeview_medicamentos():
    for item in treeview.get_children():
        treeview.delete(item)
    for i, item in enumerate(medicamentos_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Presentación"],
                item["Dosis"],
                item["Fecha"]
            )
        )

# Carga los medicamentos desde el archivo medicamento.txt al iniciar la app
def cargar_desde_archivo_medicamentos():
    try:
        with open("medicamento.txt", "r", encoding="utf-8") as archivo:
            medicamentos_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    medicamento = {
                        "Nombre": datos[0],
                        "Presentación": datos[1],
                        "Dosis": datos[2],
                        "Fecha": datos[3]
                    }
                    medicamentos_data.append(medicamento)
            cargar_treeview_medicamentos()
    except FileNotFoundError:
        pass

# Elimina el medicamento seleccionado del Treeview y del archivo
def eliminar_medicamento():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar medicamento", f"¿Estás seguro de que deseas eliminar este medicamento '{treeview.item(id_item, 'values')[0]}'?"):
            del medicamentos_data[indice]
            guardar_en_archivo_medicamentos()
            cargar_treeview_medicamentos()
            messagebox.showinfo("Eliminar Medicamento", "Medicamento eliminado exitosamente")
    else:
        messagebox.showwarning("Eliminar Medicamento", "No se ha seleccionado ningún medicamento.")
        return

# Asocia los botones a sus funciones
btn_registrar.config(command=registrarMedicamento)
btn_eliminar.config(command=eliminar_medicamento)

# Al iniciar la app, carga los medicamentos guardados
cargar_desde_archivo_medicamentos()

# Inicia el bucle principal de la ventana
ventana.mainloop()


