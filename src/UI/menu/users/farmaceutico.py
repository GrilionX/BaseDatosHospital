import pyodbc

# Configuración de la conexión a SQL Server
connection_string = "Driver={SQL Server};Server=TU_SERVIDOR;Database=TU_BASE_DE_DATOS;Trusted_Connection=yes;"
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

def listar_farmaceuticos():
    cursor.execute("SELECT * FROM Farmaceutico")
    farmaceuticos = cursor.fetchall()
    print("\nLista de Farmacéuticos:")
    for farmaceutico in farmaceuticos:
        print(f"ID: {farmaceutico.idEmpleado}, Nombre: {farmaceutico.nombre}")

def agregar_farmaceutico(idEmpleado, nombre):
    try:
        cursor.execute("INSERT INTO Farmaceutico (idEmpleado, nombre) VALUES (?, ?)", (idEmpleado, nombre))
        conn.commit()
        print("Farmacéutico agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar farmacéutico: {e}")

def eliminar_farmaceutico(idEmpleado):
    try:
        cursor.execute("DELETE FROM Farmaceutico WHERE idEmpleado = ?", (idEmpleado,))
        conn.commit()
        print("Farmacéutico eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar farmacéutico: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        print("\n1. Listar farmacéuticos\n2. Agregar farmacéutico\n3. Eliminar farmacéutico\n4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            listar_farmaceuticos()
        elif opcion == "2":
            idEmpleado = int(input("ID del empleado: "))
            nombre = input("Nombre del farmacéutico: ")
            agregar_farmaceutico(idEmpleado, nombre)
        elif opcion == "3":
            idEmpleado = int(input("ID del empleado a eliminar: "))
            eliminar_farmaceutico(idEmpleado)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
