from modelo.DAO.UsuarioDAO import UsuarioDAO
from modelo.VO.UsuarioVO import UsuarioVO

usuario_dao = UsuarioDAO()
nuevo_usuario = UsuarioVO(
    nombre="Julian",
    apellido="Martinez",
    correo="julian.martinez@example.com",
    sexo="Masculino"
)

ID_nuevo_usuario = usuario_dao.insertar_usuario(nuevo_usuario)

if ID_nuevo_usuario != -1:
    print(f"Usuario insertado correctamente con ID {ID_nuevo_usuario}.")
else:
    print("Error al insertar usuario.")


# usuario_a_actualizar = UsuarioVO(nombre="Manuela", apellido="Torres", correo="manuela.torres@email.com", sexo="Femenino")
# usuario_a_actualizar.ID_usuario = 16 
# if usuario_dao.actualizar_usuario(usuario_a_actualizar):
#     print("Usuario actualizado exitosamente.")
# else:
#     print("No se pudo actualizar el usuario.")

# imprimir_usuario = usuario_dao.leer_usuario(ID_usuario = 12)

# if imprimir_usuario:
#     print(f"ID: {imprimir_usuario.ID_usuario}, Nombre: {imprimir_usuario.nombre}, Apellido: {imprimir_usuario.apellido}, Correo: {imprimir_usuario.correo}, Sexo: {imprimir_usuario.sexo}")
# else:
#     print("No se encontró el usuario.")
# # nuevo_usuario = UsuarioVO(
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


