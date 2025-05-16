# PYSIDE2
from PySide2.QtWidgets import QMainWindow, QMessageBox, QStackedWidget, QSizePolicy

# PROYECT FILES

# UI
from ui_mainwindow import Ui_MainWindow

# tab files
from clientes_tab import ClientesTab
from autos_tab import AutosTab
from servicios_tab import ServiciosTab
# aux files
from cliente import Cliente
from auto import Auto
from servicio import Servicio


class MainWindow(QMainWindow):
    """
    This class contains the mainwindow used to receive accounts data
    """

    def __init__(self):
        """
        the __init__ method initialize the window and use the interface
        """
        # --- UI ---
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.stackedWidget = QStackedWidget(self.ui.centralwidget)

        # Añadir el QStackedWidget al diseño central
        self.ui.stackedWidget.addWidget(self.stackedWidget)

        # Conectar los botones a las páginas correspondientes
        self.ui.pushButton_inicio.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.pushButton_autos.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_autos))
        self.ui.pushButton_clientes.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_clientes))
        self.ui.pushButton_servicios.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_servicios))

        # Añadir las páginas al QStackedWidget
        self.stackedWidget.addWidget(self.ui.page_inicio)
        self.stackedWidget.addWidget(self.ui.page_autos)
        self.stackedWidget.addWidget(self.ui.page_clientes)
        self.stackedWidget.addWidget(self.ui.page_servicios)

        # Pestañas
        self.cliente = Cliente()
        self.clientes_tab = ClientesTab(self.ui, self.cliente)
        self.automovil = Auto()
        self.autos_tab = AutosTab(self.ui, self.cliente, self.automovil)
        self.servicio = Servicio()
        self.servicio_tab = ServiciosTab(
        self.ui, self.automovil, self.servicio)
