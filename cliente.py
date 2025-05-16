from PySide2.QtCore import QObject, Signal


class Cliente(QObject):
    __id = ""
    __nombre = ""
    __telefono = ""
    __descripcion = ""
    valor_changed = Signal(str)

    def __init__(self, id="", nombre="", telefono="", descripcion="") -> None:
        super().__init__()
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__descripcion = descripcion
    # -------------------------------------

    def ponerId(self, id):
        self.__id = id

        self.valor_changed.emit(self.__id)

    def ponerNombre(self, nombre):
        self.__nombre = nombre

    def ponerTelefono(self, tel):
        self.__telefono = tel

    def ponerDescripcion(self, desc):
        self.__descripcion = desc
    # -------------------------------------

    @property
    def obtenerId(self):
        return self.__id

    @property
    def obtenerNombre(self):
        return self.__nombre

    @property
    def obtenerTelefono(self):
        return self.__telefono

    @property
    def obtenerDescripcion(self):
        return self.__descripcion


"""cliente = Cliente()

cli = Cliente("2", "Daniel", "3323128767", "Esta es la")

cliente = cli

print(cliente.obtenerNombre, cliente.obtenerTelefono, cliente.obtenerDescripcion)"""
