
import json
import requests
from servicio import Servicio


class ListaServicios():
    __lista_servicios = []

    def crearServicio(self, serv: Servicio):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/serv/agregarServicio.php'

            datos = {'id_automovil': serv.obtenerIdAuto, 'fecha': serv.obtenerFecha,
                     'resumen': serv.obtenerResumen, 'precio': serv.obtenerPrecio,
                     'inversion': serv.obtenerInversion, 'kilometraje': serv.obtenerKilometraje}

            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                return respuesta.text
            else:
                print("Error: ", respuesta.status_code)
                return 0
            # return 1
        except Exception as ex:
            print(f"Error {ex}")
            return 0

    def mostrarServicios(self, id_automovil):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/serv/mostrarServicio.php'
            datos = {'id_automovil': id_automovil}
            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                print(respuesta.text)
                lista = json.loads(respuesta.text)
                print("Lista:::", lista)

                if 'error' in lista:
                    self.__lista_servicios.clear()
                    return

                self.__lista_servicios = [
                    Servicio(**serv) for serv in lista]
            else:
                print("Error: ", respuesta.status_code)
            # return 1
        except Exception as ex:
            print(f"Error {ex}")

    def actualizarServicio(self, serv: Servicio):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/serv/actualizarServicio.php'
            datos = {'id': serv.obtenerId, 'id_automovil': serv.obtenerIdAuto, 'fecha': serv.obtenerFecha,
                     'resumen': serv.obtenerResumen, 'precio': serv.obtenerPrecio,
                     'inversion': serv.obtenerInversion, 'kilometraje': serv.obtenerKilometraje}

            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                return respuesta.text
            else:
                print("Error: ", respuesta.status_code)
                return 0
            # return 1
        except Exception as ex:
            print(f"Error {ex}")
            return 0

    def eliminarServicio(self, id):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/serv/eliminarServicio.php'
            datos = {'id': id}

            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                return respuesta.text
            else:
                print("Error: ", respuesta.status_code)
            # return 1
        except Exception as ex:
            print(f"Error {ex}")
            return 0

    def seleccionarServicio(self, row):
        try:
            return self.__lista_servicios[row]
        except Exception as ex:
            print(f"Error {ex}")

    # funciones auxiliares
    def __len__(self):
        return (
            len(self.__lista_servicios)
        )

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__lista_servicios):
            serv = self.__lista_servicios[self.cont]
            self.cont += 1
            return serv
        else:
            raise StopIteration
