import tkinter as tk
from database.operaciones import listar_citas_paciente

def mostrar_menu_paciente():
    def consultar_citas():
        ventana_paciente.destroy()
        ventana_consulta = tk.Tk()
        ventana_consulta.title("Mis Citas")

        citas = listar_citas_paciente(id_paciente=entrada_id_paciente.get())

        for idx, cita in enumerate(citas, start=1):
            tk.Label(ventana_consulta, text=f"Cita {idx}: {cita}").pack()

        ventana_consulta.mainloop()

    ventana_paciente = tk.Tk()
    ventana_paciente.title("Menú Paciente")

    tk.Label(ventana_paciente, text="ID Paciente:").pack()
    entrada_id_paciente = tk.Entry(ventana_paciente)
    entrada_id_paciente.pack()

    tk.Button(ventana_paciente, text="Consultar Citas", command=consultar_citas).pack()
    ventana_paciente.mainloop()
