from modelo.DAO.UsuarioDAO import UsuarioDAO
from modelo.VO.UsuarioVO import UsuarioVO

usuario_dao = UsuarioDAO()

# usuario_a_actualizar = UsuarioVO(nombre="Manuela", apellido="Torres", correo="manuela.torres@email.com", sexo="Femenino")
# usuario_a_actualizar.ID_usuario = 16 
# if usuario_dao.actualizar_usuario(usuario_a_actualizar):
#     print("Usuario actualizado exitosamente.")
# else:
#     print("No se pudo actualizar el usuario.")


# nuevo_usuario = UsuarioVO(
#     nombre="Manuel",
#     apellido="Gomez",
#     correo="manuel.gomez@example.com",
#     sexo="Masculino"
#     )
# if usuario_dao.insertar_usuario(nuevo_usuario):
#     print("Usuario insertado correctamente.")
# else:
#    print("Error al insertar usuario.")


# id_a_eliminar = 16

# if usuario_dao.eliminar_usuario(id_a_eliminar):
#     print("El usuario ha sido eliminado correctamente.")
# else:
#     print("No se pudo eliminar el usuario.")