import tkinter as tk
from tkinter import messagebox
from UI.menu.users.recepcionista import mostrar_menu_recepcionista
from UI.menu.users.doctor import mostrar_menu_doctor
from UI.menu.users.paciente import mostrar_menu_paciente

def mostrar_pantalla_inicio():
    def abrir_recepcionista():
        ventana_inicio.destroy()
        mostrar_menu_recepcionista()

    def abrir_doctor():
        ventana_inicio.destroy()
        mostrar_menu_doctor()

    def abrir_paciente():
        ventana_inicio.destroy()
        mostrar_menu_paciente()

    ventana_inicio = tk.Tk()
    ventana_inicio.title("Sistema de Gestión Hospitalaria")

    tk.Label(ventana_inicio, text="Selecciona el tipo de usuario").pack(pady=10)

    tk.Button(ventana_inicio, text="Recepcionista", command=abrir_recepcionista).pack(pady=5)
    tk.Button(ventana_inicio, text="Doctor", command=abrir_doctor).pack(pady=5)
    tk.Button(ventana_inicio, text="Paciente", command=abrir_paciente).pack(pady=5)

    ventana_inicio.mainloop()
