import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from interfaces.Herramientas import Ui_MainWindow
from qt_material import apply_stylesheet
import sys

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 300, 150)
        
        layout = QVBoxLayout()
        self.label_usuario = QLabel("Usuario:")
        self.input_usuario = QLineEdit()
        self.label_password = QLabel("Contraseña:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.boton_login = QPushButton("Iniciar Sesión")
        
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.boton_login)
        
        self.setLayout(layout)
        self.boton_login.clicked.connect(self.validar_usuario)
        self.usuario = None
    
    def validar_usuario(self):
        usuario = self.input_usuario.text().strip()
        password = self.input_password.text().strip()
        
        conexion = sqlite3.connect("prestamos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND password = ?", (usuario, password))
        resultado = cursor.fetchone()
        conexion.close()
        
        if resultado:
            self.usuario = usuario
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

class CambiarCredencialesDialog(QDialog):
    def __init__(self, usuario_actual):
        super().__init__()
        self.setWindowTitle("Modificar Usuario y Contraseña")
        self.usuario_actual = usuario_actual

        layout = QVBoxLayout()
        
        self.label_usuario = QLabel("Nuevo Usuario:")
        self.input_usuario = QLineEdit()
        
        self.label_password = QLabel("Nueva Contraseña:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        
        self.boton_guardar = QPushButton("Guardar Cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)
        
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.boton_guardar)
        
        self.setLayout(layout)

    def guardar_cambios(self):
        nuevo_usuario = self.input_usuario.text().strip()
        nueva_password = self.input_password.text().strip()
        
        if not nuevo_usuario or not nueva_password:
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos.")
            return
        
        conexion = sqlite3.connect("prestamos.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET nombre = ?, password = ? WHERE nombre = ?", 
                       (nuevo_usuario, nueva_password, self.usuario_actual))
        conexion.commit()
        conexion.close()
        
        QMessageBox.information(self, "Éxito", "Credenciales actualizadas correctamente.")
        self.accept()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setupUi(self)
        self.usuario = usuario
        self.conectar_eventos()
        self.crear_bd()
    
    def conectar_eventos(self):
        self.pushButton_2.clicked.connect(self.registrar_prestamo)
        self.pushButton.clicked.connect(self.devolver_herramienta)
        self.actionSalir.triggered.connect(self.close)
        self.actionUsuario_2.triggered.connect(self.modificar_credenciales)

    def modificar_credenciales(self):
        dialogo = CambiarCredencialesDialog(self.usuario)
        if dialogo.exec() == QDialog.Accepted:
            self.usuario = dialogo.input_usuario.text().strip()
    
    def crear_bd(self):
        conexion = sqlite3.connect("prestamos.db")
        cursor = conexion.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS herramientas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                disponible INTEGER DEFAULT 1
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                herramienta_id INTEGER,
                fecha_prestamo TEXT,
                fecha_devolucion TEXT,
                devuelto INTEGER DEFAULT 0,
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY(herramienta_id) REFERENCES herramientas(id)
            )
        ''')
        
        conexion.commit()
        conexion.close()
    
    def registrar_prestamo(self):
        herramienta = self.lineEdit_2.text().strip()
        
        if not herramienta:
            QMessageBox.warning(self, "Error", "Debe ingresar una herramienta.")
            return
        
        conexion = sqlite3.connect("prestamos.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT id FROM usuarios WHERE nombre = ?", (self.usuario,))
        usuario_data = cursor.fetchone()
        if not usuario_data:
            QMessageBox.warning(self, "Error", "El usuario no existe.")
            conexion.close()
            return
        usuario_id = usuario_data[0]
        
        cursor.execute("INSERT INTO herramientas (nombre, disponible) VALUES (?, 0)", (herramienta,))
        herramienta_id = cursor.lastrowid
        
        cursor.execute("INSERT INTO prestamos (usuario_id, herramienta_id, fecha_prestamo, devuelto) VALUES (?, ?, DATE('now'), 0)",
                       (usuario_id, herramienta_id))
        
        conexion.commit()
        conexion.close()
        
        QMessageBox.information(self, "Éxito", "Préstamo registrado correctamente.")
    
    def devolver_herramienta(self):
        conexion = sqlite3.connect("prestamos.db")
        cursor = conexion.cursor()
        
        cursor.execute("UPDATE prestamos SET fecha_devolucion = DATE('now'), devuelto = 1 WHERE usuario_id = (SELECT id FROM usuarios WHERE nombre = ?) AND devuelto = 0",
                       (self.usuario,))
        cursor.execute("UPDATE herramientas SET disponible = 1 WHERE id IN (SELECT herramienta_id FROM prestamos WHERE usuario_id = (SELECT id FROM usuarios WHERE nombre = ?) AND devuelto = 1)",
                       (self.usuario,))
        
        conexion.commit()
        conexion.close()
        
        QMessageBox.information(self, "Éxito", "Herramienta devuelta correctamente.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="light_blue.xml")  
    
    login = LoginDialog()
    if login.exec() == QDialog.Accepted:
        window = MainWindow(login.usuario)
        window.show()
        sys.exit(app.exec())