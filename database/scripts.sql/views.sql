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
