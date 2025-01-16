import tkinter as tk
from database import agregar_cita, listar_citas, eliminar_cita
from tkinter import messagebox

def mostrar_menu_recepcionista():
    def gestionar_citas():
        ventana_recepcionista.destroy()
        ventana_citas = tk.Tk()
        ventana_citas.title("Gestión de Citas")

        def agregar_nueva_cita():
            id_paciente = entrada_id_paciente.get()
            id_doctor = entrada_id_doctor.get()
            fecha = entrada_fecha.get()
            hora = entrada_hora.get()

            if agregar_cita(id_paciente, id_doctor, fecha, hora):
                messagebox.showinfo("Éxito", "Cita agregada correctamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar la cita")

        tk.Label(ventana_citas, text="ID Paciente:").grid(row=0, column=0)
        entrada_id_paciente = tk.Entry(ventana_citas)
        entrada_id_paciente.grid(row=0, column=1)

        tk.Label(ventana_citas, text="ID Doctor:").grid(row=1, column=0)
        entrada_id_doctor = tk.Entry(ventana_citas)
        entrada_id_doctor.grid(row=1, column=1)

        tk.Label(ventana_citas, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0)
        entrada_fecha = tk.Entry(ventana_citas)
        entrada_fecha.grid(row=2, column=1)

        tk.Label(ventana_citas, text="Hora (HH:MM):").grid(row=3, column=0)
        entrada_hora = tk.Entry(ventana_citas)
        entrada_hora.grid(row=3, column=1)

        tk.Button(ventana_citas, text="Agregar Cita", command=agregar_nueva_cita).grid(row=4, column=1)
        ventana_citas.mainloop()

    ventana_recepcionista = tk.Tk()
    ventana_recepcionista.title("Menú Recepcionista")

    tk.Button(ventana_recepcionista, text="Gestionar Citas", command=gestionar_citas).pack()
    ventana_recepcionista.mainloop()
