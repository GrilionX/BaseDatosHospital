from conection_db import get_connection

def agregar_cita(id_paciente, id_doctor, fecha, hora):
    conexion =get_connection()
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
        print("Error al agregar cita:", e)
        return False
    finally:
        conexion.close()

def listar_citas_paciente(id_paciente):
    conexion = get_connection()
    if not conexion:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT fecha, hora, id_doctor FROM Citas WHERE id_paciente = ?", id_paciente)
        return cursor.fetchall()
    except Exception as e:
        print("Error al listar citas:", e)
        return []
    finally:
        conexion.close()

def agregar_historial(id_paciente, descripcion):
    conexion = get_connection()
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
        print("Error al agregar historial:", e)
        return False
    finally:
        conexion.close()
