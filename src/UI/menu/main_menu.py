from utils.styles import print_title
from database.conection_db import get_connection
import tkinter as tk
from tkinter import messagebox
from UI.menu.users.recepcionista import mostrar_menu_recepcionista
from UI.menu.users.doctor import mostrar_menu_doctor
from UI.menu.users.paciente import mostrar_menu_paciente

def iniciar_aplicacion():
    def autenticar():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()

        if usuario == "recepcionista":
            ventana.destroy()
            mostrar_menu_recepcionista()
        elif usuario == "doctor":
            ventana.destroy()
            mostrar_menu_doctor()
        elif usuario == "paciente":
            ventana.destroy()
            mostrar_menu_paciente()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    ventana = tk.Tk()
    ventana.title("Sistema de Citas Hospitalarias")

    tk.Label(ventana, text="Usuario:").grid(row=0, column=0)
    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.grid(row=0, column=1)

    tk.Label(ventana, text="Contraseña:").grid(row=1, column=0)
    entrada_contrasena = tk.Entry(ventana, show="*")
    entrada_contrasena.grid(row=1, column=1)

    tk.Button(ventana, text="Iniciar Sesión", command=autenticar).grid(row=2, column=1)

    ventana.mainloop()

