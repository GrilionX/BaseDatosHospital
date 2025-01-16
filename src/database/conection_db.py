import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=GRILION\\SQLEXPRESS;"  # Nombre del servidor
            "DATABASE=HospitalGestion2;"   # Nombre de la base de datos
            "Trusted_Connection=yes;"      # Autenticación de Windows
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except pyodbc.Error as e:
        print("Error al conectar a la base de datos.")
        print(f"Detalle del error: {e}")
        return None
