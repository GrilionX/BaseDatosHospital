-- Trigger para confirmar el pago dentro de un periodo de 8 horas
CREATE TRIGGER tr_confirmar_pago
ON Pago
AFTER INSERT
AS
BEGIN
    DECLARE @idPago INT;
    DECLARE @fechaPago DATE;
    DECLARE @horaPago TIME;

    SELECT @idPago = idPago, @fechaPago = fechaPago, @horaPago = horaPago FROM inserted;

    IF DATEDIFF(HOUR, @fechaPago + ' ' + @horaPago, GETDATE()) > 8
    BEGIN
        -- Si no se confirma el pago en 8 horas, actualiza el estado de la cita
        UPDATE Cita 
        SET estatus = 'No Confirmada' 
        WHERE idPaciente = (SELECT idPaciente FROM Pago WHERE idPago = @idPago);
    END
END;
