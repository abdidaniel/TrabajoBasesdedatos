INSERT INTO Usuario (nombre, apellido, correo, sexo) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', 'Masculino'),
('María', 'López', 'maria.lopez@email.com', 'Femenino'),
('Carlos', 'Gómez', 'carlos.gomez@email.com', 'No Binario'),
('Ana', 'Ramírez', 'ana.ramirez@email.com', 'Femenino'),
('Pedro', 'Sánchez', 'pedro.sanchez@email.com', 'Masculino'),
('Luisa', 'Fernández', 'luisa.fernandez@email.com', 'Femenino'),
('Miguel', 'Torres', 'miguel.torres@email.com', 'Masculino'),
('Elena', 'Díaz', 'elena.diaz@email.com', 'Femenino'),
('Sofía', 'Martínez', 'sofia.martinez@email.com', 'Femenino'),
('Alejandro', 'Ruiz', 'alejandro.ruiz@email.com', 'Masculino'),
('Diana', 'Ortega', 'diana.ortega@email.com', 'Femenino'),
('Fernando', 'Vargas', 'fernando.vargas@email.com', 'Masculino');

INSERT INTO Direccion (nombre, latitud, longitud) VALUES
('Av. Principal 123', 19.432608, -99.133209),
('Calle Secundaria 456', 40.712776, -74.005974),
('Boulevard Central 789', 34.052235, -118.243683),
('Callejón Escondido 321', 41.403629, 2.174356),
('Plaza Mayor 654', 48.856613, 2.352222),
('Autopista Norte 987', 51.507351, -0.127758),
('Calle de la Paz 147', 55.755825, 37.617298),
('Avenida Sur 258', -33.868820, 151.209290),
('Calle Estrella 369', -23.550520, -46.633308),
('Paseo de los Ángeles 741', 37.774929, -122.419418),
('Carrera 7 159', 6.524379, 3.379206),
('Avenida Libertad 951', -34.603722, -58.381592);

INSERT INTO Destino (ID_direccion, ID_usuario) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12);

INSERT INTO Vehiculo (tipo_vehiculo, tipo_combustible, matricula, ID_usuario) VALUES
('Combustion', 'Gasolina', 'ABC123', 1),
('Electrico', 'Energia', 'DEF456', 2),
('Combustion', 'Gas', 'GHI789', 3),
('Electrico', 'Energia', 'JKL012', 4),
('Combustion', 'Gasolina', 'MNO345', 5),
('Electrico', 'Energia', 'PQR678', 6),
('Combustion', 'Gas', 'STU901', 7),
('Electrico', 'Energia', 'VWX234', 8),
('Combustion', 'ACPM', 'YZA567', 9),
('Electrico', 'Energia', 'BCD890', 10),
('Combustion', 'Gasolina', 'EFG123', 11),
('Electrico', 'Energia', 'HIJ456', 12);

INSERT INTO Visualizacion (modo_oscuro, vista_mapa, orientacion, auto_enfoque) VALUES
('Activado', '3D', 'Dirección de Marcha', 'Activado'),
('Desactivado', '2D', 'Norte Arriba', 'Desactivado'),
('Activado', '3D', 'Norte Arriba', 'Activado'),
('Desactivado', '2D', 'Dirección de Marcha', 'Desactivado'),
('Activado', '3D', 'Norte Arriba', 'Activado'),
('Desactivado', '2D', 'Dirección de Marcha', 'Desactivado'),
('Activado', '3D', 'Norte Arriba', 'Activado'),
('Desactivado', '2D', 'Dirección de Marcha', 'Desactivado'),
('Activado', '3D', 'Norte Arriba', 'Activado'),
('Desactivado', '2D', 'Dirección de Marcha', 'Desactivado'),
('Activado', '3D', 'Norte Arriba', 'Activado'),
('Desactivado', '2D', 'Dirección de Marcha', 'Desactivado');

INSERT INTO Configuracion (ID_usuario, ID_destino, ID_visualizacion, ID_vehiculo, COLPASS, alertas_trafico, idioma, navegacion) VALUES
(1, 1, 1, 1, TRUE, TRUE, 'Español', 'Evita Peajes'),
(2, 2, 2, 2, FALSE, TRUE, 'Inglés', 'No Evita'),
(3, 3, 3, 3, TRUE, FALSE, 'Francés', 'Evita Peajes'),
(4, 4, 4, 4, TRUE, TRUE, 'Alemán', 'No Evita'),
(5, 5, 5, 5, FALSE, FALSE, 'Italiano', 'Evita Peajes'),
(6, 6, 6, 6, TRUE, TRUE, 'Portugués', 'No Evita'),
(7, 7, 7, 7, FALSE, FALSE, 'Holandés', 'Evita Peajes'),
(8, 8, 8, 8, TRUE, TRUE, 'Ruso', 'No Evita'),
(9, 9, 9, 9, FALSE, FALSE, 'Japonés', 'Evita Peajes'),
(10, 10, 10, 10, TRUE, TRUE, 'Chino', 'No Evita'),
(11, 11, 11, 11, FALSE, FALSE, 'Coreano', 'Evita Peajes'),
(12, 12, 12, 12, TRUE, TRUE, 'Árabe', 'No Evita');
