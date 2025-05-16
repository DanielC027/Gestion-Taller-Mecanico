# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(999, 922)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Estilos generales */\n"
"QWidget {\n"
"    background-color: #F8F9FA; /* Gris claro */\n"
"}\n"
"\n"
"* {\n"
"    font-family: 'Verdana', sans-serif;\n"
"}\n"
"\n"
"/* Estilos para QLabel */\n"
"QLabel {\n"
"    color: #333333; /* Gris oscuro */\n"
"}\n"
"\n"
"/* Estilos para QPushButton */\n"
"QPushButton {\n"
"    background-color: #007BFF; /* Azul */\n"
"    color: #FFFFFF;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: #007BFF;\n"
"    border-radius: 15px; /* Esto har\u00e1 que los botones sean redondos */\n"
"    padding: 5px;\n"
"    min-width: 80px;\n"
"    max-width: 150px;\n"
"    min-height: 25px;\n"
"    max-height: 40px;\n"
"}\n"
"\n"
"/* Cuando el mouse est\u00e1 sobre el bot\u00f3n */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Azul oscuro */\n"
"    border-color: #0056b3;\n"
"}\n"
"\n"
"/* Estilos para QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"    border: 1px solid #CCCCCC;\n"
"}\n"
"\n"
"/* Est"
                        "ilos para QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"    border: 1px solid #CCCCCC;\n"
"}\n"
"\n"
"/* Estilos para QTableWidget */\n"
"QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"    gridline-color: #CCCCCC;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #E9ECEF; /* Gris claro */\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"    border: 1px solid #CCCCCC;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #007BFF; /* Azul */\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* Estilos para errores o alertas */\n"
"QMessageBox {\n"
"    background-color: #DC3545; /* Rojo */\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* Estilos para QGroupBox */\n"
"QGroupBox {\n"
"    background-color: #E9ECEF; /* Gris claro */\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding-top: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #333333; /* Gris oscu"
                        "ro */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_superior = QFrame(self.frame_principal)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_53 = QLabel(self.frame_superior)
        self.label_53.setObjectName(u"label_53")
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_53)

        self.pushButton_inicio = QPushButton(self.frame_superior)
        self.pushButton_inicio.setObjectName(u"pushButton_inicio")
        self.pushButton_inicio.setMaximumSize(QSize(160, 50))
        self.pushButton_inicio.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"iconos/1200px-Motorkontrollleuchte.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_inicio.setIcon(icon)
        self.pushButton_inicio.setIconSize(QSize(70, 70))

        self.horizontalLayout_7.addWidget(self.pushButton_inicio)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frame_principal)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_botones = QFrame(self.frame_inferior)
        self.frame_botones.setObjectName(u"frame_botones")
        self.frame_botones.setStyleSheet(u"QFrame {\n"
"    /*background-color: black;*/\n"
"    color: white; /* Cambia el color del texto si es necesario */\n"
"    border-radius: 10px; /* Ajusta el valor para redondear m\u00e1s o menos las esquinas */\n"
"}\n"
"")
        self.frame_botones.setFrameShape(QFrame.StyledPanel)
        self.frame_botones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_botones)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_clientes = QPushButton(self.frame_botones)
        self.pushButton_clientes.setObjectName(u"pushButton_clientes")
        self.pushButton_clientes.setMinimumSize(QSize(94, 39))
        self.pushButton_clientes.setMaximumSize(QSize(164, 54))
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_clientes.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"iconos/persona.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clientes.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.pushButton_clientes)

        self.pushButton_autos = QPushButton(self.frame_botones)
        self.pushButton_autos.setObjectName(u"pushButton_autos")
        self.pushButton_autos.setMinimumSize(QSize(94, 39))
        self.pushButton_autos.setMaximumSize(QSize(164, 54))
        self.pushButton_autos.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"iconos/auto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_autos.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.pushButton_autos)

        self.pushButton_servicios = QPushButton(self.frame_botones)
        self.pushButton_servicios.setObjectName(u"pushButton_servicios")
        self.pushButton_servicios.setMinimumSize(QSize(94, 39))
        self.pushButton_servicios.setMaximumSize(QSize(164, 54))
        self.pushButton_servicios.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"iconos/llave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_servicios.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.pushButton_servicios)


        self.horizontalLayout.addWidget(self.frame_botones)

        self.frame_paginas = QFrame(self.frame_inferior)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_paginas)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.label_37 = QLabel(self.page_inicio)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(310, 200, 211, 71))
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.label_37.setFont(font2)
        self.stackedWidget.addWidget(self.page_inicio)
        self.page_clientes = QWidget()
        self.page_clientes.setObjectName(u"page_clientes")
        self.gridLayout_6 = QGridLayout(self.page_clientes)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_c = QFrame(self.page_clientes)
        self.frame_c.setObjectName(u"frame_c")
        self.frame_c.setFrameShape(QFrame.StyledPanel)
        self.frame_c.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_c)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.frame_c)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_51 = QLabel(self.frame)
        self.label_51.setObjectName(u"label_51")
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_51.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_51)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_c)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.nombre_cliente_crear_cliente_lineEdit = QLineEdit(self.groupBox)
        self.nombre_cliente_crear_cliente_lineEdit.setObjectName(u"nombre_cliente_crear_cliente_lineEdit")

        self.gridLayout_2.addWidget(self.nombre_cliente_crear_cliente_lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.telefono_cliente_crear_cliente_lineEdit = QLineEdit(self.groupBox)
        self.telefono_cliente_crear_cliente_lineEdit.setObjectName(u"telefono_cliente_crear_cliente_lineEdit")

        self.gridLayout_2.addWidget(self.telefono_cliente_crear_cliente_lineEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.descripcion_cliente_crear_cliente_plainText = QPlainTextEdit(self.groupBox)
        self.descripcion_cliente_crear_cliente_plainText.setObjectName(u"descripcion_cliente_crear_cliente_plainText")

        self.gridLayout_2.addWidget(self.descripcion_cliente_crear_cliente_plainText, 2, 1, 1, 1)

        self.guardar_crear_cliente_button = QPushButton(self.groupBox)
        self.guardar_crear_cliente_button.setObjectName(u"guardar_crear_cliente_button")

        self.gridLayout_2.addWidget(self.guardar_crear_cliente_button, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.mostrar_clientes_clientes_tableWidget = QTableWidget(self.groupBox_3)
        self.mostrar_clientes_clientes_tableWidget.setObjectName(u"mostrar_clientes_clientes_tableWidget")

        self.gridLayout_7.addWidget(self.mostrar_clientes_clientes_tableWidget, 0, 0, 1, 1)

        self.mostrar_mostrar_clientes_button = QPushButton(self.groupBox_3)
        self.mostrar_mostrar_clientes_button.setObjectName(u"mostrar_mostrar_clientes_button")

        self.gridLayout_7.addWidget(self.mostrar_mostrar_clientes_button, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_9 = QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)

        self.nombre_cliente_actualizar_cliente_lineEdit = QLineEdit(self.groupBox_2)
        self.nombre_cliente_actualizar_cliente_lineEdit.setObjectName(u"nombre_cliente_actualizar_cliente_lineEdit")

        self.gridLayout_9.addWidget(self.nombre_cliente_actualizar_cliente_lineEdit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)

        self.telefono_cliente_actualizar_cliente_lineEdit = QLineEdit(self.groupBox_2)
        self.telefono_cliente_actualizar_cliente_lineEdit.setObjectName(u"telefono_cliente_actualizar_cliente_lineEdit")

        self.gridLayout_9.addWidget(self.telefono_cliente_actualizar_cliente_lineEdit, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 2, 0, 1, 1)

        self.descripcion_cliente_actualizar_cliente_plainText = QPlainTextEdit(self.groupBox_2)
        self.descripcion_cliente_actualizar_cliente_plainText.setObjectName(u"descripcion_cliente_actualizar_cliente_plainText")

        self.gridLayout_9.addWidget(self.descripcion_cliente_actualizar_cliente_plainText, 2, 1, 1, 1)

        self.actualizar_actualizar_cliente_button = QPushButton(self.groupBox_2)
        self.actualizar_actualizar_cliente_button.setObjectName(u"actualizar_actualizar_cliente_button")

        self.gridLayout_9.addWidget(self.actualizar_actualizar_cliente_button, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.nombre_cliente_eliminar_cliente_lineEdit = QLineEdit(self.groupBox_4)
        self.nombre_cliente_eliminar_cliente_lineEdit.setObjectName(u"nombre_cliente_eliminar_cliente_lineEdit")

        self.gridLayout_8.addWidget(self.nombre_cliente_eliminar_cliente_lineEdit, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)

        self.telefono_cliente_eliminar_cliente_lineEdit = QLineEdit(self.groupBox_4)
        self.telefono_cliente_eliminar_cliente_lineEdit.setObjectName(u"telefono_cliente_eliminar_cliente_lineEdit")

        self.gridLayout_8.addWidget(self.telefono_cliente_eliminar_cliente_lineEdit, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 2, 0, 1, 1)

        self.descripcion_cliente_eliminar_cliente_plainText = QPlainTextEdit(self.groupBox_4)
        self.descripcion_cliente_eliminar_cliente_plainText.setObjectName(u"descripcion_cliente_eliminar_cliente_plainText")

        self.gridLayout_8.addWidget(self.descripcion_cliente_eliminar_cliente_plainText, 2, 1, 1, 1)

        self.eliminar_eliminar_cliente_button = QPushButton(self.groupBox_4)
        self.eliminar_eliminar_cliente_button.setObjectName(u"eliminar_eliminar_cliente_button")

        self.gridLayout_8.addWidget(self.eliminar_eliminar_cliente_button, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_4, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 11)

        self.gridLayout_6.addWidget(self.frame_c, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_clientes)
        self.page_autos = QWidget()
        self.page_autos.setObjectName(u"page_autos")
        self.gridLayout = QGridLayout(self.page_autos)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_a = QFrame(self.page_autos)
        self.frame_a.setObjectName(u"frame_a")
        self.frame_a.setFrameShape(QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_a)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame_a)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_52 = QLabel(self.frame_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_52)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_a)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_7 = QGroupBox(self.frame_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_11 = QGridLayout(self.groupBox_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_43 = QLabel(self.groupBox_7)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_11.addWidget(self.label_43, 0, 0, 1, 1)

        self.modelo_actualizar_auto_lineEdit = QLineEdit(self.groupBox_7)
        self.modelo_actualizar_auto_lineEdit.setObjectName(u"modelo_actualizar_auto_lineEdit")

        self.gridLayout_11.addWidget(self.modelo_actualizar_auto_lineEdit, 0, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_7)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_11.addWidget(self.label_42, 1, 0, 1, 1)

        self.marca_actualizar_auto_lineEdit = QLineEdit(self.groupBox_7)
        self.marca_actualizar_auto_lineEdit.setObjectName(u"marca_actualizar_auto_lineEdit")

        self.gridLayout_11.addWidget(self.marca_actualizar_auto_lineEdit, 1, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_7)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_11.addWidget(self.label_45, 2, 0, 1, 1)

        self.anio_actualizar_auto_lineEdit = QLineEdit(self.groupBox_7)
        self.anio_actualizar_auto_lineEdit.setObjectName(u"anio_actualizar_auto_lineEdit")

        self.gridLayout_11.addWidget(self.anio_actualizar_auto_lineEdit, 2, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_7)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_11.addWidget(self.label_44, 3, 0, 1, 1)

        self.descripcion_actualizar_auto_plainTextEdit = QPlainTextEdit(self.groupBox_7)
        self.descripcion_actualizar_auto_plainTextEdit.setObjectName(u"descripcion_actualizar_auto_plainTextEdit")

        self.gridLayout_11.addWidget(self.descripcion_actualizar_auto_plainTextEdit, 3, 1, 1, 1)

        self.actualizar_auto_pushButton = QPushButton(self.groupBox_7)
        self.actualizar_auto_pushButton.setObjectName(u"actualizar_auto_pushButton")

        self.gridLayout_11.addWidget(self.actualizar_auto_pushButton, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_46 = QLabel(self.groupBox_6)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_10.addWidget(self.label_46, 0, 0, 1, 1)

        self.modelo_crear_auto_lineEdit = QLineEdit(self.groupBox_6)
        self.modelo_crear_auto_lineEdit.setObjectName(u"modelo_crear_auto_lineEdit")

        self.gridLayout_10.addWidget(self.modelo_crear_auto_lineEdit, 0, 1, 1, 1)

        self.label_47 = QLabel(self.groupBox_6)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_10.addWidget(self.label_47, 1, 0, 1, 1)

        self.marca_crear_auto_lineEdit = QLineEdit(self.groupBox_6)
        self.marca_crear_auto_lineEdit.setObjectName(u"marca_crear_auto_lineEdit")

        self.gridLayout_10.addWidget(self.marca_crear_auto_lineEdit, 1, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_6)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_10.addWidget(self.label_48, 2, 0, 1, 1)

        self.anio_crear_auto_lineEdit = QLineEdit(self.groupBox_6)
        self.anio_crear_auto_lineEdit.setObjectName(u"anio_crear_auto_lineEdit")

        self.gridLayout_10.addWidget(self.anio_crear_auto_lineEdit, 2, 1, 1, 1)

        self.label_49 = QLabel(self.groupBox_6)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_10.addWidget(self.label_49, 3, 0, 1, 1)

        self.descripcion_crear_auto_plainTextEdit = QPlainTextEdit(self.groupBox_6)
        self.descripcion_crear_auto_plainTextEdit.setObjectName(u"descripcion_crear_auto_plainTextEdit")

        self.gridLayout_10.addWidget(self.descripcion_crear_auto_plainTextEdit, 3, 1, 1, 1)

        self.crear_auto_pushButton = QPushButton(self.groupBox_6)
        self.crear_auto_pushButton.setObjectName(u"crear_auto_pushButton")

        self.gridLayout_10.addWidget(self.crear_auto_pushButton, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.frame_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_12 = QGridLayout(self.groupBox_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.mostrar_auto_tableWidget = QTableWidget(self.groupBox_8)
        self.mostrar_auto_tableWidget.setObjectName(u"mostrar_auto_tableWidget")

        self.gridLayout_12.addWidget(self.mostrar_auto_tableWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_8, 1, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.frame_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_13 = QGridLayout(self.groupBox_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_39 = QLabel(self.groupBox_9)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_13.addWidget(self.label_39, 0, 0, 1, 1)

        self.modelo_eliminar_auto_lineEdit = QLineEdit(self.groupBox_9)
        self.modelo_eliminar_auto_lineEdit.setObjectName(u"modelo_eliminar_auto_lineEdit")

        self.gridLayout_13.addWidget(self.modelo_eliminar_auto_lineEdit, 0, 1, 1, 1)

        self.label_38 = QLabel(self.groupBox_9)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_13.addWidget(self.label_38, 1, 0, 1, 1)

        self.marca_eliminar_auto_lineEdit = QLineEdit(self.groupBox_9)
        self.marca_eliminar_auto_lineEdit.setObjectName(u"marca_eliminar_auto_lineEdit")

        self.gridLayout_13.addWidget(self.marca_eliminar_auto_lineEdit, 1, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_9)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_13.addWidget(self.label_41, 2, 0, 1, 1)

        self.anio_eliminar_auto_lineEdit = QLineEdit(self.groupBox_9)
        self.anio_eliminar_auto_lineEdit.setObjectName(u"anio_eliminar_auto_lineEdit")

        self.gridLayout_13.addWidget(self.anio_eliminar_auto_lineEdit, 2, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_9)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_13.addWidget(self.label_40, 3, 0, 1, 1)

        self.descripcion_eliminar_auto_plainTextEdit = QPlainTextEdit(self.groupBox_9)
        self.descripcion_eliminar_auto_plainTextEdit.setObjectName(u"descripcion_eliminar_auto_plainTextEdit")

        self.gridLayout_13.addWidget(self.descripcion_eliminar_auto_plainTextEdit, 3, 1, 1, 1)

        self.eliminar_auto_pushButton = QPushButton(self.groupBox_9)
        self.eliminar_auto_pushButton.setObjectName(u"eliminar_auto_pushButton")

        self.gridLayout_13.addWidget(self.eliminar_auto_pushButton, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_9, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.cliente_autosTab_label = QLabel(self.frame_4)
        self.cliente_autosTab_label.setObjectName(u"cliente_autosTab_label")

        self.gridLayout_3.addWidget(self.cliente_autosTab_label, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 11)

        self.gridLayout.addWidget(self.frame_a, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_autos)
        self.page_servicios = QWidget()
        self.page_servicios.setObjectName(u"page_servicios")
        self.horizontalLayout_2 = QHBoxLayout(self.page_servicios)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_s = QFrame(self.page_servicios)
        self.frame_s.setObjectName(u"frame_s")
        self.frame_s.setFrameShape(QFrame.StyledPanel)
        self.frame_s.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_s)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.frame_s)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_50 = QLabel(self.frame_5)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_50)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_s)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_11 = QGroupBox(self.frame_6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_16 = QGridLayout(self.groupBox_11)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_28 = QLabel(self.groupBox_11)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_16.addWidget(self.label_28, 0, 0, 1, 1)

        self.fecha_actualizar_servicio_dateEdit = QDateEdit(self.groupBox_11)
        self.fecha_actualizar_servicio_dateEdit.setObjectName(u"fecha_actualizar_servicio_dateEdit")
        self.fecha_actualizar_servicio_dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_16.addWidget(self.fecha_actualizar_servicio_dateEdit, 0, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_11)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_16.addWidget(self.label_30, 1, 0, 1, 1)

        self.precio_actualizar_servicio_doubleSpinBox = QDoubleSpinBox(self.groupBox_11)
        self.precio_actualizar_servicio_doubleSpinBox.setObjectName(u"precio_actualizar_servicio_doubleSpinBox")
        self.precio_actualizar_servicio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout_16.addWidget(self.precio_actualizar_servicio_doubleSpinBox, 1, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_11)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_16.addWidget(self.label_27, 2, 0, 1, 1)

        self.inversion_actualizar_servicio_doubleSpinBox = QDoubleSpinBox(self.groupBox_11)
        self.inversion_actualizar_servicio_doubleSpinBox.setObjectName(u"inversion_actualizar_servicio_doubleSpinBox")
        self.inversion_actualizar_servicio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout_16.addWidget(self.inversion_actualizar_servicio_doubleSpinBox, 2, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_11)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_16.addWidget(self.label_29, 3, 0, 1, 1)

        self.kilometraje_actualizar_servicio_lineEdit = QLineEdit(self.groupBox_11)
        self.kilometraje_actualizar_servicio_lineEdit.setObjectName(u"kilometraje_actualizar_servicio_lineEdit")

        self.gridLayout_16.addWidget(self.kilometraje_actualizar_servicio_lineEdit, 3, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_11)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_16.addWidget(self.label_31, 4, 0, 1, 1)

        self.resumen_actualizar_servicio_plainTextEdit = QPlainTextEdit(self.groupBox_11)
        self.resumen_actualizar_servicio_plainTextEdit.setObjectName(u"resumen_actualizar_servicio_plainTextEdit")

        self.gridLayout_16.addWidget(self.resumen_actualizar_servicio_plainTextEdit, 4, 1, 1, 1)

        self.actualizar_servicio_pushButton = QPushButton(self.groupBox_11)
        self.actualizar_servicio_pushButton.setObjectName(u"actualizar_servicio_pushButton")

        self.gridLayout_16.addWidget(self.actualizar_servicio_pushButton, 5, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_11, 2, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.frame_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_15 = QGridLayout(self.groupBox_10)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.mostrar_servicio_tableWidget = QTableWidget(self.groupBox_10)
        self.mostrar_servicio_tableWidget.setObjectName(u"mostrar_servicio_tableWidget")

        self.gridLayout_15.addWidget(self.mostrar_servicio_tableWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_10, 1, 1, 1, 1)

        self.groupBox_12 = QGroupBox(self.frame_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_17 = QGridLayout(self.groupBox_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_33 = QLabel(self.groupBox_12)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_17.addWidget(self.label_33, 0, 0, 1, 1)

        self.fecha_eliminar_servicio_dateEdit = QDateEdit(self.groupBox_12)
        self.fecha_eliminar_servicio_dateEdit.setObjectName(u"fecha_eliminar_servicio_dateEdit")
        self.fecha_eliminar_servicio_dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_17.addWidget(self.fecha_eliminar_servicio_dateEdit, 0, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_12)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_17.addWidget(self.label_35, 1, 0, 1, 1)

        self.precio_eliminar_servicio_doubleSpinBox = QDoubleSpinBox(self.groupBox_12)
        self.precio_eliminar_servicio_doubleSpinBox.setObjectName(u"precio_eliminar_servicio_doubleSpinBox")
        self.precio_eliminar_servicio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout_17.addWidget(self.precio_eliminar_servicio_doubleSpinBox, 1, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_12)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_17.addWidget(self.label_32, 2, 0, 1, 1)

        self.inversion_eliminar_servicio_doubleSpinBox = QDoubleSpinBox(self.groupBox_12)
        self.inversion_eliminar_servicio_doubleSpinBox.setObjectName(u"inversion_eliminar_servicio_doubleSpinBox")
        self.inversion_eliminar_servicio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout_17.addWidget(self.inversion_eliminar_servicio_doubleSpinBox, 2, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_12)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_17.addWidget(self.label_34, 3, 0, 1, 1)

        self.kilometraje_eliminar_servicio_lineEdit = QLineEdit(self.groupBox_12)
        self.kilometraje_eliminar_servicio_lineEdit.setObjectName(u"kilometraje_eliminar_servicio_lineEdit")

        self.gridLayout_17.addWidget(self.kilometraje_eliminar_servicio_lineEdit, 3, 1, 1, 1)

        self.label_36 = QLabel(self.groupBox_12)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_17.addWidget(self.label_36, 4, 0, 1, 1)

        self.resumen_eliminar_servicio_plainTextEdit = QPlainTextEdit(self.groupBox_12)
        self.resumen_eliminar_servicio_plainTextEdit.setObjectName(u"resumen_eliminar_servicio_plainTextEdit")

        self.gridLayout_17.addWidget(self.resumen_eliminar_servicio_plainTextEdit, 4, 1, 1, 1)

        self.eliminar_servicio_pushButton = QPushButton(self.groupBox_12)
        self.eliminar_servicio_pushButton.setObjectName(u"eliminar_servicio_pushButton")

        self.gridLayout_17.addWidget(self.eliminar_servicio_pushButton, 5, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_12, 2, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.frame_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_14 = QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_14.addWidget(self.label_22, 0, 0, 1, 1)

        self.fecha_crear_servicio_dateEdit = QDateEdit(self.groupBox_5)
        self.fecha_crear_servicio_dateEdit.setObjectName(u"fecha_crear_servicio_dateEdit")
        self.fecha_crear_servicio_dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_14.addWidget(self.fecha_crear_servicio_dateEdit, 0, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_14.addWidget(self.label_23, 1, 0, 1, 1)

        self.precio_crear_servicio_doubleSpinBox = QDoubleSpinBox(self.groupBox_5)
        self.precio_crear_servicio_doubleSpinBox.setObjectName(u"precio_crear_servicio_doubleSpinBox")
        self.precio_crear_servicio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout_14.addWidget(self.precio_crear_servicio_doubleSpinBox, 1, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_14.addWidget(self.label_24, 2, 0, 1, 1)

        self.inversion_crear_servicio_doubleSpinBox = QDoubleSpinBox(self.groupBox_5)
        self.inversion_crear_servicio_doubleSpinBox.setObjectName(u"inversion_crear_servicio_doubleSpinBox")
        self.inversion_crear_servicio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout_14.addWidget(self.inversion_crear_servicio_doubleSpinBox, 2, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_14.addWidget(self.label_25, 3, 0, 1, 1)

        self.kilometraje_crear_servicio_lineEdit = QLineEdit(self.groupBox_5)
        self.kilometraje_crear_servicio_lineEdit.setObjectName(u"kilometraje_crear_servicio_lineEdit")

        self.gridLayout_14.addWidget(self.kilometraje_crear_servicio_lineEdit, 3, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_14.addWidget(self.label_26, 4, 0, 1, 1)

        self.resumen_crear_servicio_plainTextEdit = QPlainTextEdit(self.groupBox_5)
        self.resumen_crear_servicio_plainTextEdit.setObjectName(u"resumen_crear_servicio_plainTextEdit")

        self.gridLayout_14.addWidget(self.resumen_crear_servicio_plainTextEdit, 4, 1, 1, 1)

        self.crear_servicio_pushButton = QPushButton(self.groupBox_5)
        self.crear_servicio_pushButton.setObjectName(u"crear_servicio_pushButton")

        self.gridLayout_14.addWidget(self.crear_servicio_pushButton, 5, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)

        self.automovil_serviciosTab_label = QLabel(self.frame_6)
        self.automovil_serviciosTab_label.setObjectName(u"automovil_serviciosTab_label")

        self.gridLayout_4.addWidget(self.automovil_serviciosTab_label, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 11)

        self.horizontalLayout_2.addWidget(self.frame_s)

        self.stackedWidget.addWidget(self.page_servicios)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_paginas)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.verticalLayout.addWidget(self.frame_inferior)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 11)

        self.verticalLayout_2.addWidget(self.frame_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Servicio Canela", None))
        self.pushButton_inicio.setText("")
        self.pushButton_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.pushButton_autos.setText(QCoreApplication.translate("MainWindow", u"Autos", None))
        self.pushButton_servicios.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Bienvenido !", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.guardar_crear_cliente_button.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.mostrar_mostrar_clientes_button.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.actualizar_actualizar_cliente_button.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.eliminar_eliminar_cliente_button.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Autos", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.actualizar_auto_pushButton.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.crear_auto_pushButton.setText(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None))
        self.eliminar_auto_pushButton.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.cliente_autosTab_label.setText(QCoreApplication.translate("MainWindow", u"(Nombre del cliente)", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Inversi\u00f3n", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Kilometraje", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Resumen", None))
        self.actualizar_servicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Inversi\u00f3n", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Kilometraje", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Resumen", None))
        self.eliminar_servicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Inversi\u00f3n", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Kilometraje", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Resumen", None))
        self.crear_servicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Automovil:", None))
        self.automovil_serviciosTab_label.setText(QCoreApplication.translate("MainWindow", u"(Nombre del automovil)", None))
    # retranslateUi

