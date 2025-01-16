from database.conection_db import get_connection
import os


def initialize_database():
    script_paths = [
        'database/tables.sql',
        'database/functions.sql',
        'database/triggers.sql',
        'database/procedures.sql'
    ]

    connection = get_connection()
    if not connection:
        print("No se pudo conectar a la base de datos. Verifica la configuracion.")
        return

    try:
        cursor = connection.cursor()
        for script_path in script_paths:
            if os.path.exists(script_path):
                print(f"Ejecutando script: {script_path}...")
                with open(script_path, 'r', encoding='utf-8') as file:
                    sql_script = file.read()
                cursor.execute(sql_script)
                connection.commit()
                print(f"Script {script_path} ejecutado correctamente.")
            else:
                print(f"El archivo {script_path} no existe. Verifica la estructura del proyecto.")
        cursor.close()
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        connection.close()


def main_menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Menu de Recepcionistas")
        print("2. Menu de Doctores")
        print("3. Menu de Pacientes")
        print("4. Salir")
        
        try:
            opcion = int(input("Selecciona una opcion: "))
            if opcion == 1:
                print("Menu de Recepcionistas:")
            elif opcion == 2:
                print("Menu de Doctores:")
            elif opcion == 3:
                print("Menu de Pacientes:")
            elif opcion == 4:
                print("Saliendo del sistema. ¡Gracias por usar el Gestor del Mictlan!")
                break
            else:
                print("Opción invalida. Intenta de nuevo.")
        except ValueError:
            print("Entrada invalida. Por favor ingresa un numero.")


def main():
    """
    Punto de entrada principal del programa.
    """
    print("=== Gestor de Hospital - Mictlán ===")
    print("Inicializando sistema...")

    # Validar conexión a la base de datos
    connection = get_connection()
    if connection:
        print("Conexión a la base de datos exitosa.")
        connection.close()
    else:
        print("Error al conectar con la base de datos. Revisa la configuración.")
        return

    # Inicializar base de datos
    print("\nPreparando la base de datos...")
    initialize_database()

    # Iniciar el menú principal
    main_menu()


if __name__ == "__main__":
    main()
