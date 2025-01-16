import tkinter as tk
from tkinter import messagebox
from database.operaciones import agregar_cita, listar_citas

def mostrar_menu_recepcionista():
    def nueva_cita():
        id_paciente = entrada_id_paciente.get()
        id_doctor = entrada_id_doctor.get()
        fecha = entrada_fecha.get()
        hora = entrada_hora.get()

        if agregar_cita(id_paciente, id_doctor, fecha, hora):
            messagebox.showinfo("Éxito", "Cita agregada correctamente")
        else:
            messagebox.showerror("Error", "No se pudo agregar la cita")

    ventana_recepcionista = tk.Tk()
    ventana_recepcionista.title("Menú Recepcionista")

    tk.Label(ventana_recepcionista, text="ID Paciente:").grid(row=0, column=0)
    entrada_id_paciente = tk.Entry(ventana_recepcionista)
    entrada_id_paciente.grid(row=0, column=1)

    tk.Label(ventana_recepcionista, text="ID Doctor:").grid(row=1, column=0)
    entrada_id_doctor = tk.Entry(ventana_recepcionista)
    entrada_id_doctor.grid(row=1, column=1)

    tk.Label(ventana_recepcionista, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0)
    entrada_fecha = tk.Entry(ventana_recepcionista)
    entrada_fecha.grid(row=2, column=1)

    tk.Label(ventana_recepcionista, text="Hora (HH:MM):").grid(row=3, column=0)
    entrada_hora = tk.Entry(ventana_recepcionista)
    entrada_hora.grid(row=3, column=1)

    tk.Button(ventana_recepcionista, text="Agregar Cita", command=nueva_cita).grid(row=4, column=1)
    ventana_recepcionista.mainloop()
