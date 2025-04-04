import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QComboBox

# Conexión a la base de datos
def init_db():
    conn = sqlite3.connect("prestamos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'usuario'))
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS herramientas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            disponible INTEGER DEFAULT 1
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            herramienta_id INTEGER NOT NULL,
            fecha_prestamo TEXT NOT NULL,
            fecha_devolucion TEXT,
            FOREIGN KEY (herramienta_id) REFERENCES herramientas(id)
        )
    """)
    conn.commit()
    conn.close()
init_db()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        self.label_user = QLabel("Usuario:")
        self.input_user = QLineEdit()
        self.label_pass = QLabel("Contraseña:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Ingresar")
        self.login_button.clicked.connect(self.login)
        
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.input_pass)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def login(self):
        username = self.input_user.text()
        password = self.input_pass.text()
        
        conn = sqlite3.connect("prestamos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM usuarios WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            self.main_window = MainWindow(username, user[0])
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
class MainWindow(QMainWindow):
    def __init__(self, username, role):
        super().__init__()
        self.setWindowTitle("Sistema de Préstamos de Herramientas")
        self.setGeometry(100, 100, 400, 300)

        self.username = username  # Agrega esta línea
        self.role = role

        layout = QVBoxLayout()
        self.label = QLabel(f"Bienvenido, {username} ({role})")
        layout.addWidget(self.label)

        if role == "admin":
            self.btn_registro_herramienta = QPushButton("Registrar Nueva Herramienta")
            self.btn_registro_herramienta.clicked.connect(self.registrar_herramienta)
            layout.addWidget(self.btn_registro_herramienta)

            self.btn_prestamo = QPushButton("Realizar Préstamo")
            self.btn_prestamo.clicked.connect(self.realizar_prestamo)
            layout.addWidget(self.btn_prestamo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    
    def registrar_herramienta(self):
        self.registro_window = RegistroHerramienta()
        self.registro_window.show()
    
    def realizar_prestamo(self):
        self.prestamo_window = PrestamoHerramienta(self.username)  # Pasar el nombre de usuario
        self.prestamo_window.show()


class RegistroHerramienta(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Herramienta")
        self.setGeometry(150, 150, 300, 200)
        
        layout = QVBoxLayout()
        self.label_nombre = QLabel("Nombre de la Herramienta:")
        self.input_nombre = QLineEdit()
        self.label_desc = QLabel("Descripción:")
        self.input_desc = QLineEdit()
        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.clicked.connect(self.guardar_herramienta)
        
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_desc)
        layout.addWidget(self.input_desc)
        layout.addWidget(self.btn_guardar)
        self.setLayout(layout)
    
    def guardar_herramienta(self):
        nombre = self.input_nombre.text()
        descripcion = self.input_desc.text()
        
        if nombre:
            conn = sqlite3.connect("prestamos.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO herramientas (nombre, descripcion) VALUES (?, ?)", (nombre, descripcion))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Éxito", "Herramienta registrada correctamente")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "El nombre es obligatorio")


class PrestamoHerramienta(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Realizar Préstamo")
        self.setGeometry(200, 200, 400, 300)
        self.username = username
        
        layout = QVBoxLayout()

        # Configuración de la tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["ID", "Herramienta"])
        
        # Llamar a cargar_herramientas al inicio
        self.cargar_herramientas()

        layout.addWidget(self.tabla)

        # Botón para realizar el préstamo
        self.btn_prestar = QPushButton("Prestar")
        self.btn_prestar.clicked.connect(self.prestar_herramienta)
        layout.addWidget(self.btn_prestar)

        self.setLayout(layout)

    def cargar_herramientas(self):
        # Conexión a la base de datos
        conn = sqlite3.connect("prestamos.db")
        cursor = conn.cursor()
        
        # Seleccionar solo las herramientas disponibles (disponible=1)
        cursor.execute("SELECT id, nombre FROM herramientas WHERE disponible=1")
        herramientas = cursor.fetchall()
        conn.close()
        
        # Si no hay herramientas disponibles, mostrar mensaje
        if not herramientas:
            QMessageBox.warning(self, "Aviso", "No hay herramientas disponibles para prestar.")
            return
        
        # Establecer el número de filas basado en el número de herramientas
        self.tabla.setRowCount(len(herramientas))
        
        # Agregar las herramientas a la tabla
        for i, (id, nombre) in enumerate(herramientas):
            self.tabla.setItem(i, 0, QTableWidgetItem(str(id)))
            self.tabla.setItem(i, 1, QTableWidgetItem(nombre))
    
    def prestar_herramienta(self):
        # Obtener la fila seleccionada en la tabla
        row = self.tabla.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Seleccione una herramienta para prestar")
            return

        # Obtener el ID de la herramienta seleccionada
        herramienta_id = int(self.tabla.item(row, 0).text())

        # Conexión a la base de datos
        conn = sqlite3.connect("prestamos.db")
        cursor = conn.cursor()
        
        # Actualizar la herramienta a no disponible
        cursor.execute("UPDATE herramientas SET disponible=0 WHERE id=?", (herramienta_id,))
        
        # Insertar el préstamo en la base de datos
        cursor.execute("INSERT INTO prestamos (usuario, herramienta_id, fecha_prestamo) VALUES (?, ?, date('now'))", (self.username, herramienta_id))
        
        conn.commit()
        conn.close()
        
        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Éxito", "Préstamo registrado correctamente")
        
        # Recargar las herramientas disponibles
        self.cargar_herramientas()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
