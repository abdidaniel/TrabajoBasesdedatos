import sqlite3
from modelo.VO.VisualizacionVO import VisualizacionVO
from db.conectar import crear_conexion

class VisualizacionDAO:
    def __init__(self):
        self.conexion = crear_conexion()

    def crear_visualizacion_por_defecto(self, ID_usuario: int) -> bool:
        """Crea un registro de visualización por defecto al crear un usuario."""
        sql = """INSERT INTO Visualizacion (ID_visual, modo_oscuro, vista_mapa, orientacion, auto_enfoque)
                 VALUES (?, 'Desactivado', '2D', 'Norte Arriba', 'Activado')"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (ID_usuario,))
            self.conexion.commit()
            
            return True
        except sqlite3.Error as e:
            print(f"Error al crear configuración de visualización: {e}")
            return False
        finally:
            cursor.close()

    def leer_visualizacion(self, ID_usuario: int) -> VisualizacionVO:
        """Obtiene las configuraciones de visualización de un usuario."""
        sql = "SELECT modo_oscuro, vista_mapa, orientacion, auto_enfoque FROM Visualizacion WHERE ID_visual = ?"
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (ID_usuario,))
            row = cursor.fetchone()

            if row:
                return VisualizacionVO(modo_oscuro=row[0], vista_mapa=row[1], orientacion=row[2], auto_enfoque=row[3])
            else:
                print(f"No se encontró configuración de visualización para el usuario con ID {ID_usuario}.")
                return None
        except sqlite3.Error as e:
            print(f"Error al leer visualización: {e}")
            return None
        finally:
            cursor.close()

    def actualizar_visualizacion(self, ID_usuario: int, visualizacion: VisualizacionVO) -> bool:
        """Actualiza las configuraciones de visualización de un usuario."""
        sql = """UPDATE Visualizacion 
                 SET modo_oscuro = ?, vista_mapa = ?, orientacion = ?, auto_enfoque = ?
                 WHERE ID_visual = ?"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (visualizacion.modo_oscuro, visualizacion.vista_mapa, visualizacion.orientacion, visualizacion.auto_enfoque, ID_usuario))
            self.conexion.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al actualizar visualización: {e}")
            return False
        finally:
            cursor.close()
            