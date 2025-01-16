import pyodbc
from datetime import datetime

# Configuración de la conexión a SQL Server
connection_string = "Driver={SQL Server};Server=TU_SERVIDOR;Database=TU_BASE_DE_DATOS;Trusted_Connection=yes;"
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

def registrar_actividad(nombreUsuario, actividad):
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    try:
        cursor.execute("INSERT INTO Bitacora (nombreUsuario, fecha, hora, actividad) VALUES (?, ?, ?, ?)",
                       (nombreUsuario, fecha, hora, actividad))
        conn.commit()
        print("Actividad registrada correctamente.")
    except Exception as e:
        print(f"Error al registrar actividad: {e}")

def consultar_bitacora():
    try:
        cursor.execute("SELECT * FROM Bitacora")
        actividades = cursor.fetchall()
        print("\nRegistro de Bitácora:")
        for actividad in actividades:
            print(f"ID: {actividad.idBitacora}, Usuario: {actividad.nombreUsuario}, Fecha: {actividad.fecha}, "
                  f"Hora: {actividad.hora}, Actividad: {actividad.actividad}")
    except Exception as e:
        print(f"Error al consultar bitácora: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        print("\n1. Registrar actividad\n2. Consultar bitácora\n3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombreUsuario = input("Nombre del usuario: ")
            actividad = input("Descripción de la actividad: ")
            registrar_actividad(nombreUsuario, actividad)
        elif opcion == "2":
            consultar_bitacora()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
