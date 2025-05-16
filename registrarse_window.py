from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import time
import requests


class RegistrarseWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrarse")

        # Crear widgets
        self.username_label = QLabel("Nombre de usuario:")
        self.username_edit = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit()
        self.password_label = QLabel("Contraseña:")
        self.password_edit = QLineEdit()
        self.registrar_button = QPushButton("REGISTRARSE")
        self.cancel_button = QPushButton("CANCELAR")
        self.error_label = QLabel()

        # Crear el diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.registrar_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.error_label)

        self.setLayout(layout)

        self.resize(400, 250)  # Ancho: 400, Alto: 200
        self.registrar_button.clicked.connect(self.registrar)
        self.cancel_button.clicked.connect(self.cancel)

    def registrar(self):
        self.crearCuenta()
        time.sleep(3)
        self.accept()

    def crearCuenta(self):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/RegistrarUsuario.php'
            nombre = self.username_edit.text()
            email = self.email_edit.text()
            contrasena = self.password_edit.text()

            if nombre == "" or email == "" or contrasena == "":
                QMessageBox.information(
                    None,
                    "Error",
                    "Datos no validos"
                )
                return

            datos = {'nombre': nombre, 'email': email,
                     'contrasena': contrasena}

            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                print(respuesta.text)
                QMessageBox.information(
                    None,
                    "Exito",
                    "Cuenta registrada"
                )
            else:
                print("Error: ", respuesta.status_code)
                QMessageBox.information(
                    None,
                    "Error",
                    "No se registro"
                )
            # return 1
        except Exception as ex:
            print(f"Error {ex}")
            QMessageBox.information(
                None,
                "Error",
                "No se pudo registrar"
            )

    def cancel(self):
        self.reject()
