from modelo.VO.ConfiguracionVO import ConfiguracionVO
from db.conectar import crear_conexion


class ConfiguracionDAO:
    def __init__(self):
        self.conexion = crear_conexion()

    def crear_configuracion(self, config_vo):
        """Crea un nuevo registro de configuración"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO Configuracion (
                    ID_usuario, ID_destino, ID_visualizacion, 
                    ID_vehiculo, COLPASS, alertas_trafico, idioma, navegacion
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                config_vo.id_usuario, config_vo.id_destino,
                config_vo.id_visualizacion, config_vo.id_vehiculo,
                int(config_vo.colpass), int(config_vo.alertas_trafico),
                config_vo.idioma, config_vo.navegacion
            ))
            self.conexion.commit()
            config_vo.id_confi = cursor.lastrowid
            return config_vo
        except Exception as e:
            self.conexion.rollback()
            raise e

    def obtener_por_id_configuracion(self, id_confi):
        """Obtiene una configuración por su ID"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_confi, ID_usuario, ID_destino, ID_visualizacion, 
                   ID_vehiculo, COLPASS, alertas_trafico, idioma, navegacion
            FROM Configuracion WHERE ID_confi = ?
        """, (id_confi,))

        row = cursor.fetchone()
        if row:
            return ConfiguracionVO(
                id_confi=row[0],
                id_usuario=row[1],
                id_destino=row[2],
                id_visualizacion=row[3],
                id_vehiculo=row[4],
                colpass=bool(row[5]),
                alertas_trafico=bool(row[6]),
                idioma=row[7],
                navegacion=row[8]
            )
        return None

    def actualizar_configuracion(self, config_vo):
        """Actualiza una configuración existente"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                UPDATE Configuracion
                SET ID_usuario = ?, ID_destino = ?, ID_visualizacion = ?,
                    ID_vehiculo = ?, COLPASS = ?, alertas_trafico = ?, idioma = ?, navegacion = ?
                WHERE ID_confi = ?
            """, (
                config_vo.id_usuario, config_vo.id_destino,
                config_vo.id_visualizacion, config_vo.id_vehiculo,
                int(config_vo.colpass), int(config_vo.alertas_trafico),
                config_vo.idioma, config_vo.navegacion,
                config_vo.id_confi
            ))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e

    def eliminar_configuracion(self, id_confi):
        """Elimina una configuración por su ID"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute(
                "DELETE FROM Configuracion WHERE ID_confi = ?", (id_confi,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e

    def leer_configuracion(self):
        """Obtiene todas las configuraciones"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_confi, ID_usuario, ID_destino, ID_visualizacion, 
                   ID_vehiculo, COLPASS, alertas_trafico, idioma, navegacion
            FROM Configuracion
        """)

        configuraciones = []
        for row in cursor.fetchall():
            configuraciones.append(ConfiguracionVO(
                id_confi=row[0],
                id_usuario=row[1],
                id_destino=row[2],
                id_visualizacion=row[3],
                id_vehiculo=row[4],
                colpass=bool(row[5]),
                alertas_trafico=bool(row[6]),
                idioma=row[7],
                navegacion=row[8]
            ))
        return configuraciones
