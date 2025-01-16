import tkinter as tk
from tkinter import messagebox
import pymssql

def conectar_db():
    conn = pymssql.connect(server='localhost', user='sa', password='password', database='HospitalGestion2')
    return conn

def registrar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()
    tipo_usuario = combo_tipo_usuario.get()
    
    # Verificar que no haya campos vacíos
    if not nombre or not correo or not contrasena or not tipo_usuario:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
        return

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.callproc('sp_registrarUsuario', (nombre, correo, contrasena, tipo_usuario))
    conn.commit()
    messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito")
    conn.close()

def iniciar_sesion():
    correo = entry_correo_login.get()
    contrasena = entry_contrasena_login.get()

    if not correo or not contrasena:
        messagebox.showwarning("Campos incompletos", "Por favor, complete ambos campos.")
        return

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.callproc('sp_iniciarSesion', (correo, contrasena))
    result = cursor.fetchone()

    if result is None:
        messagebox.showerror("Error", "Credenciales incorrectas.")
    else:
        tipo_usuario = result[0]
        messagebox.showinfo("Login exitoso", f"Bienvenido, {tipo_usuario}.")
    conn.close()

window = tk.Tk()
window.title("Sistema de Login")

frame_registro = tk.Frame(window)
frame_registro.pack(padx=10, pady=10)

label_registro = tk.Label(frame_registro, text="Registro de Usuario", font=("Arial", 14))
label_registro.grid(row=0, column=0, columnspan=2)

label_nombre = tk.Label(frame_registro, text="Nombre:")
label_nombre.grid(row=1, column=0)
entry_nombre = tk.Entry(frame_registro)
entry_nombre.grid(row=1, column=1)

label_correo = tk.Label(frame_registro, text="Correo:")
label_correo.grid(row=2, column=0)
entry_correo = tk.Entry(frame_registro)
entry_correo.grid(row=2, column=1)

label_contrasena = tk.Label(frame_registro, text="Contraseña:")
label_contrasena.grid(row=3, column=0)
entry_contrasena = tk.Entry(frame_registro, show="*")
entry_contrasena.grid(row=3, column=1)

label_tipo_usuario = tk.Label(frame_registro, text="Tipo de Usuario:")
label_tipo_usuario.grid(row=4, column=0)
combo_tipo_usuario = tk.Combobox(frame_registro, values=["Paciente", "Recepcionista", "Doctor"])
combo_tipo_usuario.grid(row=4, column=1)

button_registro = tk.Button(frame_registro, text="Registrar", command=registrar_usuario)
button_registro.grid(row=5, column=0, columnspan=2, pady=5)

frame_login = tk.Frame(window)
frame_login.pack(padx=10, pady=10)

label_login = tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 14))
label_login.grid(row=0, column=0, columnspan=2)

label_correo_login = tk.Label(frame_login, text="Correo:")
label_correo_login.grid(row=1, column=0)
entry_correo_login = tk.Entry(frame_login)
entry_correo_login.grid(row=1, column=1)

label_contrasena_login = tk.Label(frame_login, text="Contraseña:")
label_contrasena_login.grid(row=2, column=0)
entry_contrasena_login = tk.Entry(frame_login, show="*")
entry_contrasena_login.grid(row=2, column=1)

button_login = tk.Button(frame_login, text="Iniciar sesión", command=iniciar_sesion)
button_login.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
