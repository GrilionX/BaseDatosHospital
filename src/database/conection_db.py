import pyodbc

def obtener_conexion():
    try:
        return pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=tu_servidor;"
            "Database=tu_base_de_datos;"
            "UID=tu_usuario;"
            "PWD=tu_contraseña;"
        )
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
