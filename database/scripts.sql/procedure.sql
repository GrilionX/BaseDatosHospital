-- Procedimiento para cancelar una cita y calcular el reembolso correspondiente
CREATE PROCEDURE dbo.sp_cancelar_cita
    @idCita INT,
    @fechaCancelacion DATE,
    @horaCancelacion TIME
AS
BEGIN
    DECLARE @fechaCita DATE;
    DECLARE @horaCita TIME;
    DECLARE @reembolso DECIMAL;

    -- Obtener la fecha y hora de la cita
    SELECT @fechaCita = fechaCita, @horaCita = horaCita FROM Cita WHERE idCita = @idCita;

    -- Calcular el porcentaje de reembolso
    SET @reembolso = dbo.fn_calcular_reembolso(@fechaCita, @horaCita, @fechaCancelacion, @horaCancelacion);

    -- Actualizar el estatus de la cita y mostrar el reembolso
    IF @reembolso > 0
    BEGIN
        UPDATE Cita SET estatus = 'Cancelada' WHERE idCita = @idCita;
        PRINT 'Reembolso: ' + CAST(@reembolso * 100 AS VARCHAR) + '%';
    END
    ELSE
    BEGIN
        PRINT 'No hay reembolso por cancelación tardía.';
    END
END;



-- Procedimiento para agendar una cita dentro del rango permitido
CREATE PROCEDURE dbo.sp_agendar_cita 
    @idPaciente INT, 
    @idDoctor INT, 
    @fechaCita DATE, 
    @horaCita TIME, 
    @gestionadaPorRecepcionista BIT
AS
BEGIN
    -- Verifica si la cita es válida (entre 48 horas de anticipación y 3 meses)
    IF DATEDIFF(HOUR, GETDATE(), @fechaCita + ' ' + @horaCita) >= 48 
       AND DATEDIFF(MONTH, GETDATE(), @fechaCita) <= 3
    BEGIN
        -- Inserta la cita
        INSERT INTO Cita (idPaciente, idDoctor, fechaCita, horaCita, estatus, gestionadaPorRecepcionista)
        VALUES (@idPaciente, @idDoctor, @fechaCita, @horaCita, 'Pendiente', @gestionadaPorRecepcionista);
    END
    ELSE
    BEGIN
        PRINT 'La cita no cumple con las condiciones de tiempo.';
    END
END;
