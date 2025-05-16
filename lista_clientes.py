
import json
import requests
from cliente import Cliente


class ListaClientes():
    __lista_clientes = []

    def crearCliente(self, cliente: Cliente):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/clientes/agregarCliente.php'
            datos = {'nombre': cliente.obtenerNombre, 'telefono': cliente.obtenerTelefono,
                     'descripcion': cliente.obtenerDescripcion}

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

    def mostrarClientes(self):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/clientes/mostrarClientes.php'
            respuesta = requests.get(url, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                print(respuesta.text)
                lista = json.loads(respuesta.text)

                if 'error' in lista:
                    self.__lista_clientes.clear()
                    return

                self.__lista_clientes = [
                    Cliente(**cliente) for cliente in lista]
            else:
                print("Error: ", respuesta.status_code)
            # return 1
        except Exception as ex:
            print(f"Error {ex}")

    def actualizarCliente(self, cliente):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/clientes/actualizarCliente.php'
            datos = {'id': cliente.obtenerId, 'nombre': cliente.obtenerNombre, 'telefono': cliente.obtenerTelefono,
                     'descripcion': cliente.obtenerDescripcion}

            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                print(respuesta.text)
                return respuesta.text

            else:
                print("Error: ", respuesta.status_code)
                return 0
            # return 1
        except Exception as ex:
            print(f"Error {ex}")
            return 0

    def eliminarCliente(self, id):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/clientes/eliminarCliente.php'
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

    def seleccionarCliente(self, row):
        try:
            return self.__lista_clientes[row]
        except Exception as ex:
            print(f"Error {ex}")

    # funciones auxiliares
    def __len__(self):
        return (
            len(self.__lista_clientes)
        )

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__lista_clientes):
            cliente = self.__lista_clientes[self.cont]
            self.cont += 1
            return cliente
        else:
            raise StopIteration
