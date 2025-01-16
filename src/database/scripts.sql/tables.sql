--CREACION FORMAL DE LA BD
CREATE DATABASE HospitalGestion2;
GO
USE HospitalGestion2;
GO
-- Script completo de creación en 3FN actualizado para incluir que Paciente también sea un Usuario y reglas de negocio relacionadas con citas

-- Tabla: Usuarios (abstracta para roles como recepcionistas, doctores, pacientes, etc.)
CREATE TABLE Usuario (
    idUsuario INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    paterno VARCHAR(50) NOT NULL,
    materno VARCHAR(50),
    telefono VARCHAR(10),
    correo VARCHAR(50) UNIQUE NOT NULL,
    tipoUsuario VARCHAR(20) NOT NULL -- Define si es Doctor, Recepcionista, Paciente, etc.
);

-- Tabla: Roles
CREATE TABLE Rol (
    idRol INT PRIMARY KEY,
    nombreRol VARCHAR(50) NOT NULL
);

-- Tabla: Direcciones
CREATE TABLE Direccion (
    idDireccion INT PRIMARY KEY,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    colonia VARCHAR(50),
    codigoPostal VARCHAR(5)
);

-- Tabla: Empleados (empleados como farmacéuticos, recepcionistas, etc.)
CREATE TABLE Empleado (
    idEmpleado INT PRIMARY KEY,
    idUsuario INT NOT NULL,
    salario MONEY NOT NULL,
    idRol INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
    FOREIGN KEY (idRol) REFERENCES Rol(idRol)
);

-- Tabla: Recepcionistas
CREATE TABLE Recepcionista (
    idRecepcionista INT PRIMARY KEY,
    idEmpleado INT NOT NULL,
    numEmpleado INT UNIQUE NOT NULL,
    numPiso INT,
    FOREIGN KEY (idEmpleado) REFERENCES Empleado(idEmpleado)
);

-- Tabla: Especialidades
CREATE TABLE Especialidad (
    idEspecialidad INT PRIMARY KEY,
    nombreEspecialidad VARCHAR(50) NOT NULL
);

-- Tabla: Consultorios
CREATE TABLE Consultorio (
    numConsultorio INT PRIMARY KEY,
    numPiso INT NOT NULL
);

-- Tabla: Doctores
CREATE TABLE Doctor (
    idDoctor INT PRIMARY KEY,
    idEmpleado INT NOT NULL,
    idEspecialidad INT NOT NULL,
    numConsultorio INT NOT NULL,
    FOREIGN KEY (idEmpleado) REFERENCES Empleado(idEmpleado),
    FOREIGN KEY (idEspecialidad) REFERENCES Especialidad(idEspecialidad),
    FOREIGN KEY (numConsultorio) REFERENCES Consultorio(numConsultorio)
);


-- Tabla: Pacientes (ahora también son usuarios)
CREATE TABLE Paciente (
    idPaciente INT PRIMARY KEY,
    idUsuario INT NOT NULL,
    CURP VARCHAR(18) UNIQUE,
    idDireccion INT NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
    FOREIGN KEY (idDireccion) REFERENCES Direccion(idDireccion)
);

-- Tabla: Citas
CREATE TABLE Cita (
    idCita INT PRIMARY KEY,
    idPaciente INT NOT NULL,
    idDoctor INT NOT NULL,
    fechaCita DATE NOT NULL,
    horaCita TIME NOT NULL,
    estatus VARCHAR(50),
    gestionadaPorRecepcionista BIT NOT NULL DEFAULT 0, -- Indica si la cita fue gestionada por la recepcionista
    FOREIGN KEY (idPaciente) REFERENCES Paciente(idPaciente),
    FOREIGN KEY (idDoctor) REFERENCES Doctor(idDoctor)
);

-- Tabla: Recetas
CREATE TABLE Receta (
    idReceta INT PRIMARY KEY,
    idCita INT NOT NULL,
    alergias VARCHAR(150),
    observaciones VARCHAR(200),
    prescripcion VARCHAR(200),
    fechaReceta DATE NOT NULL,
    horaReceta TIME NOT NULL,
    FOREIGN KEY (idCita) REFERENCES Cita(idCita)
);

-- Tabla: Medicamentos
CREATE TABLE Medicamento (
    idMedicamento INT PRIMARY KEY,
    nombreMedicamento VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    formaAdministracion VARCHAR(50),
    presentacion VARCHAR(50),
    cantidadInventario INT NOT NULL,
    precio MONEY NOT NULL
);

-- Tabla: Medicamentos por Receta
CREATE TABLE MedicamentosPorReceta (
    idMedicamentoReceta INT PRIMARY KEY,
    idReceta INT NOT NULL,
    idMedicamento INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (idReceta) REFERENCES Receta(idReceta),
    FOREIGN KEY (idMedicamento) REFERENCES Medicamento(idMedicamento)
);

-- Tabla: Servicios
CREATE TABLE Servicio (
    idServicio INT PRIMARY KEY,
    nombreServicio VARCHAR(50) NOT NULL,
    precio MONEY NOT NULL
);

-- Tabla: Pagos
CREATE TABLE Pago (
    idPago INT PRIMARY KEY,
    folio CHAR(14) UNIQUE NOT NULL,
    idPaciente INT NOT NULL,
    idServicio INT NOT NULL,
    fechaPago DATE NOT NULL,
    horaPago TIME NOT NULL,
    lineaCaptura VARCHAR(20),
    FOREIGN KEY (idPaciente) REFERENCES Paciente(idPaciente),
    FOREIGN KEY (idServicio) REFERENCES Servicio(idServicio)
);

-- Tabla: Servicio Farmacéutico
CREATE TABLE ServicioFarmaceutico (
    idServicioF INT PRIMARY KEY,
    nombreServicio VARCHAR(50) NOT NULL,
    precio MONEY NOT NULL
);

-- Tabla: Farmacéuticos
CREATE TABLE Farmaceutico (
    idFarmaceutico INT PRIMARY KEY,
    idEmpleado INT NOT NULL,
    FOREIGN KEY (idEmpleado) REFERENCES Empleado(idEmpleado)
);

-- Tabla: Turnos
CREATE TABLE Turno (
    numTurno INT PRIMARY KEY,
    horaEntrada TIME NOT NULL,
    horaSalida TIME NOT NULL,
    diasDescanso VARCHAR(50) NOT NULL
);

-- Tabla: Bitácoras
CREATE TABLE Bitacora (
    idBitacora INT PRIMARY KEY,
    nombreUsuario VARCHAR(50),
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    actividad VARCHAR(200) NOT NULL
);

-- Tabla: Tickets
CREATE TABLE Ticket (
    numeroTicket INT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    totalPago MONEY NOT NULL,
    idPago INT NOT NULL,
    FOREIGN KEY (idPago) REFERENCES Pago(idPago)
);