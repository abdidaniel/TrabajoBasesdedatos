from modelo import queries as Q
from vista import vista as V
from PyQt5.QtWidgets import (QApplication, QTableWidgetItem,
                             )
from PyQt5 import QtCore, Qt
import sys
import pprint as pp


# Controlador de la GUI, nota no se como putas vamos hacerlo con el DAO y VO porque tiene que relacionarse con eso, por ahora funciona con las queries

class ControladorGUI:
    def __init__(self):

        self.app = QApplication(sys.argv)

        self.ventana_main = V.VentanaMain
        self.ventana_buscar_usuario = V.VentanaBuscarUsuario
        self.ventana_obtener_vehiculo = V.VentanaObtenerVehiculo
        self.ventana_obtener_tipo_vehiculo = V.VentanaObtenerTipoVehiculo

    def _setup_handlers(self):

        # hacer estos handlers para que se saquen el valor de la vista y lo meta a "buscar"
        def handler_ventana_buscar_usuario():
            self.ventana_buscar_usuario.show()
            id = "Leer comentario arriba"
            lista = Q.usuarios_id(id)
            self.ventana_main.w3['tbl_us'].setColumnCount(5)
            self.ventana_main.w3['tbl_us'].setHorizontalHeaderLabels(
                ['id', 'nombre', 'apellido', 'correo', 'sexo'])
            self.ventana_main.w3['tbl_us'].setRouwCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[4]))

        def handler_ventana_obtener_vehiculo():
            self.ventana_obtener_vehiculo.show()
            id = "porfavor lean"
            lista = Q.vehiculos_id(id)
            self.ventana_main.w3['tbl_ve'].setColumnCount(5)
            self.ventana_main.w3['tbl_ve'].setHorizontalHeaderLabels(
                ['id', 'tipo_vehiculo', 'tipo_combustible', 'matricula', 'id_usuario'])
            self.ventana_main.w3['tbl_ve'].setRouwCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[4]))

        def handler_ventana_obtener_tipo_vehiculo():
            self.ventana_obtener_tipo_vehiculo.show()
            id = "Hi Pepa I'm dad ARRIBA MIREN ARRIBA"
            lista = Q.vehiculos_tipo(id)
            self.ventana_main.w3['tbl_ve'].setColumnCount(5)
            self.ventana_main.w3['tbl_ve'].setHorizontalHeaderLabels(
                ['id', 'tipo_vehiculo', 'tipo_combustible', 'matricula', 'id_usuario'])
            self.ventana_main.w3['tbl_ve'].setRouwCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w3['tbl_ve'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[4]))

        # REVISEN ARRIBA MANGA DE NEGROS
        # AAAAAAAAAAAAAAAAA
        # Hola

        def handler_ver_tabla_usuario():
            lista = Q.usuarios_completos
            self.ventana_main.w3['tbl_us'].setColumnCount(5)
            self.ventana_main.w3['tbl_us'].setHorizontalHeaderLabels(
                ['id', 'nombre', 'apellido', 'correo', 'sexo'])
            self.ventana_main.w3['tbl_us'].setRouwCount(len(lista))
            for index, usuario in enumerate(lista):
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(usuario[0])))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(usuario[1]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[2]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(usuario[3]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(usuario[4]))

        def handler_ver_tabla_vehiculo():
            lista = Q.vehiculos_completos
            self.ventana_main.w3['tbl_ve'].setColumnCount(5)
            self.ventana_main.w3['tbl_ve'].setHorizontalHeaderLabels(
                ['id', 'tipo_vehiculo', 'tipo_combustible', 'matricula', 'id_usuario'])
            self.ventana_main.w3['tbl_ve'].setRouwCount(len(lista))
            for index, vehiculo in enumerate(lista):
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(vehiculo[0])))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(vehiculo[1]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[2]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(vehiculo[3]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(vehiculo[4]))

        def handler_ver_tabla_ubicacion():
            lista = Q.ubicaciones_completos
            self.ventana_main.w3['tbl_ub'].setColumnCount(4)
            self.ventana_main.w3['tbl_ub'].setHorizontalHeaderLabels(
                ['id', 'nombre', 'latitud', 'longitud'])
            self.ventana_main.w3['tbl_ub'].setRouwCount(len(lista))
            for index, ubicacion in enumerate(lista):
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(ubicacion[0])))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(ubicacion[1]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(ubicacion[2]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(ubicacion[3]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(ubicacion[4]))

        def handler_ver_tabla_destino():
            lista = Q.destinos_completos
            self.ventana_main.w3['tbl_de'].setColumnCount(3)
            self.ventana_main.w3['tbl_de'].setHorizontalHeaderLabels(
                ['id', 'usuario', 'lugar'])
            self.ventana_main.w3['tbl_de'].setRouwCount(len(lista))
            for index, destino in enumerate(lista):
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 0, QTableWidgetItem(str(destino[0])))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 1, QTableWidgetItem(destino[1]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(destino[2]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 3, QTableWidgetItem(destino[3]))
                self.ventana_main.w3['tbl_us'].setItem(
                    index, 2, QTableWidgetItem(destino[4]))

      
        self.ventana_main.w1['b_vr_usuarios'].clicked.connect(
            handler_ver_tabla_usuario)
        self.ventana_main.w1['b_vr_vehiculos'].clicked.connect(
            handler_ver_tabla_vehiculo)
        self.ventana_main.w1['b_vr_ubicaciones'].clicked.connect(
            handler_ver_tabla_ubicacion)
        self.ventana_main.w1['b_vr_destino'].clicked.connect(
            handler_ver_tabla_destino)

        self.ventana_main.w1['b_bsc_usuario'].clicked.connect(
            handler_ventana_buscar_usuario)
        self.ventana_main.w2['b_bsc_vehiculo'].clicked.connect(
            handler_ventana_obtener_vehiculo)
        self.ventana_main.w2['b_ob_tipovehi'].clicked.connect(
            handler_ventana_obtener_tipo_vehiculo)

