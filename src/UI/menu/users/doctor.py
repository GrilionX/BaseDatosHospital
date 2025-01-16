import tkinter as tk
from tkinter import messagebox
from database import agregar_historial, listar_historial

def mostrar_menu_doctor():
    def gestionar_historial():
        ventana_doctor.destroy()
        ventana_historial = tk.Tk()
        ventana_historial.title("Gestión de Historial Médico")

        def agregar_nuevo_historial():
            id_paciente = entrada_id_paciente.get()
            descripcion = entrada_descripcion.get("1.0", tk.END).strip()

            if agregar_historial(id_paciente, descripcion):
                messagebox.showinfo("Éxito", "Historial agregado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar el historial")

        tk.Label(ventana_historial, text="ID Paciente:").grid(row=0, column=0)
        entrada_id_paciente = tk.Entry(ventana_historial)
        entrada_id_paciente.grid(row=0, column=1)

        tk.Label(ventana_historial, text="Descripción:").grid(row=1, column=0)
        entrada_descripcion = tk.Text(ventana_historial, height=5, width=40)
        entrada_descripcion.grid(row=1, column=1)

        tk.Button(ventana_historial, text="Agregar Historial", command=agregar_nuevo_historial).grid(row=2, column=1)
        ventana_historial.mainloop()

    ventana_doctor = tk.Tk()
    ventana_doctor.title("Menú Doctor")

    tk.Button(ventana_doctor, text="Gestionar Historial Médico", command=gestionar_historial).pack()
    ventana_doctor.mainloop()
