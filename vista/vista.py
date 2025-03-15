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


class VentanaMain (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Waze")
        self.setGeometry(200, 200, 800, 800)
        self.w1 = dict()
        self.w2 = dict()
        self.w3 = dict()

        self.w1['b_bsc_usuario'] = QPushButton("Buscar Usuario")
        self.w1['b_historial'] = QPushButton("Ver Historial De Navegación")
        self.w1['b_ubicacion'] = QPushButton("Ver Ubicaciones")

        self.w2['b_mtr_reporte'] = QPushButton("Mostra Reportes")
        self.w2['b_cr_reporte'] = QPushButton("Crear Reporte")
        self.w2['b_fn_reporte'] = QPushButton("Finalizar Reporte")

        self.w3['tbl_usuarios'] = QTableWidget()
        self.w3['tbl_ubicacion'] = QTableWidget()
        self.w3['tbl_reporte'] = QTableWidget()

        self.cajamain = QVBoxLayout()
        self.cajamain.setContentsMargins(0, 0, 0, 0)
        self.cajamain.setSpacing(0)
        self.cajamain.setAlignment(Qt.Qt.AlignTop)

        self.cajai = QVBoxLayout()
        self.cajai.setContentsMargins(0, 0, 0, 0)
        self.cajai.setSpacing(0)
        self.cajai.setAlignment(Qt.Qt.AlignLeft)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w1.items():
            self.cajai.addWidget(w)

        self.cajad = QVBoxLayout()
        self.cajad.setContentsMargins(0, 0, 0, 0)
        self.cajad.setSpacing(0)
        self.cajad.setAlignment(Qt.Qt.AlignRight)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w2.items():
            self.cajad.addWidget(w)

        self.cajaa = QVBoxLayout()
        self.cajaa.setContentsMargins(0, 0, 0, 0)
        self.cajaa.setSpacing(0)
        self.cajaa.setAlignment(Qt.Qt.AlignBottom)

        self.layout_main = QVBoxLayout()
        for key_w, w in self.w3.items():
            self.cajaa.addWidget(w)

        self.cajamain.addWidget(self.cajai)
        self.cajamain.addWidget(self.cajad)
        self.layout_main.addLayout(self.cajaa)
        self.setLayout(self.layout_main)


class VentanaCrearReporte:

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Nuevo Evento')
        self.setGeometry(100, 100, 400, 300)
        self.w1 = dict()
        self.w2 = dict()
        self.w1['lbl_ubicacion'] = QLabel('Numero De Ubicacion: ')
        self.w2['inp_ubicacion'] = QLineEdit()
        self.w1['lbl_evento'] = QLabel('Seleccione el tipo de evento')
        self.w1['input_apellido'] = QLineEdit()
        self.w2['btn_guardar'] = QPushButton('Guardar')
        self.layout_principal = QVBoxLayout()

        for w in self.w.values():
            self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)
