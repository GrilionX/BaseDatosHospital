import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;' 
            'DATABASE=HospitalGestion2;'
            'Trusted_Connection=yes;'
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        return None
