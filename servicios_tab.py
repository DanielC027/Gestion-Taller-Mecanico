"""
    This libraries are used to show and manipulate the main window
"""
# --- PROYECT FILES ---
# Objects
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow

from lista_servicios import ListaServicios
from PySide2.QtCore import Slot, QDate
# --- PYSIDE2 LIBRARIES ---

# Interface

# System
from servicio import Servicio
from auto import Auto


class ServiciosTab(object):
    """
    manipula la lista de servicios
    """

    def __init__(self, ui: Ui_MainWindow, automovil: Auto, servicio: Servicio):
        self.ui = ui
        self.__automovil = automovil
        self.__servicio = servicio
        self.__listaServicios = ListaServicios()
        """______________________________INTERACTIONS______________________________"""
        self.__automovil.valor_changed.connect(self.click_mostrar_servicios)
        self.ui.crear_servicio_pushButton.clicked.connect(
            self.click_crear_servicio)
        self.ui.eliminar_servicio_pushButton.clicked.connect(
            self.click_eliminar_servicio)
        self.ui.actualizar_servicio_pushButton.clicked.connect(
            self.click_actualizar_servicio)

        # ____________________________________________
    # ---> MOSTRAR servicios
    @Slot()
    def click_mostrar_servicios(self):
        print("click_mostrar_servicios")
        self.limpearInfo()
        print("funciona\n\n")
        self.__listaServicios.mostrarServicios(self.__automovil.obtenerId)
        self.ui.automovil_serviciosTab_label.setText(self.__automovil.obtenerModelo + " " + self.__automovil.obtenerAnio)
        # se pone la informacion en el table widget
        self.ui.mostrar_servicio_tableWidget.setColumnCount(5)
        headers = ["Fecha"," Resumen", "Precio", "Inversion", "Kilometraje"]
        self.ui.mostrar_servicio_tableWidget.setHorizontalHeaderLabels(
            headers)

        self.ui.mostrar_servicio_tableWidget.setRowCount(
            len(self.__listaServicios))

        row = 0
        for servicio in self.__listaServicios:
            fecha_w = QTableWidgetItem(servicio.obtenerFecha)
            resumen_w = QTableWidgetItem(servicio.obtenerResumen)
            precio_w = QTableWidgetItem(str(servicio.obtenerPrecio))
            inversion_w = QTableWidgetItem(str(servicio.obtenerInversion))
            kilometraje_w = QTableWidgetItem(str(servicio.obtenerKilometraje))

            self.ui.mostrar_servicio_tableWidget.setItem(
                row, 0, fecha_w)
            self.ui.mostrar_servicio_tableWidget.setItem(
                row, 1, resumen_w)
            self.ui.mostrar_servicio_tableWidget.setItem(
                row, 2, precio_w)
            self.ui.mostrar_servicio_tableWidget.setItem(
                row, 3, inversion_w)
            self.ui.mostrar_servicio_tableWidget.setItem(
                row, 4, kilometraje_w)
            row += 1

        self.ui.mostrar_servicio_tableWidget.cellClicked.connect(
            self.on_cell_clicked)


    def on_cell_clicked(self, row):
        print("on cell")
        print(f"row: {row}")
        autom = self.__listaServicios.seleccionarServicio(row)

        self.__servicio.ponerId(autom.obtenerId)
        self.__servicio.ponerIdAutomovil(autom.obtenerIdAuto)
        self.__servicio.ponerFecha(autom.obtenerFecha)
        self.__servicio.ponerResumen(autom.obtenerResumen)
        self.__servicio.ponerPrecio(autom.obtenerPrecio)
        self.__servicio.ponerInversion(autom.obtenerInversion)
        self.__servicio.ponerKilometraje(autom.obtenerKilometraje)

        self.ponerInfoActualizarServicio()
        self.ponerInfoEliminarServicio()

    def ponerInfoActualizarServicio(self):
        try:
            fecha = QDate.fromString(self.__servicio.obtenerFecha, "yyyy-MM-dd")
            self.ui.fecha_actualizar_servicio_dateEdit.setDate(fecha)
            self.ui.precio_actualizar_servicio_doubleSpinBox.setValue(float(self.__servicio.obtenerPrecio))
            self.ui.inversion_actualizar_servicio_doubleSpinBox.setValue(float(self.__servicio.obtenerInversion))
            self.ui.kilometraje_actualizar_servicio_lineEdit.setText(str(self.__servicio.obtenerKilometraje))
            self.ui.resumen_actualizar_servicio_plainTextEdit.setPlainText(self.__servicio.obtenerResumen)

        except Exception as ex:
            print(f"excepcion: {ex}")

    def ponerInfoEliminarServicio(self):
        try:
            fecha = QDate.fromString(self.__servicio.obtenerFecha, "yyyy-MM-dd")
            self.ui.fecha_eliminar_servicio_dateEdit.setDate(fecha)
            self.ui.fecha_eliminar_servicio_dateEdit.setDisabled(True)

            self.ui.precio_eliminar_servicio_doubleSpinBox.setValue(float(self.__servicio.obtenerPrecio))
            self.ui.precio_eliminar_servicio_doubleSpinBox.setDisabled(True)

            self.ui.inversion_eliminar_servicio_doubleSpinBox.setValue(float(self.__servicio.obtenerInversion))
            self.ui.inversion_eliminar_servicio_doubleSpinBox.setDisabled(True)

            self.ui.kilometraje_eliminar_servicio_lineEdit.setText(str(self.__servicio.obtenerKilometraje))
            self.ui.kilometraje_eliminar_servicio_lineEdit.setDisabled(True)

            self.ui.resumen_eliminar_servicio_plainTextEdit.setPlainText(self.__servicio.obtenerResumen)
            self.ui.resumen_eliminar_servicio_plainTextEdit.setDisabled(True)
        except Exception as ex:
            print(f"excepcion: {ex}")




    def limpearInfo(self):
        self.ui.fecha_actualizar_servicio_dateEdit.clear()
        self.ui.precio_actualizar_servicio_doubleSpinBox.clear()
        self.ui.inversion_actualizar_servicio_doubleSpinBox.clear()
        self.ui.kilometraje_actualizar_servicio_lineEdit.setText("")
        self.ui.resumen_actualizar_servicio_plainTextEdit.setPlainText("")

        self.ui.fecha_eliminar_servicio_dateEdit.clear()
        self.ui.precio_eliminar_servicio_doubleSpinBox.clear()
        self.ui.inversion_eliminar_servicio_doubleSpinBox.clear()
        self.ui.kilometraje_eliminar_servicio_lineEdit.clear()
        self.ui.resumen_eliminar_servicio_plainTextEdit.clear()
    # ---> <---
    # ---> CREAR SERVICIO

    @Slot()
    def click_crear_servicio(self):
        id_automovil = self.__automovil.obtenerId
        fecha = self.ui.fecha_crear_servicio_dateEdit.date().toString("yyyy-MM-dd")
        precio = self.ui.precio_crear_servicio_doubleSpinBox.value()
        inversion = self.ui.inversion_crear_servicio_doubleSpinBox.value()
        kilometraje = self.ui.kilometraje_crear_servicio_lineEdit.text()
        resumen = self.ui.resumen_crear_servicio_plainTextEdit.toPlainText()

        if fecha == "" or precio == 0 or inversion == 0 or kilometraje == "" or resumen == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Datos no válidos"
            )
            return

        servicio = Servicio("", id_automovil, fecha, resumen, precio, inversion, kilometraje)

        if self.__listaServicios.crearServicio(servicio):
            QMessageBox.information(
                self.ui.centralwidget,
                "Éxito",
                "Se creó correctamente el servicio"
            )
            self.ui.fecha_crear_servicio_dateEdit.setDate(QDate.currentDate())
            self.ui.precio_crear_servicio_doubleSpinBox.setValue(0.0)
            self.ui.inversion_crear_servicio_doubleSpinBox.setValue(0.0)
            self.ui.kilometraje_crear_servicio_lineEdit.clear()
            self.ui.resumen_crear_servicio_plainTextEdit.clear()
            self.click_mostrar_servicios()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible crear el servicio"
            )

    # ---> <---

    # ---> ELIMINAR SERVICIO

    @Slot()
    def click_eliminar_servicio(self):
        # Crear una instancia del cuadro de mensaje
        message_box = QMessageBox()
        # Establecer el tipo de mensaje y los botones
        message_box.setIcon(QMessageBox.Question)
        message_box.setText("¿Está seguro de eliminar el servicio?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)

        # Mostrar el diálogo
        result = message_box.exec_()

        # Verificar el resultado
        if result == QMessageBox.No:
            return

        id = self.__servicio.obtenerId
        resultado = self.__listaServicios.eliminarServicio(id)
        if resultado[0] == '1':
            QMessageBox.information(
                self.ui.centralwidget,
                "Éxito",
                "Se eliminó correctamente el servicio"
            )
            self.click_mostrar_servicios()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible eliminar el servicio"
            )


    # ---> <---

    # ---> ACTUALIZAR SERVICIO

    @Slot()
    def click_actualizar_servicio(self):
        # Crear una instancia del cuadro de mensaje
        message_box = QMessageBox()
        # Establecer el tipo de mensaje y los botones
        message_box.setIcon(QMessageBox.Question)
        message_box.setText("¿Está seguro de modificar el servicio?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)

        # Mostrar el diálogo
        result = message_box.exec_()

        # Verificar el resultado
        if result == QMessageBox.No:
            return

        id_servicio = self.__servicio.obtenerId
        id_automovil = self.__servicio.obtenerIdAuto
        fecha = self.ui.fecha_actualizar_servicio_dateEdit.date().toString("yyyy-MM-dd")
        precio = self.ui.precio_actualizar_servicio_doubleSpinBox.value()
        inversion = self.ui.inversion_actualizar_servicio_doubleSpinBox.value()
        kilometraje = self.ui.kilometraje_actualizar_servicio_lineEdit.text()
        resumen = self.ui.resumen_actualizar_servicio_plainTextEdit.toPlainText()

        if id_servicio == "" or id_automovil == "" or fecha == "" or precio == 0 or inversion == 0 or kilometraje == "" or resumen == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Datos no válidos"
            )
            return

        servicio = Servicio(id_servicio, id_automovil, fecha, resumen, precio, inversion, kilometraje)
        resultado = self.__listaServicios.actualizarServicio(servicio)

        if resultado[0] == "1":
            QMessageBox.information(
                self.ui.centralwidget,
                "Éxito",
                "Se modificó correctamente el servicio"
            )
            self.click_mostrar_servicios()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible modificar el servicio"
            )


    # ---> <---
