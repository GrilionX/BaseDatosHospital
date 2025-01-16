from database.conection_db import obtener_conexion

def agregar_cita(id_paciente, id_doctor, fecha, hora):
    conexion = obtener_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Citas (id_paciente, id_doctor, fecha, hora)
            VALUES (?, ?, ?, ?)
        """, id_paciente, id_doctor, fecha, hora)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al agendar cita:", e)
        return False
    finally:
        conexion.close()

def listar_citas_paciente(id_paciente):
    conexion = obtener_conexion()
    if not conexion:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT fecha, hora, id_doctor FROM Citas WHERE id_paciente = ?", id_paciente)
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar citas:", e)
        return []
    finally:
        conexion.close()

def agregar_historial(id_paciente, descripcion):
    conexion = obtener_conexion()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Historial (id_paciente, descripcion)
            VALUES (?, ?)
        """, id_paciente, descripcion)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al agregar registro:", e)
        return False
    finally:
        conexion.close()
