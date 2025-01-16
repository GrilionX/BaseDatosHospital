from database.conection_db import get_connection
import os


def initialize_database():

    script_paths = [
        'database/tables.sql',
        'database/function.sql',
        'database/triggers.sql',
        'database/procedures.sql',
        'database/views.sql'
    ]

    connection = get_connection()
    if not connection:
        print("No se pudo conectar a la base de datos. Verifica la configuración.")
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

    # Inicializar base de datos
    print("\nPreparando la base de datos...")
    initialize_database()

    print("\nSistema listo. Próximamente se agregarán funcionalidades y menús.")
    print("Gracias por usar el Gestor de Hospital - Mictlán.")


if __name__ == "__main__":
    main()
