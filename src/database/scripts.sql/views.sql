-- Vista de citas canceladas con información del paciente, doctor y reembolso
CREATE VIEW dbo.vw_citas_canceladas AS
SELECT 
    c.idCita,
    p.nombre + ' ' + p.paterno AS Paciente,
    d.nombre + ' ' + d.paterno AS Doctor,
    c.fechaCita,
    c.horaCita,
    c.estatus,
    dbo.fn_calcular_reembolso(c.fechaCita, c.horaCita, GETDATE(), GETDATE()) AS Reembolso
FROM Cita c
JOIN Paciente p ON c.idPaciente = p.idPaciente
JOIN Doctor d ON c.idDoctor = d.idDoctor
WHERE c.estatus = 'Cancelada';

-- Vista para obtener todas las citas activas (no canceladas)
CREATE VIEW VistaCitasActivas AS
SELECT Citas.id, Citas.id_paciente, Citas.id_doctor, Citas.fecha, Citas.hora, Pacientes.nombre AS nombre_paciente, Doctores.nombre AS nombre_doctor
FROM Citas
INNER JOIN Pacientes ON Citas.id_paciente = Pacientes.id
INNER JOIN Doctores ON Citas.id_doctor = Doctores.id
WHERE Citas.cancelada = 0;

-- Vista para obtener las citas por paciente
CREATE VIEW VistaCitasPorPaciente AS
SELECT Citas.id, Citas.id_doctor, Citas.fecha, Citas.hora, Doctores.nombre AS nombre_doctor
FROM Citas
INNER JOIN Doctores ON Citas.id_doctor = Doctores.id
WHERE Citas.id_paciente = @id_paciente AND Citas.cancelada = 0;


CREATE PROCEDURE sp_iniciarSesion
    @correo VARCHAR(50),
    @contraseña VARCHAR(255)
AS
BEGIN
    DECLARE @tipoUsuario VARCHAR(20);
    
    -- Verificar si las credenciales son correctas
    SELECT @tipoUsuario = tipoUsuario
    FROM VistaUsuarios
    WHERE correo = @correo AND contraseña = @contraseña;
    
    IF @tipoUsuario IS NULL
    BEGIN
        SELECT 'Credenciales incorrectas';
    END
    ELSE
    BEGIN
        SELECT @tipoUsuario AS tipoUsuario;
    END
END;
