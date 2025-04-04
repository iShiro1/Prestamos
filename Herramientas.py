# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Herramientas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(715, 644)
        icon = QIcon()
        icon.addFile(u":/iconos/Logo2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionUsuario = QAction(MainWindow)
        self.actionUsuario.setObjectName(u"actionUsuario")
        self.actionAdministrador = QAction(MainWindow)
        self.actionAdministrador.setObjectName(u"actionAdministrador")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/Cerrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSalir.setIcon(icon1)
        self.actionUsuario_2 = QAction(MainWindow)
        self.actionUsuario_2.setObjectName(u"actionUsuario_2")
        self.actionContrase_a = QAction(MainWindow)
        self.actionContrase_a.setObjectName(u"actionContrase_a")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/iconos/Prestamo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon2, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        icon3 = QIcon()
        icon3.addFile(u":/iconos/Devolucion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon3, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableView_2 = QTableView(self.tab_3)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_4.addWidget(self.tableView_2)

        icon4 = QIcon()
        icon4.addFile(u":/iconos/Pendiente.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_3, icon4, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableView_3 = QTableView(self.tab_4)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_5.addWidget(self.tableView_3)

        icon5 = QIcon()
        icon5.addFile(u":/iconos/Entregado.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tab_4, icon5, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 715, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuAgregar = QMenu(self.menuMenu)
        self.menuAgregar.setObjectName(u"menuAgregar")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/agregar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuAgregar.setIcon(icon6)
        self.menuModificar = QMenu(self.menuMenu)
        self.menuModificar.setObjectName(u"menuModificar")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/modificar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuModificar.setIcon(icon7)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionSalir)
        self.menuMenu.addAction(self.menuModificar.menuAction())
        self.menuMenu.addAction(self.menuAgregar.menuAction())
        self.menuAgregar.addAction(self.actionUsuario)
        self.menuAgregar.addAction(self.actionAdministrador)
        self.menuModificar.addAction(self.actionUsuario_2)
        self.menuModificar.addAction(self.actionContrase_a)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Prestamos", None))
        self.actionUsuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.actionAdministrador.setText(QCoreApplication.translate("MainWindow", u"Herramienta", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionSalir.setIconText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionUsuario_2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.actionContrase_a.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Prestamo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre de usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Herramienta", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Prestamo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre de usuario", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Devolver", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Devolucion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pendiente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Entregado", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAgregar.setTitle(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.menuModificar.setTitle(QCoreApplication.translate("MainWindow", u"Modificar", None))
    # retranslateUi

