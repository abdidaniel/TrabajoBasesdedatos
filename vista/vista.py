from PyQt5.QtWidgets import (QPushButton,
                             QVBoxLayout,
                             QTableWidget,
                             QTableWidgetItem,
                             QSlider,
                             QLabel,
                             QWidget,
                             QDialog,
                             QLineEdit,
                             QSpinBox,
                             QRadioButton,
                             QHBoxLayout,
                             )
from PyQt5 import QtCore, Qt

# Main GUI
# Como nota pues le organice lo que ustedes tenian ya que estaba desactualizado

# Nota update, ptm toco volverlo a cuadrar jadawjdajdmawi, hare todo porque si


class VentanaMain (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Waze")
        self.setGeometry(200, 200, 800, 800)
        self.w1 = dict()
        self.w2 = dict()
        self.w3 = dict()
        self.w4 = dict()

        self.w1['b_bsc_usuario'] = QPushButton("Buscar Usuario")
        self.w1['b_vr_usuarios'] = QPushButton("Ver Usuarios")
        self.w1['b_aña_usuario'] = QPushButton("Añadir Usuario")
        self.w1['b_eli_usuario'] = QPushButton(
            "Eliminar Usuario")
        self.w1['b_act_usuario'] = QPushButton(
            "actualizar usuario")

        self.w2['b_bsc_vehiculo'] = QPushButton("Buscar vehiculo")
        self.w2['b_vr_vehiculos'] = QPushButton("Ver vehiculo")
        self.w2['b_aña_vehiculo'] = QPushButton("Añadir vehiculo")
        self.w2['b_eli_vehiculo'] = QPushButton(
            "Eliminar vehiculo")
        self.w2['b_act_vehiculo'] = QPushButton(
            "Actualizar vehiculo")

        self.w3['b_bsc_config'] = QPushButton("Buscar Configuración")
        self.w3['b_vr_configs'] = QPushButton("Ver Configuraciones")
        self.w3['b_aña_config'] = QPushButton("Añadir Configuración")
        self.w3['b_eli_config'] = QPushButton("Eliminar Configuración")
        self.w3['b_act_config'] = QPushButton(
            "Actualizar Configuración")

        self.w4['lbl_us'] = QLabel('Tabla Usuarios')
        self.w4['tbl_us'] = QTableWidget()
        self.w4['tbl_us'].setColumnCount(5)
        self.w4['tbl_us'].setHorizontalHeaderLabels(
            ['id', 'nombre', 'apellido', 'correo', 'sexo'])

        self.w4['lbl_ve'] = QLabel('Tabla Vehiculos')
        self.w4['tbl_ve'] = QTableWidget()
        self.w4['tbl_ve'].setColumnCount(5)
        self.w4['tbl_ve'].setHorizontalHeaderLabels(
            ['id', 'tipo_vehiculo', 'tipo_combustible', 'matricula', 'id_usuario'])

        self.w4['lbl_con'] = QLabel('Tabla Configuracion')
        self.w4['tbl_con'] = QTableWidget()
        self.w4['tbl_con'].setColumnCount(9)
        self.w4['tbl_con'].setHorizontalHeaderLabels(
            ['id', 'id_usuario', 'id_destino', 'id_visualización',
             'id_vehiculo', 'COLPASS', 'alertas', 'idioma', 'navegacion'])

        self.cajamain = QHBoxLayout()
        self.cajamain.setContentsMargins(0, 0, 0, 0)
        self.cajamain.setSpacing(0)
        self.cajamain.setAlignment(Qt.Qt.AlignTop)

        self.cajad = QVBoxLayout()
        self.cajad.setContentsMargins(0, 0, 0, 0)
        self.cajad.setSpacing(0)
        self.cajad.setAlignment(Qt.Qt.AlignRight)

        self.cajai = QVBoxLayout()
        self.cajai.setContentsMargins(0, 0, 0, 0)
        self.cajai.setSpacing(0)
        self.cajai.setAlignment(Qt.Qt.AlignLeft)

        self.cajam = QVBoxLayout()
        self.cajam.setContentsMargins(0, 0, 0, 0)
        self.cajam.setSpacing(0)
        self.cajam.setAlignment(Qt.Qt.AlignCenter)

        self.cajaa = QVBoxLayout()
        self.cajaa.setContentsMargins(0, 0, 0, 0)
        self.cajaa.setSpacing(0)
        self.cajaa.setAlignment(Qt.Qt.AlignBottom)
        # recorrida de layouts
        self.layout_main = QVBoxLayout()
        for key_w, w in self.w1.items():
            self.cajai.addWidget(w)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w2.items():
            self.cajad.addWidget(w)
        self.layout_main = QVBoxLayout()
        for key_w, w in self.w3.items():
            self.cajam.addWidget(w)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w4.items():
            self.cajaa.addWidget(w)

        self.cajamain.addLayout(self.cajai)
        self.cajamain.addLayout(self.cajam)
        self.cajamain.addLayout(self.cajad)

        self.layout_main.addLayout(self.cajamain)
        self.layout_main.addLayout(self.cajaa)
        self.setLayout(self.layout_main)

# Clase de boton bsc usuario

# Removi todo porque no era con iba con los requerimientos del profesor


class VentanaBuscar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buscar")
        self.setGeometry(100, 100, 400, 100)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_usuario'] = QLabel('ID:')

        self.w2['spin_id'] = QSpinBox()
        self.w2['btn_buscar'] = QPushButton('Buscar')

        self.cajamain = QHBoxLayout()
        self.cajamain.setContentsMargins(0, 0, 0, 0)
        self.cajamain.setSpacing(0)
        self.cajamain.setAlignment(Qt.Qt.AlignTop)

        self.cajad = QVBoxLayout()
        self.cajad.setContentsMargins(0, 0, 0, 0)
        self.cajad.setSpacing(0)
        self.cajad.setAlignment(Qt.Qt.AlignRight)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w2.items():
            self.cajad.addWidget(w)

        self.cajai = QVBoxLayout()
        self.cajai.setContentsMargins(0, 0, 0, 0)
        self.cajai.setSpacing(0)
        self.cajai.setAlignment(Qt.Qt.AlignLeft)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w1.items():
            self.cajai.addWidget(w)

        self.cajamain.addLayout(self.cajai)
        self.cajamain.addLayout(self.cajad)
        self.layout_main.addLayout(self.cajamain)
        self.setLayout(self.layout_main)
        self.w2['btn_buscar'].clicked.connect(self.accept)

# Removi el crear reporte porque pues, no va con los administradores, transferido a obtener vehiculo
# Creacion de ventanas de addicion


class VentanaUsuario(QDialog):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Usuario")
        self.setGeometry(100, 100, 400, 200)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_nombre'] = QLabel('Nombre')
        self.w1['lbl_apellido'] = QLabel('Apellido ')
        self.w1['lbl_correo'] = QLabel('Correo')
        self.w2['lbl_sexo'] = QLabel('Sexo')
        self.w1['btn_buscar'] = QPushButton('Buscar')
        self.w2['inp_nombre'] = QLineEdit()
        self.w2['inp_apellido'] = QLineEdit()
        self.w2['inp_correo'] = QLineEdit()
        self.w2['inp_sexo'] = QLineEdit()

        self.cajamain = QHBoxLayout()
        self.cajamain.setContentsMargins(0, 0, 0, 0)
        self.cajamain.setSpacing(0)
        self.cajamain.setAlignment(Qt.Qt.AlignTop)

        self.cajad = QVBoxLayout()
        self.cajad.setContentsMargins(0, 0, 0, 0)
        self.cajad.setSpacing(0)
        self.cajad.setAlignment(Qt.Qt.AlignRight)

        self.cajai = QVBoxLayout()
        self.cajai.setContentsMargins(0, 0, 0, 0)
        self.cajai.setSpacing(0)
        self.cajai.setAlignment(Qt.Qt.AlignLeft)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w1.items():
            self.cajai.addWidget(w)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w2.items():
            self.cajad.addWidget(w)

        self.cajamain.addLayout(self.cajai)
        self.cajamain.addLayout(self.cajad)
        self.layout_main.addLayout(self.cajamain)
        self.setLayout(self.layout_main)
        self.w1['btn_buscar'].clicked.connect(self.accept)


class VentanaConfiguracion(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuracion")
        self.setGeometry(100, 100, 400, 300)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_id_usuario'] = QLabel('ID Usuario')
        self.w1['lbl_id_destino'] = QLabel('ID Destino')
        self.w1['lbl_id_visualizacion'] = QLabel('ID Visualización')
        self.w1['lbl_id_vehiculo'] = QLabel('ID Vehículo')
        self.w1['lbl_colpass'] = QLabel('COLPASS')
        self.w1['lbl_alertas'] = QLabel('Alertas Tráfico')
        self.w1['lbl_idioma'] = QLabel('Idioma')
        self.w1['lbl_navegacion'] = QLabel('Navegación')

        self.w2['inp_id_usuario'] = QSpinBox()
        self.w2['inp_id_destino'] = QSpinBox()
        self.w2['inp_id_visualizacion'] = QSpinBox()
        self.w2['inp_id_vehiculo'] = QSpinBox()
        self.w2['inp_colpass'] = QSpinBox()
        self.w2['inp_colpass'].setMinimum(0)
        self.w2['inp_colpass'].setMaximum(1)
        self.w2['inp_alertas'] = QSpinBox()
        self.w2['inp_alertas'].setMaximum(1)
        self.w2['inp_alertas'].setMinimum(0)
        self.w2['inp_idioma'] = QLineEdit()
        self.w2['inp_navegacion'] = QLineEdit()
        self.w1['btn_guardar'] = QPushButton('Guardar')

        self.cajamain = QHBoxLayout()
        self.cajamain.setContentsMargins(0, 0, 0, 0)
        self.cajamain.setSpacing(0)
        self.cajamain.setAlignment(Qt.Qt.AlignTop)

        self.cajad = QVBoxLayout()
        self.cajad.setContentsMargins(0, 0, 0, 0)
        self.cajad.setSpacing(0)
        self.cajad.setAlignment(Qt.Qt.AlignRight)

        self.cajai = QVBoxLayout()
        self.cajai.setContentsMargins(0, 0, 0, 0)
        self.cajai.setSpacing(0)
        self.cajai.setAlignment(Qt.Qt.AlignLeft)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w1.items():
            self.cajai.addWidget(w)

        for key_w, w in self.w2.items():
            self.cajad.addWidget(w)

        self.cajamain.addLayout(self.cajai)
        self.cajamain.addLayout(self.cajad)
        self.layout_main.addLayout(self.cajamain)
        self.setLayout(self.layout_main)
        self.w1['btn_guardar'].clicked.connect(self.accept)


class VentanaVehiculo(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vehiculo")
        self.setGeometry(100, 100, 400, 100)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_tipo_vehiculo'] = QLabel('Tipo de Vehiculo')
        self.w1['lbl_tipo_combustible'] = QLabel('Tipo de combustible')
        self.w1['lbl_matricula'] = QLabel('Matricula')
        self.w1['lbl_id_usuario'] = QLabel('ID_usuario')
        self.w2['inp_tipo_vehiculo'] = QLineEdit()
        self.w2['inp_tipo_combustible'] = QLineEdit()
        self.w2['inp_matricula'] = QLineEdit()
        self.w2['inp_id_usuario'] = QSpinBox()
        self.w1['btn_guardar'] = QPushButton('Guardar')

        self.cajamain = QHBoxLayout()
        self.cajamain.setContentsMargins(0, 0, 0, 0)
        self.cajamain.setSpacing(0)
        self.cajamain.setAlignment(Qt.Qt.AlignTop)

        self.cajad = QVBoxLayout()
        self.cajad.setContentsMargins(0, 0, 0, 0)
        self.cajad.setSpacing(0)
        self.cajad.setAlignment(Qt.Qt.AlignRight)

        self.cajai = QVBoxLayout()
        self.cajai.setContentsMargins(0, 0, 0, 0)
        self.cajai.setSpacing(0)
        self.cajai.setAlignment(Qt.Qt.AlignLeft)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w1.items():
            self.cajai.addWidget(w)

        for key_w, w in self.w2.items():
            self.cajad.addWidget(w)

        self.cajamain.addLayout(self.cajai)
        self.cajamain.addLayout(self.cajad)
        self.layout_main.addLayout(self.cajamain)
        self.setLayout(self.layout_main)
        self.w1['btn_guardar'].clicked.connect(self.accept)

