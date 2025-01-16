import tkinter as tk
from database.operaciones import listar_pacientes

def mostrar_pacientes():
    ventana_pacientes = tk.Tk()
    ventana_pacientes.title("Lista de Pacientes")

    pacientes = listar_pacientes()
    for idx, paciente in enumerate(pacientes, start=1):
        tk.Label(ventana_pacientes, text=f"{idx}. {paciente['nombre']} - ID: {paciente['id']}").pack()

    ventana_pacientes.mainloop()
