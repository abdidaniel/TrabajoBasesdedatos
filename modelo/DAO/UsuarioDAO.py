import sqlite3
from modelo.VO.UsuarioVO import UsuarioVO
from db.conectar import crear_conexion
from modelo.DAO.VisualizacionDAO import VisualizacionDAO

class UsuarioDAO:

    def __init__(self):
        self.conexion = crear_conexion()
        self.visualizacion_dao = VisualizacionDAO() 
    #Insertar usuario
    def insertar_usuario(self, usuario: UsuarioVO) -> bool:
        """Inserta un nuevo usuario en la base de datos."""
        sql = """INSERT INTO Usuario (nombre, apellido, correo, sexo)
                 VALUES (?, ?, ?, ?)"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (usuario.nombre, usuario.apellido, usuario.correo, usuario.sexo))
            self.conexion.commit()
            ID_usuario = cursor.lastrowid  # Obtener el ID del usuario recién insertado
            self.visualizacion_dao.crear_visualizacion_por_defecto(ID_usuario)  # Crear configuración visual

            return True
        except sqlite3.Error as e:
            print(f"Error al insertar usuario: {e}")
            return False
        finally:
            cursor.close()
    #ELiminar usuario
    def eliminar_usuario(self, id_usuario: int) -> bool:
        """Elimina un usuario de la base de datos por su ID."""
        sql = "DELETE FROM Usuario WHERE ID_usuario = ?"
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (id_usuario,))
            self.conexion.commit()
            
            if cursor.rowcount > 0:
                print(f"Usuario con ID {id_usuario} eliminado correctamente.")
                return True
            else:
                print(f"No se encontró un usuario con ID {id_usuario}.")
                return False
        except sqlite3.Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            cursor.close()
    #Actualizar usuario
    def actualizar_usuario(self, usuario: UsuarioVO)  -> bool:
        """Actualiza un usuario de la base de datos por su ID."""
        sql = """UPDATE Usuario 
                 SET nombre = ?, apellido = ?, correo = ?, sexo = ?
                 WHERE ID_usuario = ?"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (usuario.nombre, usuario.apellido, usuario.correo, usuario.sexo, usuario.ID_usuario))
            self.conexion.commit()
            
            if cursor.rowcount > 0:
                print(f"Usuario con ID {usuario.ID_usuario} actualizado correctamente.")
                return True
            else:
                print(f"No se encontró un usuario con ID {usuario.ID_usuario}.")
                return False
        except sqlite3.Error as e:
            print(f"Error al actualizar usuario: {e}")
            return False
        finally:
            cursor.close()
    #Imprimir usuario
    def leer_usuario(self, ID_usuario: int) -> UsuarioVO:
        """Obtiene un usuario de la base de datos por su ID."""
        sql = "SELECT ID_usuario, nombre, apellido, correo, sexo FROM Usuario WHERE ID_usuario = ?"
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (ID_usuario,))
            row = cursor.fetchone()

            if row:
                usuario = UsuarioVO(nombre=row[1], apellido=row[2], correo=row[3], sexo=row[4])
                usuario.ID_usuario = row[0]
                return usuario
            else:
                print(f"No se encontró el usuario con ID {ID_usuario}.")
                return None
        except sqlite3.Error as e:
            print(f"Error al leer usuario: {e}")
            return None
        finally:
            cursor.close()



