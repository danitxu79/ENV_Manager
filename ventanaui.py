# -*- coding: utf-8 -*-

import sys  # Importamos módulo sys
from PyQt5 import uic, QtWidgets  # Importamos módulo uic y Qtwidgets

qtCreatorFile = "ventana.ui"  # Nombre del archivo UI aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)  # El modulo ui carga el archivo


class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):  # Y venga esa ventana
    def __init__(self):  # Constructor de la clase
        QtWidgets.QMainWindow.__init__(self)  # Constructor
        Ui_MainWindow.__init__(self)  # Constructor
        self.setupUi(self)  # Método Constructor de la ventana

        # Aquí ira nuestro código funcional
        self.label.setText("<html><head/><body><p><span style=\" font-size:18pt;"
                           "\">Pylsa el botón!</span></p></body></html>")
        self.pushButton.setText("Presióname")
        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.label.setText("<html><head/><body><p><span style=\" font-size:18pt; color:#55aa00;"
                           "\">Un clavito clavo Pablito</span></p></body></html>")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())
