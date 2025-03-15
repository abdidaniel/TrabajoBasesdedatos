import sqlite3
from modelo.VO import DireccionVO
from db.conectar import crear_conexion

class DireccionDAO:
    def __init__(self):
        self.conexion = crear_conexion()
    
    def crear(self, direccion_vo):
        """Crea un nuevo registro de dirección"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO DIRECCION (
                    nombre, latitud, longitud
                ) VALUES (?, ?, ?)
            """, (
                direccion_vo.nombre, 
                direccion_vo.latitud, 
                direccion_vo.longitud
            ))
            self.conexion.commit()
            direccion_vo.id_direccion = cursor.lastrowid
            return direccion_vo
        except Exception as e:
            self.conexion.rollback()
            raise e
    
    def obtener_por_id(self, id_direccion):
        """Obtiene una dirección por su ID"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_direccion, nombre, latitud, longitud
            FROM DIRECCION WHERE ID_direccion = ?
        """, (id_direccion,))
        
        row = cursor.fetchone()
        if row:
            return DireccionVO(
                id_direccion=row[0],
                nombre=row[1],
                latitud=row[2],
                longitud=row[3]
            )
        return None
    
    def actualizar(self, direccion_vo):
        """Actualiza una dirección existente"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("""
                UPDATE DIRECCION
                SET nombre = ?, latitud = ?, longitud = ?
                WHERE ID_direccion = ?
            """, (
                direccion_vo.nombre,
                direccion_vo.latitud,
                direccion_vo.longitud,
                direccion_vo.id_direccion
            ))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e
    
    def eliminar(self, id_direccion):
        """Elimina una dirección por su ID"""
        cursor = self.conexion.cursor()
        try:
            cursor.execute("DELETE FROM DIRECCION WHERE ID_direccion = ?", (id_direccion,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conexion.rollback()
            raise e
    
    def obtener_todos(self):
        """Obtiene todas las direcciones"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_direccion, nombre, latitud, longitud
            FROM DIRECCION
        """)
        
        direcciones = []
        for row in cursor.fetchall():
            direcciones.append(DireccionVO(
                id_direccion=row[0],
                nombre=row[1],
                latitud=row[2],
                longitud=row[3]
            ))
        return direcciones
    
    def buscar_por_nombre(self, texto_busqueda):
        """Busca direcciones por coincidencia en el nombre"""
        cursor = self.conexion.cursor()
        cursor.execute("""
            SELECT ID_direccion, nombre, latitud, longitud
            FROM DIRECCION
            WHERE nombre LIKE ?
        """, (f'%{texto_busqueda}%',))
        
        direcciones = []
        for row in cursor.fetchall():
            direcciones.append(DireccionVO(
                id_direccion=row[0],
                nombre=row[1],
                latitud=row[2],
                longitud=row[3]
            ))
        return direcciones