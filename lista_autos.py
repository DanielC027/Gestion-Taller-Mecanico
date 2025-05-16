
import json
import requests
from auto import Auto


class ListaAutos():
    __lista_autos = []

    def crearAuto(self, auto: Auto):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/autos/agregarAuto.php'
            datos = {'id_cliente': auto.obtenerIdCliente, 'modelo': auto.obtenerModelo,
                     'marca': auto.obtenerMarca, 'anio': auto.obtenerAnio, 'descripcion': auto.obtenerDescripcion}

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

    def mostrarAutos(self, id_cliente):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/autos/mostrarAutos.php'
            datos = {'id_cliente': id_cliente}
            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                print(respuesta.text)
                lista = json.loads(respuesta.text)
                print("Lista:::", lista)

                if 'error' in lista:
                    self.__lista_autos.clear()
                    return

                self.__lista_autos = [
                    Auto(**auto) for auto in lista]
            else:
                print("Error: ", respuesta.status_code)
            # return 1
        except Exception as ex:
            print(f"Error {ex}")

    def actualizarAuto(self, auto):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/autos/actualizarAuto.php'
            datos = {'id': auto.obtenerId, 'id_cliente': auto.obtenerIdCliente, 'modelo': auto.obtenerModelo,
                     'marca': auto.obtenerMarca, 'anio': auto.obtenerAnio, 'descripcion': auto.obtenerDescripcion}

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

    def eliminarAuto(self, id):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/autos/eliminarAuto.php'
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

    def seleccionarAuto(self, row):
        try:
            return self.__lista_autos[row]
        except Exception as ex:
            print(f"Error {ex}")

    # funciones auxiliares
    def __len__(self):
        return (
            len(self.__lista_autos)
        )

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__lista_autos):
            auto = self.__lista_autos[self.cont]
            self.cont += 1
            return auto
        else:
            raise StopIteration
