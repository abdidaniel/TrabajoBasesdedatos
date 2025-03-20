from modelo import queries as Q
from modelo.DAO import configuracionDAO, UsuarioDAO, VehiculoDAO
from vista import vista as V
from PyQt5.QtWidgets import (QApplication, QTableWidgetItem,

                             )

from PyQt5 import QtCore, Qt
import sys
import pprint as pp


# Fixeado todo
# algunos metodos en vez de esperar al mensaje del popout
class ControladorGUI:
    def __init__(self):

        self.app = QApplication(sys.argv)

        self.ventana_main = V.VentanaMain()
        self.ventana_actualizar = V.VentanaActualizar()
        self.ventana_buscar = V.VentanaBuscar()
        self.ventana_eliminar = V.VentanaEliminar()
        self.ventana_usuario = V.VentanaUsuario()
        self.ventana_vehiculo = V.VentanaVehiculo()
        self.ventana_configuracion = V.VentanaConfiguracion()
        self.USU_DAO = UsuarioDAO.UsuarioDAO()
        self.CON_DAO = configuracionDAO.ConfiguracionDAO()
        self.VEH_DAO = VehiculoDAO.VehiculoDAO()

        self._setup_handlers()

    def _setup_handlers(self):

        # hacer estos handlers para que se saquen el valor de la vista y lo meta a "buscar"

        def handler_funcion_insertar_usuario():
            self.USU_DAO.insertar_usuario(UsuarioDAO.UsuarioVO(nombre=self.ventana_usuario.w2['inp_nombre'].text(),
                                                               apellido=self.ventana_usuario.w2['inp_apellido'].text(
            ),
                correo=self.ventana_usuario.w2['inp_correo'].text(
            ),
                sexo=self.ventana_usuario.w2['inp_sexo'].text(
            )
            ))

        def handler_ventana_insertar_usuario():
            self.ventana_usuario.show()

        def handler_ventana_ver_tabla_usuario():
            lista = self.USU_DAO.leer_usuario()
            self.ventana_main.w4['tbl_us'].setRowCount(
                len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario.ID_usuario)))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario.nombre))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario.apellido))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario.correo))
                self.ventana_main.w4['tbl_us'].setItem(
                    index, 4, QTableWidgetItem(usuario.sexo))

        def handler_funcion_obtener_usuario():

            usuario = self.USU_DAO.obtener_por_id_usuario(
                self.ventana_buscar.w2['spin_id'].value())
            self.ventana_main.w4['tbl_us'].setRowCount(1)
            self.ventana_main.w4['tbl_us'].setItem(
                0, 0, QTableWidgetItem(str(usuario.ID_usuario)))
            self.ventana_main.w4['tbl_us'].setItem(
                0, 1, QTableWidgetItem(usuario.nombre))
            self.ventana_main.w4['tbl_us'].setItem(
                0, 2, QTableWidgetItem(usuario.apellido))
            self.ventana_main.w4['tbl_us'].setItem(
                0, 3, QTableWidgetItem(usuario.correo))
            self.ventana_main.w4['tbl_us'].setItem(
                0, 4, QTableWidgetItem(usuario.sexo))

        def handler_ventana_obtener_usuario():
            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_obtener_vehiculo)
            except:
                print("ya desconectado")

            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_obtener_configuracion)
            except:
                print("ya desconetada")

            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_obtener_usuario)
            except:
                ("Ya conectado")
            self.ventana_buscar.show()

        def handler_funcion_actualizar_usuario():
            self.USU_DAO.actualizar_usuario(UsuarioDAO.UsuarioVO(nombre=self.ventana_usuario.w2['inp_nombre'].text(), apellido=self.ventana_usuario.w2['inp_apellido'].text(
            ), correo=self.ventana_usuario.w2['inp_correo'].text(), sexo=self.ventana_usuario.w2['inp_sexo'].text(), ID_usuario=self.ventana_buscar.w2['spin_id'].value()))

        def handler_ventana_actualizar_usuario():
            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_actualizar_vehiculo)
            except:
                print("ya desconectado")

            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_actualizar_configuracion)
            except:
                print("ya desconetada")

            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_actualizar_usuario)
            except:
                ("Ya conectado")
            self.ventana_usuario.show()
            self.ventana_actualizar.show()

        def handler_funcion_eliminar_usuario():

            self.USU_DAO.eliminar_usuario(
                self.ventana_eliminar.w2['spin_id'].value())
            self.ventana_eliminar.close()

        def handler_ventana_eliminar_usuario():
            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_eliminar_vehiculo)
            except:
                print("ya desconectado")

            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_eliminar_configuracion)
            except:
                print("ya desconetada")

            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_eliminar_usuario)
            except:
                ("Ya conectado")
            self.ventana_eliminar.show()

        # |  | | | | | | |  | | |  | | |

        def handler_funcion_insertar_vehiculo():
            self.VEH_DAO.crear_vehiculo(VehiculoDAO.VehiculoVO(tipo_vehiculo=self.ventana_usuario.w2['inp_tipo_vehiculo'].text(),
                                                               tipo_combustible=self.ventana_usuario.w2[
                'inp_tipo_combustible'].text(),
                matricula=self.ventana_usuario.w2['inp_matricula'].text(
            ),
                id_vehiculo=self.ventana_usuario.w2['inp_id_usuario'].value(
            )
            ))

        def handler_ventana_insertar_vehiculo():
            self.ventana_vehiculo.show()

        def handler_ventana_ver_tabla_vehiculo():
            self.ventana_main.w4['tbl_ve'].setRowCount(
                len(self.VEH_DAO.leer_vehiculos()))
            for index, vehiculo in enumerate(self.VEH_DAO.leer_vehiculos()):
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo.id_vehiculo)))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo.tipo_vehiculo))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo.tipo_combustible))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo.matricula))
                self.ventana_main.w4['tbl_ve'].setItem(
                    index, 4, QTableWidgetItem(str(vehiculo.fk_usuario)))

        def handler_funcion_obtener_vehiculo():

            usuario = self.VEH_DAO.obtener_por_id_vehiculo(
                self.ventana_buscar.w2['spin_id'].value())
            self.ventana_main.w4['tbl_ve'].setRowCount(1)
            self.ventana_main.w4['tbl_ve'].setItem(
                0, 0, QTableWidgetItem(str(usuario.id_vehiculo)))
            self.ventana_main.w4['tbl_ve'].setItem(
                0, 1, QTableWidgetItem(usuario.tipo_vehiculo))
            self.ventana_main.w4['tbl_ve'].setItem(
                0, 2, QTableWidgetItem(usuario.tipo_combustible))
            self.ventana_main.w4['tbl_ve'].setItem(
                0, 3, QTableWidgetItem(usuario.matricula))
            self.ventana_main.w4['tbl_ve'].setItem(
                0, 4, QTableWidgetItem(str(usuario.fk_usuario)))

        def handler_ventana_obtener_vehiculo():
            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_obtener_usuario)

            except:
                print("ya desconectado")

            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_obtener_configuracion)
            except:
                print("ya desconetada")

            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_obtener_vehiculo)
            except:
                ("Ya conectado")
            self.ventana_buscar.show()

        def handler_funcion_actualizar_vehiculo():
            self.VEH_DAO.actualizar_vehiculo(VehiculoDAO.VehiculoVO(
                id_vehiculo=self.ventana_buscar.w2['spin_id'].value(),
                tipo_vehiculo=self.ventana_vehiculo.w2['inp_tipo_vehiculo'].text(
                ),
                tipo_combustible=self.ventana_vehiculo.w2['inp_tipo_combustible'].text(
                ),
                matricula=self.ventana_vehiculo.w2['inp_matricula'].text(),
                fk_usuario=self.ventana_vehiculo.w2['inp_id_usuario'].value()
            ))

        def handler_ventana_actualizar_vehiculo():
            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_actualizar_usuario)
            except:
                print("ya desconectado")

            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_actualizar_configuracion)
            except:
                print("ya desconetada")

            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_actualizar_vehiculo)
            except:
                ("Ya conectado")
            self.ventana_actualizar.show()
            self.ventana_vehiculo.show()

        def handler_funcion_eliminar_vehiculo():
            self.USU_DAO.eliminar_usuario(
                self.ventana_eliminar.w2['spin_id'].value())
            self.ventana_eliminar.close()

        def handler_ventana_eliminar_vehiculo():
            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_eliminar_usuario)
            except:
                print("ya desconectado")

            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_eliminar_configuracion)
            except:
                print("ya desconetada")

            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_eliminar_vehiculo)
            except:
                ("Ya conectado")
            self.ventana_eliminar.show()

            # |  | | | | | | | | | | || | | |

        # | | | | | | | | | | |
        def handler_funcion_insertar_configuracion():
            self.CON_DAO.crear_configuracion(configuracionDAO.ConfiguracionVO(
                id_destino=self.ventana_configuracion.w2['inp_id_destino'].value(
                ),
                id_usuario=self.ventana_configuracion.w2['inp_id_usuario'].value(
                ),
                id_visualizacion=self.ventana_configuracion.w2['inp_id_visualizacion'].value(
                ),
                id_vehiculo=self.ventana_configuracion.w2['inp_id_vehiculo'].value(
                ),
                colpass=self.ventana_configuracion.w2['inp_colpass'].value(),
                alertas_trafico=self.ventana_configuracion.w2['inp_alertas'].value(
                ),
                idioma=self.ventana_configuracion.w2['inp_idioma'].text(),
                navegacion=self.ventana_configuracion.w2['inp_navegacion'].text()))

        def handler_ventana_insertar_configuracion():
            self.ventana_configuracion.show()

        def handler_ventana_ver_tabla_configuracion():
            self.ventana_main.w4['tbl_con'].setRowCount(
                len(self.CON_DAO.leer_configuracion()))
            for index, usuario in enumerate(self.CON_DAO.leer_configuracion()):
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 0, QTableWidgetItem(str(usuario.id_confi)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 1, QTableWidgetItem(str(usuario.id_usuario)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 2, QTableWidgetItem(str(usuario.id_destino)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 3, QTableWidgetItem(str(usuario.id_visualizacion)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 4, QTableWidgetItem(str(usuario.id_vehiculo)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 5, QTableWidgetItem(str(usuario.colpass)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 6, QTableWidgetItem(str(usuario.alertas_trafico)))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 7, QTableWidgetItem(usuario.idioma))
                self.ventana_main.w4['tbl_con'].setItem(
                    index, 8, QTableWidgetItem(usuario.navegacion))

        def handler_funcion_obtener_configuracion():
            usuario = self.CON_DAO.obtener_por_id_configuracion(
                self.ventana_buscar.w2['spin_id'].value())
            self.ventana_main.w4['tbl_con'].setRowCount(1)
            self.ventana_main.w4['tbl_con'].setItem(
                0, 0, QTableWidgetItem(str(usuario.id_confi)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 1, QTableWidgetItem(str(usuario.id_usuario)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 2, QTableWidgetItem(str(usuario.id_destino)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 3, QTableWidgetItem(str(usuario.id_visualizacion)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 4, QTableWidgetItem(str(usuario.id_vehiculo)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 5, QTableWidgetItem(str(usuario.colpass)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 6, QTableWidgetItem(str(usuario.alertas_trafico)))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 7, QTableWidgetItem(usuario.idioma))
            self.ventana_main.w4['tbl_con'].setItem(
                0, 8, QTableWidgetItem(usuario.navegacion))

        def handler_ventana_obtener_configuracion():

            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.disconnect()
            except:
                print("no habia comunicacion")

            try:
                self.ventana_buscar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_obtener_configuracion)
            except:
                print("ya conectado")
            self.ventana_buscar.show()

        def handler_funcion_actualizar_configuracion():
            self.CON_DAO.actualizar_configuracion(configuracionDAO.ConfiguracionVO(
                id_destino=self.ventana_configuracion.w2['inp_id_destino'].value(
                ),
                id_usuario=self.ventana_configuracion.w2['inp_id_usuario'].value(
                ),
                id_vehiculo=self.ventana_configuracion.w2['inp_id_vehiculo'].value(
                ),
                id_visualizacion=self.ventana_configuracion.w2['inp_id_visualizacion'],
                colpass=self.ventana_configuracion.w2['inp_colpass'].value(),
                alertas_trafico=self.ventana_configuracion.w2['inp_alertas'].value(
                ),
                navegacion=self.ventana_configuracion['inp_navegacion'].text(),
                id_confi=self.ventana_actualizar.w2['spin_id'].value()))

        def handler_ventana_actualizar_configuracion():
            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_actualizar_vehiculo)
            except:
                print("ya desconectado")

            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.disconnect(
                    handler_funcion_actualizar_usuario)
            except:
                print("ya desconetada")

            try:
                self.ventana_actualizar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_actualizar_configuracion)
            except:
                ("Ya conectado")
            self.ventana_actualizar.show()
            self.ventana_configuracion.show()

        def handler_funcion_eliminar_configuracion():
            self.CON_DAO.eliminar_configuracion(
                self.ventana_eliminar.w2['spin_id'].value())
            self.ventana_eliminar.close()

        def handler_ventana_eliminar_configuracion():
            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.disconnect()
            except:
                print("ya desconectado")

            try:
                self.ventana_eliminar.w2['btn_buscar'].clicked.connect(
                    handler_funcion_eliminar_configuracion)
            except:
                ("Ya conectado")
            self.ventana_eliminar.show()

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

        self.ventana_usuario.w1['btn_buscar'].clicked.connect(
            handler_funcion_insertar_usuario)
        self.ventana_configuracion.w1['btn_guardar'].clicked.connect(
            handler_funcion_insertar_configuracion)
        self.ventana_vehiculo.w1['btn_guardar'].clicked.connect(
            handler_funcion_insertar_vehiculo)

    def mainloop(self):
        print(self.ventana_main.w2['b_bsc_vehiculo'])
        self.ventana_main.show()

        self.app.exec_()
