CREATE TABLE Usuario (
    ID_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT(150),
    apellido TEXT(100),
    correo TEXT(100) UNIQUE,
    sexo TEXT(20) CHECK (sexo IN ('Masculino', 'Femenino', 'No Binario'))
);

CREATE TABLE Direccion (
    ID_direccion INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT(250),
    latitud INT(1000),
    longitud INT(1000)
);

CREATE TABLE Destino (
    ID_DEST INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_direccion INTEGER,
    ID_usuario INTEGER,
    FOREIGN KEY (ID_direccion) REFERENCES Direccion(ID_direccion),
    FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario) ON DELETE CASCADE
);

CREATE TABLE Vehiculo (
    ID_vehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_vehiculo TEXT(12) CHECK (tipo_vehiculo IN ('Combustion', 'Electrico')),
    tipo_combustible TEXT(10) CHECK (tipo_combustible IN ('Gas', 'Energia', 'Gasolina', 'ACPM')),
    matricula TEXT(6),
    ID_usuario INTEGER,
    FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario) ON DELETE CASCADE
);

CREATE TABLE Visualizacion (
    ID_visual INTEGER PRIMARY KEY AUTOINCREMENT,
    modo_oscuro TEXT CHECK (modo_oscuro IN ('Activado', 'Desactivado')),
    vista_mapa TEXT CHECK (vista_mapa IN ('2D', '3D')),
    orientacion TEXT CHECK (orientacion IN ('Norte Arriba', 'Dirección de Marcha')),
    auto_enfoque TEXT CHECK (auto_enfoque IN ('Activado', 'Desactivado'))
);

CREATE TABLE Configuracion (
    ID_confi INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_usuario INTEGER,
    ID_destino INTEGER,
    ID_visualizacion INTEGER,
    ID_vehiculo INTEGER,
    COLPASS BOOLEAN,
    alertas_trafico BOOLEAN,
    idioma TEXT(100),
    navegacion TEXT CHECK (navegacion IN ('Evita Peajes', 'No Evita')),
    FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario) ON DELETE CASCADE,
    FOREIGN KEY (ID_destino) REFERENCES Destino(ID_DEST) ON DELETE SET NULL,
    FOREIGN KEY (ID_visualizacion) REFERENCES Visualizacion(ID_visual) ON DELETE SET NULL,
    FOREIGN KEY (ID_vehiculo) REFERENCES Vehiculo(ID_vehiculo) ON DELETE SET NULL
);
