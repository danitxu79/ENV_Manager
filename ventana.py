# -*- coding: utf-8 -*-

from ventana_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        super().__init__()
        self.setupUi(self)
        self.label.setText("Haz clic en el botón")
        self.setWindowTitle("File explorer 1.0")
        self.pushButton.setText("Presióname")
        # Conectamos los eventos con sus acciones
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
