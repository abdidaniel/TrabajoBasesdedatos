import sqlite3
from modelo.VO import VehiculoVO
from db.conectar import crear_conexion


class VehiculoDAO:
    def __init__(self):
        self.conexion = crear_conexion()

    def crear_vehiculo(self, vehiculo_vo):
        """Crea un nuevo registro de vehículo"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO VEHICULO (
                    tipo_vehiculo, tipo_combustible, matricula, FK_USUARIO
                ) VALUES (?, ?, ?, ?)
            """, (
                vehiculo_vo.tipo_vehiculo, vehiculo_vo.tipo_combustible,
                vehiculo_vo.matricula, vehiculo_vo.fk_usuario
            ))
            self.conexion.commit()
            vehiculo_vo.id_vehiculo = cursor.lastrowid
            return vehiculo_vo
        except Exception as e:
            self.conexion.rollback()
            raise e

    def obtener_por_id_vehiculo(self, id_vehiculo):
        """Obtiene un vehículo por su ID"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_vehiculo, tipo_vehiculo, tipo_combustible, matricula, FK_USUARIO
            FROM VEHICULO WHERE ID_vehiculo = ?
        """, (id_vehiculo,))

        row = cursor.fetchone()
        if row:
            return VehiculoVO(
                id_vehiculo=row[0],
                tipo_vehiculo=row[1],
                tipo_combustible=row[2],
                matricula=row[3],
                fk_usuario=row[4]
            )
        return None

    def actualizar_vehiculo(self, vehiculo_vo):
        """Actualiza un vehículo existente"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                UPDATE VEHICULO
                SET tipo_vehiculo = ?, tipo_combustible = ?, matricula = ?, FK_USUARIO = ?
                WHERE ID_vehiculo = ?
            """, (
                vehiculo_vo.tipo_vehiculo, vehiculo_vo.tipo_combustible,
                vehiculo_vo.matricula, vehiculo_vo.fk_usuario,
                vehiculo_vo.id_vehiculo
            ))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e

    def eliminar_vehiculo(self, id_vehiculo):
        """Elimina un vehículo por su ID"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute(
                "DELETE FROM VEHICULO WHERE ID_vehiculo = ?", (id_vehiculo,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e

    def leer_vehiculos(self):
        """Obtiene todos los vehículos"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_vehiculo, tipo_vehiculo, tipo_combustible, matricula, FK_USUARIO
            FROM VEHICULO
        """)

        vehiculos = []
        for row in cursor.fetchall():
            vehiculos.append(VehiculoVO(
                id_vehiculo=row[0],
                tipo_vehiculo=row[1],
                tipo_combustible=row[2],
                matricula=row[3],
                fk_usuario=row[4]
            ))
        return vehiculos

    def obtener_por_usuario(self, id_usuario):
        """Obtiene todos los vehículos de un usuario específico"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_vehiculo, tipo_vehiculo, tipo_combustible, matricula, FK_USUARIO
            FROM VEHICULO
            WHERE FK_USUARIO = ?
        """, (id_usuario,))

        vehiculos = []
        for row in cursor.fetchall():
            vehiculos.append(VehiculoVO(
                id_vehiculo=row[0],
                tipo_vehiculo=row[1],
                tipo_combustible=row[2],
                matricula=row[3],
                fk_usuario=row[4]
            ))
        return vehiculos
