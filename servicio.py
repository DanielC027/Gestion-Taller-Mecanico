from PySide2.QtCore import QObject, Signal


class Servicio(QObject):
    __id = ""
    __id_automovil = ""
    __fecha = ""
    __resumen = ""
    __precio = ""
    __inversion = ""
    __kilometraje = ""
    valor_changed = Signal(str)

    def __init__(self, id="", id_automovil="", fecha="", resumen="", precio="", inversion="", kilometraje="") -> None:
        super().__init__()
        self.__id = id
        self.__id_automovil = id_automovil
        self.__fecha = fecha
        self.__resumen = resumen
        self.__precio = precio
        self.__inversion = inversion
        self.__kilometraje = kilometraje
    # -------------------------------------

    def ponerId(self, id):
        self.__id = id
        self.valor_changed.emit(self.__id)

    def ponerIdAutomovil(self, id_automovil):
        self.__id_automovil = id_automovil

    def ponerFecha(self, fecha):
        self.__fecha = fecha

    def ponerResumen(self, resumen):
        self.__resumen = resumen

    def ponerPrecio(self, precio):
        self.__precio = precio

    def ponerInversion(self, inversion):
        self.__inversion = inversion

    def ponerKilometraje(self, kilometraje):
        self.__kilometraje = kilometraje

    # -------------------------------------
    @property
    def obtenerId(self):
        return self.__id

    @property
    def obtenerIdAuto(self):
        return self.__id_automovil

    @property
    def obtenerFecha(self):
        return self.__fecha

    @property
    def obtenerResumen(self):
        return self.__resumen

    @property
    def obtenerPrecio(self):
        return self.__precio

    @property
    def obtenerInversion(self):
        return self.__inversion

    @property
    def obtenerKilometraje(self):
        return self.__kilometraje


"""

serv = Servicio("1", "3", "12/12/2232", "afinacion", "23323", "1212", "55000")

print(serv.obtenerId())
print(serv.obtenerIdAuto())
serv.ponerFecha("12/05/2023")
print(serv.obtenerFecha())
"""
