from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from registrarse_window import RegistrarseWindow
import requests


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.attemps = 0

        self.setWindowTitle("Inicio de Sesión")

        # Crear widgets
        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit()
        self.password_label = QLabel("Contraseña:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("INICIAR SESIÓN")
        self.cancel_button = QPushButton("CANCELAR")
        self.registrarse_button = QPushButton("Registrarse")
        self.error_label = QLabel()

        # Crear el diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.registrarse_button)
        layout.addWidget(self.error_label)

        self.setLayout(layout)

        self.resize(400, 250)  # Ancho: 400, Alto: 200
        self.login_button.clicked.connect(self.login)
        self.cancel_button.clicked.connect(self.cancel)
        self.registrarse_button.clicked.connect(self.registrarse)

    def login(self):
        # Realizar la verificación de la contraseña
        if self.verificarCuenta() == 1:
            # Contraseña correcta, permitir el acceso al sistema
            self.accept()
        else:
            QMessageBox.information(
                None,
                "Error",
                "No se encotro la cuenta\n O contraseña incorrecta"
            )
            if self.attemps < 5:
                self.attemps += 1
            else:
                self.cancel()

    def verificarCuenta(self):
        try:
            url = 'https://serviciocanela.000webhostapp.com/Main/IniciarSesion.php'

            email = self.email_edit.text()
            contrasena = self.password_edit.text()

            if email == "" or contrasena == "":
                QMessageBox.information(
                    None,
                    "Error",
                    "Datos no validos"
                )
                return 0

            datos = {'email': email,
                     'contrasena': contrasena}

            respuesta = requests.get(url, params=datos, timeout=5)

            if respuesta.status_code == 200:
                # se extrae la informacion y se pone en la lista
                print(respuesta.text)
                resp = respuesta.text
                if resp == "0" or resp == "3":
                    return 0
                else:
                    return 1
            else:
                print("Error: ", respuesta.status_code)
                QMessageBox.information(
                    None,
                    "Error",
                    "No se pudo conectar al servidor"
                )
                return 0
            # return 1
        except Exception as ex:
            print(f"Error {ex}")
            QMessageBox.information(
                None,
                "Error",
                "No se encontro el usuario"
            )
            return 0

    def registrarse(self):
        registra = RegistrarseWindow()
        registra.exec_()

    def cancel(self):
        self.reject()
