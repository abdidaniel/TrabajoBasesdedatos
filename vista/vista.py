from PyQt5.QtWidgets import (QPushButton,
                             QVBoxLayout,
                             QTableWidget,
                             QTableWidgetItem,
                             QSlider,
                             QLabel,
                             QWidget,
                             QDialog,
                             QLineEdit,
                             )
from PyQt5 import QtCore, Qt


# Main GUI
# Como nota pues le organice lo que ustedes tenian ya que estaba desactualizado
# Rakad


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
