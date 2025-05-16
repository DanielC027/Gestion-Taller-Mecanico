from PySide2.QtCore import QObject, Signal


class Auto(QObject):
    __id = ""
    __id_cliente = ""
    __modelo = ""
    __marca = ""
    __anio = ""
    __descripcion = ""
    valor_changed = Signal(str)

    def __init__(self, id="", id_cliente="", modelo="", marca="", anio="", descripcion="") -> None:
        super().__init__()
        self.__id = id
        self.__id_cliente = id_cliente
        self.__modelo = modelo
        self.__marca = marca
        self.__anio = anio
        self.__descripcion = descripcion
    # -------------------------------------

    def ponerId(self, id):
        self.__id = id
        self.valor_changed.emit(self.__id)

    def ponerIdCliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def ponerModelo(self, modelo):
        self.__modelo = modelo

    def ponerMarca(self, marca):
        self.__marca = marca

    def ponerAnio(self, anio):
        self.__anio = anio

    def ponerDescripcion(self, desc):
        self.__descripcion = desc
    # -------------------------------------

    @property
    def obtenerId(self):
        return self.__id

    @property
    def obtenerIdCliente(self):
        return self.__id_cliente

    @property
    def obtenerModelo(self):
        return self.__modelo

    @property
    def obtenerMarca(self):
        return self.__marca

    @property
    def obtenerAnio(self):
        return self.__anio

    @property
    def obtenerDescripcion(self):
        return self.__descripcion


"""
auto = Auto("1", "2", "sierra", "gmc", "2023", "el compa")

print(auto.obtenerId(), auto.obtenerDescripcion())
"""
