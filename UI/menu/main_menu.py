from utils.styles import print_title
from database.conection_db import get_connection

def display_main_menu():
    connection = get_connection()
    if not connection:
        print("No se pudo establecer la conexión con la base de datos. Saliendo...")
        return

    print_title("Gestor Hospital Mictlán")
    print("1. Gestión de pacientes")
    print("2. Gestión de médicos")
    print("3. Gestión de citas")
    print("4. Gestión de recetas")
    print("5. Salir")

    try:
        option = int(input("Selecciona una opción: "))
        if option == 1:
            print("Funcionalidad de Gestión de pacientes aún no implementada.")
        elif option == 2:
            print("Funcionalidad de Gestión de médicos aún no implementada.")
        elif option == 3:
            print("Funcionalidad de Gestión de citas aún no implementada.")
        elif option == 4:
            print("Funcionalidad de Gestión de recetas aún no implementada.")
        elif option == 5:
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
