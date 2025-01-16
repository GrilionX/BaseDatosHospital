-- Función para calcular el porcentaje de reembolso según la política del hospital
CREATE FUNCTION dbo.fn_calcular_reembolso (
    @fechaCita DATE, 
    @horaCita TIME, 
    @fechaCancelacion DATE, 
    @horaCancelacion TIME
) RETURNS DECIMAL
AS
BEGIN
    DECLARE @diferenciaHoras INT;
    DECLARE @reembolso DECIMAL;

    -- Calcula la diferencia en horas entre la cancelación y la cita
    SET @diferenciaHoras = DATEDIFF(HOUR, @fechaCancelacion + ' ' + @horaCancelacion, @fechaCita + ' ' + @horaCita);

    -- Reglas para calcular el reembolso
    IF @diferenciaHoras >= 48
        SET @reembolso = 1.00;  -- 100% de reembolso
    ELSE IF @diferenciaHoras >= 24
        SET @reembolso = 0.50;  -- 50% de reembolso
    ELSE
        SET @reembolso = 0.00;  -- Sin reembolso

    RETURN @reembolso;
END;