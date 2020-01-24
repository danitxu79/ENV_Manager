# -*- coding: utf-8 -*-
import ctypes

from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QTreeView, QVBoxLayout

from aplicacion_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        super().__init__()
        self.model = QFileSystemModel()
        self.tree = QTreeView()
        self.setupUi(self)
        self.title = 'Env Manager 1.0'
        self.left = 500
        self.top = 150
        self.width = 1024
        self.height = 840
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.model.setRootPath('')
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setGeometry(25,150,975,800)
        self.tree.setWindowTitle("Dir View")
        # self.tree.resize(1000, 480)
        # Fijar el tamaño mínimo
        self.setMinimumSize(1024, 774)
        # Fijar el tamaño máximo
        self.setMaximumSize(1024, 774)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
        # self.label.setText("Selecciona el directorio donde quieres crean el env")
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        top = (resolucion_alto / 2) - (self.frameSize().height() / 2)
        self.move(left, top)
        #     self.show()
        # Mostrar el texto del primer elemento seleccionado.
        # item = self.tree.selection()[0]
        # print(self.tree.item(item, option="text"))
        item = self.tree.selectedIndexes()[0]
        print(self.tree.item(item, option="text"))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()
