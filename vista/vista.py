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


class VentanaMain (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Waze")
        self.setGeometry(200, 200, 800, 800)
        self.w1 = dict()
        self.w2 = dict()
        self.w3 = dict()

        self.w1['b_bsc_usuario'] = QPushButton("Buscar Usuario")
        self.w1['b_vr_usuarios'] = QPushButton("Ver Usuarios")
        self.w1['b_vr_ubicaciones'] = QPushButton("Ver Ubicaciones")
        self.w1['b_vr_configuracion'] = QPushButton(
            "Ver Configuraciones de usuarios")
        self.w1['b_ob_configuracion'] = QPushButton(
            "Ver configuraciones de un usuario")

        self.w2['b_vr_destino'] = QPushButton("Ver Destinos")
        self.w2['b_vr_vehiculos'] = QPushButton("Ver Vehiculos")
        self.w2['b_buscar_vehiculo'] = QPushButton("Buscar vehiculo")
        self.w2['b_ob_tipovehi'] = QPushButton("Obtener tipo vehiculo")
        self.w2['b_ob_destino'] = QPushButton("Obtener Destino más visitado")

        self.w3['tbl_1'] = QTableWidget()
        self.w3['tbl_2'] = QTableWidget()

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

        self.cajaa = QVBoxLayout()
        self.cajaa.setContentsMargins(0, 0, 0, 0)
        self.cajaa.setSpacing(0)
        self.cajaa.setAlignment(Qt.Qt.AlignBottom)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w3.items():
            self.cajaa.addWidget(w)

        self.cajamain.addLayout(self.cajai)
        self.cajamain.addLayout(self.cajad)
        self.layout_main.addLayout(self.cajamain)
        self.layout_main.addLayout(self.cajaa)
        self.setLayout(self.layout_main)

# Clase de boton bsc usuario


class VentanaBuscarUsuario:
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vehiculo")
        self.setGeometry(100, 100, 400, 100)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_usuario'] = QLabel('ID del usuario:')

        self.w2['radio_gasolina'] = QSpinBox()
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


class VentanaObtenerVehiculo:

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Vehiculo")
        self.setGeometry(100, 100, 400, 100)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_vehiculo'] = QLabel('ID del Vehiculo:')

        self.w2['inp_vehiculo'] = QSpinBox()
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


# Obtener Tipo de vehiculo por el combustible xd
class VentanaObtenerTipoVehiculo:

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Tipo de Vehiculos")
        self.setGeometry(100, 100, 400, 100)
        self.w1 = dict()
        self.w2 = dict()

        self.w1['lbl_vehiculo'] = QLabel('Seleccione el tipo de vehiculo')
        self.w1['btn_buscar'] = QPushButton('Buscar')
        self.w2['radio_gasolina'] = QRadioButton("Gasolina", self)
        self.w2['radio_energia'] = QRadioButton("Energia", self)
        self.w2['radio_gas'] = QRadioButton("Gas", self)

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
        self.w1['btn_buscar'].clicked.connect(self.accept)
