import db.conectar as cbd


def usuarios_completos() -> list:

    with cbd.crear_conexion() as conector:
        sql = "SELECT * FROM Usuario;"
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def usuarios_id(id: int) -> list:

    with cbd.crear_conexion() as conector:
        sql = f"""SELECT * FROM Usuario WHERE ID_usuario = {id};"""
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def vehiculos_completos() -> list:

    with cbd.crear_conexion() as conector:
        sql = "SELECT * FROM Vehiculo;"
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def vehiculos_id(id: int) -> list:

    with cbd.crear_conexion() as conector:
        sql = f"""SELECT * FROM Vehiculo WHERE tipo_vehiculo = {id};"""
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def vehiculos_tipo(tipo_vehiculo) -> list:

    with cbd.crear_conexion() as conector:
        sql = f"""SELECT * FROM Vehiculo WHERE tipo_vehiculo = {tipo_vehiculo};"""
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def ubicaciones_completos() -> list:

    with cbd.crear_conexion() as conector:
        sql = "SELECT * FROM Dirreccion;"
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def destinos_completos() -> list:

    with cbd.crear_conexion() as conector:
        sql = "SELECT * FROM Destino;"
        cursor = conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros


def destino_mas_visitado() -> list:

    with cbd.crear_conexion() as conector:

        sql = f"""SELECT di.ID_direccion, di.nombre AS destino, COUNT(*) AS cantidad_visitas
FROM Destino d
JOIN Direccion di ON d.ID_direccion = di.ID_direccion
GROUP BY di.ID_direccion, di.nombre
ORDER BY cantidad_visitas DESC
LIMIT 1;"""
    cursor = conector.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()

    return registros


def configuracion_completos() -> list:

    with cbd.crear_conexion() as conector:
        sql = f"""SELECT c.ID_confi, u.nombre, u.apellido, v.tipo_vehiculo, d.nombre AS destino, c.COLPASS, c.alertas_trafico, c.idioma, c.navegacion
FROM Configuracion c
JOIN Usuario u ON c.ID_usuario = u.ID_usuario
LEFT JOIN Vehiculo v ON c.ID_vehiculo = v.ID_vehiculo
LEFT JOIN Destino d ON c.ID_destino = d.ID_DEST;"""

    cursor = conector.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()

    return registros


def configuracion_ID(id: int) -> list:
    with cbd.crear_conexion() as conector:
        sql = f"""SELECT c.*, u.nombre, u.apellido, v.tipo_vehiculo, dir.nombre AS destino
FROM Configuracion c
JOIN Usuario u ON c.ID_usuario = u.ID_usuario
LEFT JOIN Vehiculo v ON c.ID_vehiculo = v.ID_vehiculo
LEFT JOIN Destino d ON c.ID_destino = d.ID_DEST
LEFT JOIN Direccion dir ON d.ID_direccion = dir.ID_direccion  
WHERE c.ID_usuario = {id};"""
    cursor = conector.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()

    return registros
