-- Usuarios
INSERT INTO Usuario (idUsuario, nombre, paterno, materno, telefono, correo, tipoUsuario) VALUES
(1, 'Carlos', 'Hernández', 'López', '5551234567', 'carlos.hernandez@gmail.com', 'Recepcionista'),
(2, 'María', 'Gómez', 'Ruiz', '5559876543', 'maria.gomez@gmail.com', 'Doctor'),
(3, 'Juan', 'Pérez', 'Sánchez', '5556781234', 'juan.perez@gmail.com', 'Paciente'),
(4, 'Ana', 'Ramírez', 'Torres', '5555674321', 'ana.ramirez@gmail.com', 'Paciente'),
(5, 'Luis', 'Martínez', 'García', '5554321765', 'luis.martinez@gmail.com', 'Farmacéutico');

-- Roles
INSERT INTO Rol (idRol, nombreRol) VALUES
(1, 'Recepcionista'),
(2, 'Doctor'),
(3, 'Farmacéutico'),
(4, 'Paciente'),
(5, 'Administrador');

-- Direcciones
INSERT INTO Direccion (idDireccion, calle, numero, colonia, codigoPostal) VALUES
(1, 'Av. Reforma', '123', 'Centro', '06000'),
(2, 'Insurgentes', '456', 'Roma', '06700'),
(3, 'Revolución', '789', 'Del Valle', '03100'),
(4, 'Tlalpan', '321', 'Coyoacán', '04300'),
(5, 'Chapultepec', '654', 'Juárez', '06600');

-- Empleados
INSERT INTO Empleado (idEmpleado, idUsuario, salario, idRol) VALUES
(1, 1, 15000, 1),
(2, 2, 25000, 2),
(3, 5, 12000, 3),
(4, 4, 18000, 4),
(5, 3, 30000, 5);

-- Recepcionistas
INSERT INTO Recepcionista (idRecepcionista, idEmpleado, numEmpleado, numPiso) VALUES
(1, 1, 1001, 1),
(2, 2, 1002, 1),
(3, 3, 1003, 2),
(4, 4, 1004, 2),
(5, 5, 1005, 3);

-- Especialidades
INSERT INTO Especialidad (idEspecialidad, nombreEspecialidad) VALUES
(1, 'Cardiología'),
(2, 'Pediatría'),
(3, 'Dermatología'),
(4, 'Neurología'),
(5, 'Gastroenterología');

-- Consultorios
INSERT INTO Consultorio (numConsultorio, numPiso) VALUES
(101, 1),
(102, 1),
(201, 2),
(202, 2),
(301, 3);

-- Doctores
INSERT INTO Doctor (idDoctor, idEmpleado, idEspecialidad, numConsultorio) VALUES
(1, 2, 1, 101),
(2, 3, 2, 102),
(3, 4, 3, 201),
(4, 5, 4, 202),
(5, 1, 5, 301);

-- Pacientes
INSERT INTO Paciente (idPaciente, idUsuario, CURP, idDireccion) VALUES
(1, 3, 'PEJ840506HDFRZS01', 1),
(2, 4, 'RAM990612HDFABC02', 2),
(3, 5, 'MAR921213HDFXYZ03', 3),
(4, 2, 'HER870101HDF12304', 4),
(5, 1, 'GOM950320HDFLMN05', 5);

-- Citas
INSERT INTO Cita (idCita, idPaciente, idDoctor, fechaCita, horaCita, estatus, gestionadaPorRecepcionista) VALUES
(1, 1, 1, '2025-01-20', '09:00', 'Agendada', 1),
(2, 2, 2, '2025-01-21', '10:00', 'Agendada', 1),
(3, 3, 3, '2025-01-22', '11:00', 'Cancelada', 0),
(4, 4, 4, '2025-01-23', '12:00', 'Completada', 1),
(5, 5, 5, '2025-01-24', '13:00', 'Agendada', 1);

-- Medicamentos
INSERT INTO Medicamento (idMedicamento, nombreMedicamento, descripcion, formaAdministracion, presentacion, cantidadInventario, precio) VALUES
(1, 'Paracetamol', 'Analgésico', 'Oral', 'Tableta', 500, 10.00),
(2, 'Ibuprofeno', 'Antiinflamatorio', 'Oral', 'Tableta', 300, 15.00),
(3, 'Omeprazol', 'Gastritis', 'Oral', 'Cápsula', 200, 20.00),
(4, 'Lorazepam', 'Ansiedad', 'Oral', 'Tableta', 100, 25.00),
(5, 'Amoxicilina', 'Antibiótico', 'Oral', 'Cápsula', 150, 30.00);

-- Servicios
INSERT INTO Servicio (idServicio, nombreServicio, precio) VALUES
(1, 'Consulta General', 300.00),
(2, 'Análisis Clínicos', 500.00),
(3, 'Radiografías', 800.00),
(4, 'Ultrasonido', 1000.00),
(5, 'Cirugía Ambulatoria', 5000.00);

-- Pagos
INSERT INTO Pago (idPago, folio, idPaciente, idServicio, fechaPago, horaPago, lineaCaptura) VALUES
(1, '20250120123456', 1, 1, '2025-01-20', '09:30', 'LC1234567890'),
(2, '20250121123457', 2, 2, '2025-01-21', '10:30', 'LC1234567891'),
(3, '20250122123458', 3, 3, '2025-01-22', '11:30', 'LC1234567892'),
(4, '20250123123459', 4, 4, '2025-01-23', '12:30', 'LC1234567893'),
(5, '20250124123460', 5, 5, '2025-01-24', '13:30', 'LC1234567894');

-- Recetas
INSERT INTO Receta (idReceta, idCita, alergias, observaciones, prescripcion, fechaReceta, horaReceta) VALUES
(1, 1, 'Ninguna', 'Paciente estable', 'Paracetamol 500mg cada 8 horas', '2025-01-20', '10:00'),
(2, 2, 'Aspirina', 'Paciente con antecedentes alérgicos', 'Ibuprofeno 200mg cada 6 horas', '2025-01-21', '11:00'),
(3, 3, 'Penicilina', 'Evitar medicamentos con penicilina', 'Omeprazol 20mg cada 24 horas', '2025-01-22', '12:00'),
(4, 4, 'Ninguna', 'Observaciones sin cambios', 'Lorazepam 2mg cada 12 horas', '2025-01-23', '13:00'),
(5, 5, 'Ninguna', 'Sin observaciones adicionales', 'Amoxicilina 500mg cada 8 horas', '2025-01-24', '14:00');

-- Medicamentos por Receta
INSERT INTO MedicamentosPorReceta (idMedicamentoReceta, idReceta, idMedicamento, cantidad) VALUES
(1, 1, 1, 10),
(2, 2, 2, 15),
(3, 3, 3, 20),
(4, 4, 4, 10),
(5, 5, 5, 25);

-- Bitácoras
INSERT INTO Bitacora (idBitacora, nombreUsuario, fecha, hora, actividad) VALUES
(1, 'Carlos Hernández', '2025-01-20', '09:05', 'Cita gestionada para el paciente Juan Pérez'),
(2, 'María Gómez', '2025-01-21', '10:10', 'Consulta registrada para análisis clínicos'),
(3, 'Luis Martínez', '2025-01-22', '11:15', 'Receta generada para el paciente Ana Ramírez'),
(4, 'Carlos Hernández', '2025-01-23', '12:20', 'Pago procesado para cirugía ambulatoria'),
(5, 'María Gómez', '2025-01-24', '13:25', 'Ultrasonido programado para Luis Martínez');

-- Tickets
INSERT INTO Ticket (numeroTicket, fecha, hora, totalPago, idPago) VALUES
(1, '2025-01-20', '09:35', 300.00, 1),
(2, '2025-01-21', '10:35', 500.00, 2),
(3, '2025-01-22', '11:35', 800.00, 3),
(4, '2025-01-23', '12:35', 1000.00, 4),
(5, '2025-01-24', '13:35', 5000.00, 5);
