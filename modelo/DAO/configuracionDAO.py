import sqlite3
from modelo.VO import ConfiguracionVO
from db.conectar import crear_conexion


class ConfiguracionDAO:

    def __init__(self):
        self.conexion = crear_conexion()

    def crear_configuracion(self, config_vo):
        """Crea un nuevo registro de configuración"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO CONFIGURACION (
                    FK_USUARIO, FK_DESTINO, FK_VISUALIZACION, 
                    FK_VEHICULO, COLPASS, NAVEGACION_CHECK
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                config_vo.fk_usuario, config_vo.fk_destino,
                config_vo.fk_visualizacion, config_vo.fk_vehiculo,
                config_vo.colpass, config_vo.navegacion_check
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
            SELECT ID_CONFI, FK_USUARIO, FK_DESTINO, FK_VISUALIZACION, 
                   FK_VEHICULO, COLPASS, NAVEGACION_CHECK
            FROM CONFIGURACION WHERE ID_CONFI = ?
        """, (id_confi,))

        row = cursor.fetchone()
        if row:
            return ConfiguracionVO(
                id_confi=row[0],
                fk_usuario=row[1],
                fk_destino=row[2],
                fk_visualizacion=row[3],
                fk_vehiculo=row[4],
                colpass=bool(row[5]),
                navegacion_check=row[6]
            )
        return None

    def actualizar_configuracion(self, config_vo):
        """Actualiza una configuración existente"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                UPDATE CONFIGURACION
                SET FK_USUARIO = ?, FK_DESTINO = ?, FK_VISUALIZACION = ?,
                    FK_VEHICULO = ?, COLPASS = ?, NAVEGACION_CHECK = ?
                WHERE ID_CONFI = ?
            """, (
                config_vo.fk_usuario, config_vo.fk_destino,
                config_vo.fk_visualizacion, config_vo.fk_vehiculo,
                config_vo.colpass, config_vo.navegacion_check,
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
                "DELETE FROM CONFIGURACION WHERE ID_CONFI = ?", (id_confi,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e

    def leer_configuracion(self):
        """Obtiene todas las configuraciones"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_CONFI, FK_USUARIO, FK_DESTINO, FK_VISUALIZACION, 
                   FK_VEHICULO, COLPASS, NAVEGACION_CHECK
            FROM CONFIGURACION
        """)

        configuraciones = []
        for row in cursor.fetchall():
            configuraciones.append(ConfiguracionVO(
                id_confi=row[0],
                fk_usuario=row[1],
                fk_destino=row[2],
                fk_visualizacion=row[3],
                fk_vehiculo=row[4],
                colpass=bool(row[5]),
                navegacion_check=row[6]
            ))
        return configuraciones
