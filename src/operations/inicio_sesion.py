from UI.menu.main_menu import mostrar_pantalla_inicio
from UI.menu.users import autenticar_usuario, registrar_usuario

def mostrar_menu_inicio():
    while True:
        opcion = mostrar_pantalla_inicio()
        if opcion == "1":
            email = input("Ingrese su correo: ")
            password = input("Ingrese su contraseña: ")
            if autenticar_usuario(email, password):
                print("Inicio de sesión exitoso.")
                # Redirigir según el tipo de usuario
            else:
                print("Credenciales incorrectas.")
        elif opcion == "2":
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")
            contraseña = input("Contraseña: ")
            tipo_usuario = input("Tipo de usuario (Paciente/Doctor/Recepcionista/Farmacéutico): ")
            registrar_usuario(nombre, correo, contraseña, tipo_usuario)
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
