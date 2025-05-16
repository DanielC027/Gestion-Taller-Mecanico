"""
    This libraries are used to show and manipulate the main window
"""
# --- PROYECT FILES ---
# Objects
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow

from lista_clientes import ListaClientes
from PySide2.QtCore import Slot
# --- PYSIDE2 LIBRARIES ---

# Interface

# System
from cliente import Cliente


class ClientesTab(object):
    """
    manipula la lista de clientes
    """

    def __init__(self, ui: Ui_MainWindow, cliente: Cliente):
        self.ui = ui
        self.__cliente = cliente
        self.__listaClientes = ListaClientes()
        """______________________________INTERACTIONS______________________________"""
        self.ui.mostrar_mostrar_clientes_button.clicked.connect(
            self.click_mostrar_clientes)
        self.ui.guardar_crear_cliente_button.clicked.connect(
            self.click_crear_cliente)
        self.ui.eliminar_eliminar_cliente_button.clicked.connect(
            self.click_eliminar_cliente)
        self.ui.actualizar_actualizar_cliente_button.clicked.connect(
            self.click_actualizar_cliente)

        # ____________________________________________
    # ---> MOSTRAR CLIENTES
    @Slot()
    def click_mostrar_clientes(self):
        print("funciona\n\n")
        self.__listaClientes.mostrarClientes()

        # se pone la informacion en el table widget
        self.ui.mostrar_clientes_clientes_tableWidget.setColumnCount(3)
        headers = ["Nombre", "Telefono", "Descripcion"]
        self.ui.mostrar_clientes_clientes_tableWidget.setHorizontalHeaderLabels(
            headers)

        self.ui.mostrar_clientes_clientes_tableWidget.setRowCount(
            len(self.__listaClientes))

        row = 0
        for cliente in self.__listaClientes:
            nombre_w = QTableWidgetItem(cliente.obtenerNombre)
            telefono_w = QTableWidgetItem(cliente.obtenerTelefono)
            descripcion_w = QTableWidgetItem(
                cliente.obtenerDescripcion)

            self.ui.mostrar_clientes_clientes_tableWidget.setItem(
                row, 0, nombre_w)
            self.ui.mostrar_clientes_clientes_tableWidget.setItem(
                row, 1, telefono_w)
            self.ui.mostrar_clientes_clientes_tableWidget.setItem(
                row, 2, descripcion_w)
            row += 1

        self.ui.mostrar_clientes_clientes_tableWidget.cellClicked.connect(
            self.on_cell_clicked)

    def on_cell_clicked(self, row):
        print(f"rrow: {row}")
        client = self.__listaClientes.seleccionarCliente(row)
        self.__cliente.ponerId(client.obtenerId)
        self.__cliente.ponerNombre(client.obtenerNombre)
        self.__cliente.ponerTelefono(client.obtenerTelefono)
        self.__cliente.ponerDescripcion(client.obtenerDescripcion)

        self.ponerInfoActualizarCliente()
        self.ponerInfoEliminarCliente()
        self.ponerInfoListaAutos()

    def ponerInfoActualizarCliente(self):
        try:
            self.ui.nombre_cliente_actualizar_cliente_lineEdit.setText(
                self.__cliente.obtenerNombre)
            self.ui.telefono_cliente_actualizar_cliente_lineEdit.setText(
                self.__cliente.obtenerTelefono)
            self.ui.descripcion_cliente_actualizar_cliente_plainText.setPlainText(
                self.__cliente.obtenerDescripcion)
        except Exception as ex:
            print(f"excepcion: {ex}")

    def ponerInfoEliminarCliente(self):
        try:
            self.ui.nombre_cliente_eliminar_cliente_lineEdit.setText(
                self.__cliente.obtenerNombre)
            self.ui.nombre_cliente_eliminar_cliente_lineEdit.setDisabled(True)
            self.ui.telefono_cliente_eliminar_cliente_lineEdit.setText(
                self.__cliente.obtenerTelefono)
            self.ui.telefono_cliente_eliminar_cliente_lineEdit.setDisabled(
                True)
            self.ui.descripcion_cliente_eliminar_cliente_plainText.setPlainText(
                self.__cliente.obtenerDescripcion)
            self.ui.descripcion_cliente_eliminar_cliente_plainText.setDisabled(
                True)
        except Exception as ex:
            print(f"excepcion: {ex}")

    def ponerInfoListaAutos(self):
        pass
    # ---> <---
    # ---> CREAR CLIENTES

    @Slot()
    def click_crear_cliente(self):
        nombre = self.ui.nombre_cliente_crear_cliente_lineEdit.text()
        telefono = self.ui.telefono_cliente_crear_cliente_lineEdit.text()
        descrip = self.ui.descripcion_cliente_crear_cliente_plainText.toPlainText()
        if nombre == "" or telefono == "" or descrip == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Datos no validos"
            )
            return

        cliente = Cliente("", nombre, telefono, descrip)

        if self.__listaClientes.crearCliente(cliente):
            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se creo correctamente"
            )
            self.click_mostrar_clientes()
            self.ui.nombre_cliente_crear_cliente_lineEdit.setText("")
            self.ui.telefono_cliente_crear_cliente_lineEdit.setText("")
            self.ui.descripcion_cliente_crear_cliente_plainText.setPlainText(
                "")
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible crear el usuario"
            )

    # ---> <---

    # ---> ELIMINAR CLIENTES

    @Slot()
    def click_eliminar_cliente(self):
        # create an instance
        message_box = QMessageBox()
        # put the type of message and bottons
        message_box.setIcon(QMessageBox.Question)
        message_box.setText("¿Esta segur@ de eliminar el usuario?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)

        # show dialog
        result = message_box.exec_()

        # see result
        if result == QMessageBox.No:
            return

        id = self.__cliente.obtenerId
        resultado = self.__listaClientes.eliminarCliente(id)
        if resultado[0] == '1':
            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se elimino correctamente"
            )
            self.click_mostrar_clientes()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible eliminar el usuario"
            )

    # ---> <---

    # ---> ACTUALIZAR CLIENTES

    @Slot()
    def click_actualizar_cliente(self):
        # create an instance
        message_box = QMessageBox()
        # put the type of message and bottons
        message_box.setIcon(QMessageBox.Question)
        message_box.setText("¿Esta segur@ de modificar el usuario?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.No)

        # show dialog
        result = message_box.exec_()

        # see result
        if result == QMessageBox.No:
            return

        id = self.__cliente.obtenerId
        nombre = self.ui.nombre_cliente_actualizar_cliente_lineEdit.text()
        telefono = self.ui.telefono_cliente_actualizar_cliente_lineEdit.text()
        descrip = self.ui.descripcion_cliente_actualizar_cliente_plainText.toPlainText()

        if id == "" or nombre == "" or telefono == "" or descrip == "":
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "Datos no validos"
            )
            return

        cliente = Cliente(id, nombre, telefono, descrip)
        resultado = self.__listaClientes.actualizarCliente(cliente)
        if resultado[0] == "1":
            QMessageBox.information(
                self.ui.centralwidget,
                "Exito",
                "Se modifico correctamente"
            )
            self.click_mostrar_clientes()
        else:
            QMessageBox.information(
                self.ui.centralwidget,
                "Error",
                "No fue posible modificar el usuario"
            )

    # ---> <---
