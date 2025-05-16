"""
    This libraries are used to show and manipulate the main window
"""
# --- PROYECT FILES ---
# Objects
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow

from lista_autos import ListaAutos
from PySide2.QtCore import Slot
# --- PYSIDE2 LIBRARIES ---

# Interface

# System
from auto import Auto
from cliente import Cliente


class AutosTab(object):
    """
    manipula la lista de autos
    """

    def __init__(self, ui: Ui_MainWindow, cliente: Cliente, automovil: Auto):
        self.ui = ui
        self.__cliente = cliente
        self.__automovil = automovil
        self.__listaAutos = ListaAutos()
        """______________________________INTERACTIONS______________________________"""
        self.__cliente.valor_changed.connect(self.click_mostrar_automoviles)
        self.ui.crear_auto_pushButton.clicked.connect(
            self.click_crear_auto)
        self.ui.eliminar_auto_pushButton.clicked.connect(
            self.click_eliminar_auto)
        self.ui.actualizar_auto_pushButton.clicked.connect(
            self.click_actualizar_auto)
        # ____________________________________________
    # ---> MOSTRAR automoviles
    @Slot()
    def click_mostrar_automoviles(self):
        print("click_mostrar_automoviles")
        self.limpearInfo()
        print("funciona\n\n")
        self.__listaAutos.mostrarAutos(self.__cliente.obtenerId)
        self.ui.cliente_autosTab_label.setText(self.__cliente.obtenerNombre)
        # se pone la informacion en el table widget
        self.ui.mostrar_auto_tableWidget.setColumnCount(4)
        headers = ["Modelo", "Marca", "Año", "Descripción"]
        self.ui.mostrar_auto_tableWidget.setHorizontalHeaderLabels(
            headers)

        self.ui.mostrar_auto_tableWidget.setRowCount(
            len(self.__listaAutos))

        row = 0
        for auto in self.__listaAutos:
            modelo_w = QTableWidgetItem(auto.obtenerModelo)
            marca_w = QTableWidgetItem(auto.obtenerMarca)
            anio_w = QTableWidgetItem(auto.obtenerAnio)
            descripcion_w = QTableWidgetItem(
                auto.obtenerDescripcion)

            self.ui.mostrar_auto_tableWidget.setItem(
                row, 0, modelo_w)
            self.ui.mostrar_auto_tableWidget.setItem(
                row, 1, marca_w)
            self.ui.mostrar_auto_tableWidget.setItem(
                row, 2, anio_w)
            self.ui.mostrar_auto_tableWidget.setItem(
                row, 3, descripcion_w)
            row += 1

        self.ui.mostrar_auto_tableWidget.cellClicked.connect(
            self.on_cell_clicked)

    def on_cell_clicked(self, row):
        print(f"row: {row}")
        autom = self.__listaAutos.seleccionarAuto(row)

        self.__automovil.ponerId(autom.obtenerId)
        self.__automovil.ponerIdCliente(autom.obtenerIdCliente)
        self.__automovil.ponerModelo(autom.obtenerModelo)
        self.__automovil.ponerMarca(autom.obtenerMarca)
        self.__automovil.ponerAnio(autom.obtenerAnio)
        self.__automovil.ponerDescripcion(autom.obtenerDescripcion)

        self.ponerInfoActualizarAuto()
        self.ponerInfoEliminarAuto()
        self.ponerInfoListaServicios()
    
    def ponerInfoListaServicios(self):
        pass


    def ponerInfoActualizarAuto(self):
        try:
            self.ui.modelo_actualizar_auto_lineEdit.setText(
                self.__automovil.obtenerModelo)

            self.ui.marca_actualizar_auto_lineEdit.setText(
                self.__automovil.obtenerMarca)

            self.ui.anio_actualizar_auto_lineEdit.setText(
                self.__automovil.obtenerAnio)

            self.ui.descripcion_actualizar_auto_plainTextEdit.setPlainText(
                self.__automovil.obtenerDescripcion)

        except Exception as ex:
            print(f"excepcion: {ex}")

    def ponerInfoEliminarAuto(self):
        try:
            self.ui.modelo_eliminar_auto_lineEdit.setText(
                self.__automovil.obtenerModelo)
            self.ui.modelo_eliminar_auto_lineEdit.setDisabled(True)

            self.ui.marca_eliminar_auto_lineEdit.setText(
                self.__automovil.obtenerMarca)
            self.ui.marca_eliminar_auto_lineEdit.setDisabled(True)

            self.ui.anio_eliminar_auto_lineEdit.setText(
                self.__automovil.obtenerAnio)
            self.ui.anio_eliminar_auto_lineEdit.setDisabled(True)

            self.ui.descripcion_eliminar_auto_plainTextEdit.setPlainText(
                self.__automovil.obtenerDescripcion)
            self.ui.descripcion_eliminar_auto_plainTextEdit.setDisabled(True)
        except Exception as ex:
            print(f"excepcion: {ex}")

    def limpearInfo(self):
        self.ui.modelo_actualizar_auto_lineEdit.setText("")
        self.ui.marca_actualizar_auto_lineEdit.setText("")
        self.ui.anio_actualizar_auto_lineEdit.setText("")
        self.ui.descripcion_actualizar_auto_plainTextEdit.setPlainText("")

        self.ui.modelo_eliminar_auto_lineEdit.setText("")
        self.ui.marca_eliminar_auto_lineEdit.setText("")
        self.ui.anio_eliminar_auto_lineEdit.setText("")
        self.ui.descripcion_eliminar_auto_plainTextEdit.setPlainText("")
    # ---> <---
    # ---> CREAR AUTOS

    @Slot()
    def click_crear_auto(self):
        id_cliente = self.__cliente.obtenerId
        modelo = self.ui.modelo_crear_auto_lineEdit.text()
        marca = self.ui.marca_crear_auto_lineEdit.text()
        anio = self.ui.anio_crear_auto_lineEdit.text()
        descrip = self.ui.descripcion_crear_auto_plainTextEdit.toPlainText()
        if modelo == "" or marca == "" or anio == "" or descrip == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Datos no validos"
            )
            return

        auto = Auto("", id_cliente, modelo, marca, anio, descrip)

        if self.__listaAutos.crearAuto(auto):
            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se creo correctamente"
            )
            modelo = self.ui.modelo_crear_auto_lineEdit.setText("")
            marca = self.ui.marca_crear_auto_lineEdit.setText("")
            anio = self.ui.anio_crear_auto_lineEdit.setText("")
            descrip = self.ui.descripcion_crear_auto_plainTextEdit.setPlainText(
                "")
            self.click_mostrar_automoviles()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible crear el auto"
            )

    # ---> <---

    # ---> ELIMINAR AUTOS

    @Slot()
    def click_eliminar_auto(self):
        # create an instance
        message_box = QMessageBox()
        # put the type of message and bottons
        message_box.setIcon(QMessageBox.Question)
        message_box.setText("¿Esta segur@ de eliminar el automovil?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)

        # show dialog
        result = message_box.exec_()

        # see result
        if result == QMessageBox.No:
            return

        id = self.__automovil.obtenerId
        resultado = self.__listaAutos.eliminarAuto(id)
        if resultado[0] == '1':
            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se elimino correctamente"
            )
            self.click_mostrar_automoviles()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible eliminar el automovil"
            )

    # ---> <---

    # ---> ACTUALIZAR AUTOS

    @Slot()
    def click_actualizar_auto(self):
        # create an instance
        message_box = QMessageBox()
        # put the type of message and bottons
        message_box.setIcon(QMessageBox.Question)
        message_box.setText("¿Esta segur@ de modificar el automovil?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)

        # show dialog
        result = message_box.exec_()

        # see result
        if result == QMessageBox.No:
            return

        id = self.__automovil.obtenerId
        id_cliente = self.__automovil.obtenerIdCliente
        modelo = self.ui.modelo_actualizar_auto_lineEdit.text()
        marca = self.ui.marca_actualizar_auto_lineEdit.text()
        anio = self.ui.anio_actualizar_auto_lineEdit.text()
        descrip = self.ui.descripcion_actualizar_auto_plainTextEdit.toPlainText()

        # pedir datos

        if id == "" or id_cliente == "" or modelo == "" or marca == "" or anio == "" or descrip == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Datos no validos"
            )
            return

        aut = Auto(id, id_cliente, modelo, marca, anio, descrip)
        resultado = self.__listaAutos.actualizarAuto(aut)
        if resultado[0] == "1":
            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se modifico correctamente"
            )
            self.click_mostrar_automoviles()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible modificar el auto"
            )

    # ---> <---
