# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aplicacion_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 774)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 774))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tree = QtWidgets.QTreeView(self.centralwidget)
        self.tree.setGeometry(QtCore.QRect(10, 180, 1000, 540))
        self.tree.setObjectName("tree")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 19, 991, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_Arriba = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Iconos/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Arriba.setIcon(icon2)
        self.pushButton_Arriba.setObjectName("pushButton_Arriba")
        self.horizontalLayout.addWidget(self.pushButton_Arriba)
        self.pushButton_Crear_Carpeta = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Iconos/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Crear_Carpeta.setIcon(icon3)
        self.pushButton_Crear_Carpeta.setObjectName("pushButton_Crear_Carpeta")
        self.horizontalLayout.addWidget(self.pushButton_Crear_Carpeta)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 90, 981, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Sukar")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Aceptar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Aceptar.setObjectName("pushButton_Aceptar")
        self.horizontalLayout_2.addWidget(self.pushButton_Aceptar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_Cancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Cancelar.setObjectName("pushButton_Cancelar")
        self.horizontalLayout_2.addWidget(self.pushButton_Cancelar)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_4.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_3.setText(_translate("MainWindow", "Adelante"))
        self.pushButton_Arriba.setText(_translate("MainWindow", "Arriba"))
        self.pushButton_Crear_Carpeta.setText(_translate("MainWindow", "Crear Carpeta"))
        self.label.setText(_translate("MainWindow", "Selecciona el directorio donde quieras crear el env"))
        self.pushButton_Aceptar.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_Cancelar.setText(_translate("MainWindow", "Cancelar"))

