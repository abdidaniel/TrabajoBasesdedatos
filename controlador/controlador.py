from modelo import queries as Q
from modelo.DAO import configuracionDAO, UsuarioDAO, VehiculoDAO
from vista import vista as V
from PyQt5.QtWidgets import (QApplication, QTableWidgetItem,

                             )

from PyQt5 import QtCore, Qt
import sys
import pprint as pp


# Mks eso no esta dando con sus DAO y VO, lo probe con Queries y esta agarrando bien, solo hay unos errores y es que se ejecutan
# algunos metodos en vez de esperar al mensaje del popout
class ControladorGUI:
    def __init__(self):

        self.app = QApplication(sys.argv)

        self.ventana_main = V.VentanaMain()
        self.ventana_buscar = V.VentanaBuscar()
        self.ventana_usuario = V.VentanaUsuario()
        self.ventana_vehiculo = V.VentanaVehiculo()
        self.ventana_configuracion = V.VentanaConfiguracion()
        self.USU_DAO = UsuarioDAO.UsuarioDAO()
        self.CON_DAO = configuracionDAO.ConfiguracionDAO()
        self.VEH_DAO = VehiculoDAO.VehiculoDAO()

        self._setup_handlers()

    def _setup_handlers(self):

        # hacer estos handlers para que se saquen el valor de la vista y lo meta a "buscar"
        def handler_ventana_insertar_usuario():
            self.ventana_usuario.show()
            self.USU_DAO.insertar_usuario(self.USU_DAO.UsuarioVO(0, self.ventana_usuario.w2['inp_nombre'].value,
                                                                 self.ventana_usuario.w2['inp_apellido'].value,
                                                                 self.ventana_usuario.w2['inp_correo'].value,
                                                                 self.ventana_usuario.w2['inp_sexo'].value
                                                                 ))
            lista = Q.usuarios_completos()
            self.ventana_main.w4['tbl_us'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[4]))

        def handler_ventana_ver_tabla_usuario():
            lista = Q.usuarios_completos()
            self.ventana_main.w4['tbl_us'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))

        def handler_ventana_obtener_usuario():
            self.ventana_buscar.show()
            id = self.ventana_buscar.w2['spin_id'].value
            self.USU_DAO.obtener_por_id_usuario(id)
            lista = lista = Q.usuarios_completos()
            self.ventana_main.w4['tbl_us'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))

        def handler_ventana_actualizar_usuario():
            self.ventana_buscar.show()
            self.ventana_usuario.show()
            self.USU_DAO.actualizar_usuario(self.USU_DAO.UsuarioVO(self.ventana_usuario.w2['inp_nombre'].value,
                                                                   self.ventana_usuario.w2['inp_apellido'].value,
                                                                   self.ventana_usuario.w2['inp_correo'].value,
                                                                   self.ventana_usuario.w2['inp_sexo'].value,
                                                                   self.ventana_buscar.w2['spin_id'].value
                                                                   ))
            lista = self.USU_DAO.leer_usuario()
            self.ventana_main.w4['tbl_us'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[4]))

        def handler_ventana_eliminar_usuario():
            self.ventana_buscar.show()
            id = self.ventana_buscar.w2['spin_id'].value
            self.USU_DAO.eliminar_usuario(id)
            lista = self.USU_DAO.leer_usuario()
            self.ventana_main.w4['tbl_us'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[4]))
        # |  | || | | | |  | | |  | | |

        def handler_ventana_insertar_vehiculo():
            self.ventana_vehiculo.show()
            self.VEH_DAO.crear_vehiculo(self.VEH_DAO.VehiculoVO(self.ventana_usuario.w2['inp_tipo_vehiculo'].value,
                                                                self.ventana_usuario.w2['inp_tipo_combustible'].value,
                                                                self.ventana_usuario.w2['inp_matricula'].value,
                                                                self.ventana_usuario.w2['inp_id_usuario'].value
                                                                ))
            lista = self.VEH_DAO.leer_vehiculos()
            self.ventana_main.w4['tbl_ve'].setRowCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 4, QTableWidgetItem(str(vehiculo[4])))

        def handler_ventana_ver_tabla_vehiculo():
            lista = self.VEH_DAO.leer_vehiculos()
            self.ventana_main.w4['tbl_ve'].setRowCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 4, QTableWidgetItem(vehiculo[4]))

        def handler_ventana_obtener_vehiculo():
            self.ventana_buscar.show()
            id = self.ventana_buscar.w2['spin_id'].value
            lista = self.VEH_DAO.obtener_por_id_vehiculo(id)
            self.ventana_main.w4['tbl_ve'].setRowCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 4, QTableWidgetItem(vehiculo[4]))

        def handler_ventana_actualizar_vehiculo():
            self.ventana_buscar.show()
            self.ventana_vehiculo.show()
            self.VEH_DAO.actualizar_vehiculo(self.VEH_DAO.VehiculoVO(self.ventana_usuario.w2['inp_tipo_vehiculo'].value,
                                                                     self.ventana_usuario.w2[
                'inp_tipo_combustible'].value,
                self.ventana_usuario.w2['inp_matricula'].value,
                self.ventana_usuario.w2['inp_id_usuario'].value,
                self.ventana_buscar.w2['spin_id'].value
            ))
            lista = self.VEH_DAO.leer_vehiculos()
            self.ventana_main.w4['tbl_ve'].setRowCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 4, QTableWidgetItem(str(vehiculo[4])))

        def handler_ventana_eliminar_vehiculo():
            self.ventana_buscar.show()
            id = self.ventana_buscar.w2['spin_id'].value
            self.VEH_DAO.eliminar_vehiculo(id)
            lista = self.VEH_DAO.leer_vehiculos()
            self.ventana_main.w4['tbl_ve'].setRowCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 4, QTableWidgetItem(vehiculo[4]))

        # |  | | | | | | | | | | || | | |

        def handler_ventana_insertar_configuracion():
            self.ventana_configuracion.show()
            self.CON_DAO.crear_configuracion(self.CON_DAO.ConfiguracionDAO(self.ventana_usuario.w2['inp_id_usuario'].value,
                                                                           self.ventana_usuario.w2[
                'inp_id_destino'].value,
                self.ventana_usuario.w2[
                'inp_id_visualizacion'].value,
                self.ventana_usuario.w2['inp_id_vehiculo'].value,
                self.ventana_usuario.w2['inp_colpass'].value,
                self.ventana_usuario.w2['inp_alertas'].value,
                self.ventana_usuario.w2['inp_idioma'].value,
                self.ventana_usuario.w2['inp_navegacion'].value,
            ))
            lista = self.CON_DAO.leer_configuracion()
            self.ventana_main.w4['tbl_con'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 5, QTableWidgetItem(usuario[5]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 6, QTableWidgetItem(usuario[6]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 7, QTableWidgetItem(usuario[7]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 8, QTableWidgetItem(usuario[8]))

        def handler_ventana_ver_tabla_configuracion():
            lista = self.CON_DAO.leer_configuracion()
            self.ventana_main.w4['tbl_con'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 5, QTableWidgetItem(usuario[5]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 6, QTableWidgetItem(usuario[6]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 7, QTableWidgetItem(usuario[7]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 8, QTableWidgetItem(usuario[8]))

        def handler_ventana_obtener_configuracion():
            self.ventana_buscar.show()
            id = self.ventana_buscar.w2['spin_id'].value
            lista = self.CON_DAO.obtener_por_id_configuracion(
                id)
            lista = self.CON_DAO.leer_configuracion()
            self.ventana_main.w4['tbl_con'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 5, QTableWidgetItem(usuario[5]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 6, QTableWidgetItem(usuario[6]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 7, QTableWidgetItem(usuario[7]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 8, QTableWidgetItem(usuario[8]))

        def handler_ventana_actualizar_configuracion():
            self.ventana_buscar.show()
            self.ventana_configuracion.show()
            self.CON_DAO.actualizar_configuracion(self.CON_DAO.ConfiguracionVO(self.ventana_usuario.w2['inp_id_usuario'].value,
                                                                               self.ventana_usuario.w2[
                'inp_id_destino'].value,
                self.ventana_usuario.w2[
                'inp_id_visualizacion'].value,
                self.ventana_usuario.w2[
                'inp_id_vehiculo'].value,
                self.ventana_usuario.w2[
                'inp_colpass'].value,
                self.ventana_usuario.w2[
                'inp_alertas'].value,
                self.ventana_usuario.w2['inp_idioma'].value,
                self.ventana_usuario.w2[
                'inp_navegacion'].value,
                self.ventana_buscar.w2['spin_id'].value
            ))
            lista = self.CON_DAO.leer_configuracion()
            self.ventana_main.w4['tbl_con'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 5, QTableWidgetItem(usuario[5]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 6, QTableWidgetItem(usuario[6]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 7, QTableWidgetItem(usuario[7]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 8, QTableWidgetItem(usuario[8]))

        def handler_ventana_eliminar_configuracion():
            self.ventana_buscar.show()
            id = self.ventana_buscar.w2['spin_id'].value
            self.CON_DAO.ConfiguracionDAO.eliminar_configuracion(id)
            lista = self.CON_DAO.ConfiguracionDAO.leer_configuracion()
            self.ventana_main.w4['tbl_con'].setRowCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 4, QTableWidgetItem(usuario[4]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 5, QTableWidgetItem(usuario[5]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 6, QTableWidgetItem(usuario[6]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 7, QTableWidgetItem(usuario[7]))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 8, QTableWidgetItem(usuario[8]))

        self.ventana_main.w1['b_bsc_usuario'].clicked.connect(
            handler_ventana_obtener_usuario)
        self.ventana_main.w1['b_vr_usuarios'].clicked.connect(
            handler_ventana_ver_tabla_usuario)
        self.ventana_main.w1['b_aña_usuario'].clicked.connect(
            handler_ventana_insertar_usuario)
        self.ventana_main.w1['b_eli_usuario'].clicked.connect(
            handler_ventana_eliminar_usuario)
        self.ventana_main.w1['b_act_usuario'].clicked.connect(
            handler_ventana_actualizar_usuario)

        self.ventana_main.w2['b_bsc_vehiculo'].clicked.connect(
            handler_ventana_obtener_vehiculo)
        self.ventana_main.w2['b_vr_vehiculos'].clicked.connect(
            handler_ventana_ver_tabla_vehiculo)
        self.ventana_main.w2['b_aña_vehiculo'].clicked.connect(
            handler_ventana_insertar_vehiculo)
        self.ventana_main.w2['b_eli_vehiculo'].clicked.connect(
            handler_ventana_eliminar_vehiculo)
        self.ventana_main.w2['b_act_vehiculo'].clicked.connect(
            handler_ventana_actualizar_vehiculo)

        self.ventana_main.w3['b_bsc_config'].clicked.connect(
            handler_ventana_obtener_configuracion)
        self.ventana_main.w3['b_vr_configs'].clicked.connect(
            handler_ventana_ver_tabla_configuracion)
        self.ventana_main.w3['b_aña_config'].clicked.connect(
            handler_ventana_insertar_configuracion)
        self.ventana_main.w3['b_eli_config'].clicked.connect(
            handler_ventana_eliminar_configuracion)
        self.ventana_main.w3['b_act_config'].clicked.connect(
            handler_ventana_actualizar_configuracion)

    def mainloop(self):
        print(self.ventana_main.w2['b_bsc_vehiculo'])
        self.ventana_main.show()

        self.app.exec_()
