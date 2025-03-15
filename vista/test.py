from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, Qt
import sys


class ExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Waze")
        self.setGeometry(200, 200, 800, 800)
        self.w1 = dict()
        self.w2 = dict()
        self.w3 = dict()

        self.w1['bsc_usuario'] = QPushButton("Buscar Usuario")
        self.w1['vr_historial'] = QPushButton("Ver Historial De Navegación")
        self.w1['vr_ubicacion'] = QPushButton("Ver Ubicaciones")

        self.w2['mtr_reporte'] = QPushButton("Mostra Reportes")
        self.w2['nv_reporte'] = QPushButton("Crear Reporte")
        self.w2['fn_reporte'] = QPushButton("Finalizar Reporte")

        self.w3['tbl_usuarios'] = QTableWidget()
        self.w3['tbl_ubicacion'] = QTableWidget()
        self.w3['tbl_reporte'] = QTableWidget()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = ExampleWindow()
    ex.show()

sys.exit(app.exec_())
