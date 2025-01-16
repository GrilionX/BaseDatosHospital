CREATE TRIGGER TR_InsertarCita
ON Cita
AFTER INSERT
AS
BEGIN
    DECLARE @idCita INT, @nombreUsuario VARCHAR(50), @fecha DATE, @hora TIME;
    SELECT @idCita = idCita, @nombreUsuario = nombre + ' ' + paterno 
    FROM INSERTED
    JOIN Paciente ON Paciente.idPaciente = INSERTED.idPaciente
    JOIN Usuario ON Usuario.idUsuario = Paciente.idUsuario;
    
    SET @fecha = GETDATE();
    SET @hora = CONVERT(TIME, GETDATE());
    
    INSERT INTO Bitacora (nombreUsuario, fecha, hora, actividad)
    VALUES (@nombreUsuario, @fecha, @hora, CONCAT('Se insertó la cita con id ', @idCita));
END;


CREATE TRIGGER TR_ValidarCitaDuplicada
ON Cita
INSTEAD OF INSERT
AS
BEGIN
    DECLARE @fechaCita DATE, @horaCita TIME, @idDoctor INT, @numConsultorio INT;
    SELECT @fechaCita = fechaCita, @horaCita = horaCita, @idDoctor = idDoctor 
    FROM INSERTED;
    
    -- Verifica si hay conflicto con la fecha, hora o consultorio
    IF EXISTS (
        SELECT 1 
        FROM Cita
        WHERE fechaCita = @fechaCita 
          AND horaCita = @horaCita
          AND (idDoctor = @idDoctor OR numConsultorio IN 
              (SELECT numConsultorio FROM Doctor WHERE idDoctor = @idDoctor))
    )
    BEGIN
        RAISERROR ('Conflicto de horario o consultorio ocupado.', 16, 1);
        ROLLBACK TRANSACTION;
    END
    ELSE
    BEGIN
        INSERT INTO Cita (idCita, idPaciente, idDoctor, fechaCita, horaCita, estatus, gestionadaPorRecepcionista)
        SELECT idCita, idPaciente, idDoctor, fechaCita, horaCita, estatus, gestionadaPorRecepcionista
        FROM INSERTED;
    END
END;


CREATE TRIGGER TR_ModificarCita
ON Cita
AFTER UPDATE
AS
BEGIN
    DECLARE @idCita INT, @nombreUsuario VARCHAR(50), @fecha DATE, @hora TIME;
    SELECT @idCita = idCita, @nombreUsuario = nombre + ' ' + paterno 
    FROM INSERTED
    JOIN Paciente ON Paciente.idPaciente = INSERTED.idPaciente
    JOIN Usuario ON Usuario.idUsuario = Paciente.idUsuario;

    SET @fecha = GETDATE();
    SET @hora = CONVERT(TIME, GETDATE());
    
    INSERT INTO Bitacora (nombreUsuario, fecha, hora, actividad)
    VALUES (@nombreUsuario, @fecha, @hora, CONCAT('Se modificó la cita con id ', @idCita));
END;


CREATE TRIGGER TR_EliminarCita
ON Cita
AFTER DELETE
AS
BEGIN
    DECLARE @idCita INT, @nombreUsuario VARCHAR(50), @fecha DATE, @hora TIME;
    SELECT @idCita = idCita, @nombreUsuario = nombre + ' ' + paterno 
    FROM DELETED
    JOIN Paciente ON Paciente.idPaciente = DELETED.idPaciente
    JOIN Usuario ON Usuario.idUsuario = Paciente.idUsuario;

    SET @fecha = GETDATE();
    SET @hora = CONVERT(TIME, GETDATE());
    
    INSERT INTO Bitacora (nombreUsuario, fecha, hora, actividad)
    VALUES (@nombreUsuario, @fecha, @hora, CONCAT('Se eliminó la cita con id ', @idCita));
END;
