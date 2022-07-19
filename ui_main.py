# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba1.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QColumnView, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableView, QToolBar, QVBoxLayout,
    QWidget, QComboBox)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import recursos




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 481)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setWindowTitle('One Piece')
        MainWindow.setStyleSheet(u"")
        self.action_1_Cap = QAction(MainWindow)
        self.action_1_Cap.setObjectName(u"action_1_Cap")
        icon = QIcon()
        icon.addFile(u":/Actions/1logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_1_Cap.setIcon(icon)
        
        self.action_3_Cap = QAction(MainWindow)
        self.action_3_Cap.setObjectName(u"action_3_Cap")
        icon1 = QIcon()
        icon1.addFile(u":/Actions/3logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_3_Cap.setIcon(icon1)
        self.action_5_Cap = QAction(MainWindow)
        self.action_5_Cap.setObjectName(u"action_5_Cap")
        icon2 = QIcon()
        icon2.addFile(u":/Actions/5logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_5_Cap.setIcon(icon2)
        self.action_10_Cap = QAction(MainWindow)
        self.action_10_Cap.setObjectName(u"action_10_Cap")
        icon3 = QIcon()
        icon3.addFile(u":/Actions/10logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_10_Cap.setIcon(icon3)
        self.actionEditar_Cap = QAction(MainWindow)
        self.actionEditar_Cap.setObjectName(u"actionEditar_Cap")
        icon4 = QIcon()
        icon4.addFile(u":/Actions/database--arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEditar_Cap.setIcon(icon4)
        self.actionEliminar_Cap = QAction(MainWindow)
        self.actionEliminar_Cap.setObjectName(u"actionEliminar_Cap")
        icon5 = QIcon()
        icon5.addFile(u":/Actions/database--minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar_Cap.setIcon(icon5)
        self.actionActual_Cap = QAction(MainWindow)
        self.actionActual_Cap.setObjectName(u"actionActual_Cap")
        icon6 = QIcon()
        icon6.addFile(u":/Actions/infinitoLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionActual_Cap.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setCursor(QCursor(Qt.ArrowCursor))
        self.tabs.setStyleSheet(u"QTabWidget{\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"QLineEdit { background-color: white; border: 2px solid black; }" "\n"
"\n"
"QPushButton {\n"
" font: 20pt \"Ink Free\";\n"
" border: 1px solid black;\n"
" border-radius: 5px ;\n"
" background-color: rgb(255, 255, 135);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setTabShape(QTabWidget.Rounded)
        self.Fondos = QWidget()
        self.Fondos.setObjectName(u"Fondos")
        self.Fondos.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.Fondos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imgFondo_label = QLabel(self.Fondos)
        self.imgFondo_label.setObjectName(u"label")
        self.imgFondo_label.setMinimumSize(QSize(600, 338))
        self.imgFondo_label.setPixmap(QPixmap(u":/luffy/luffyultrainstinto.jpg"))
        self.imgFondo_label.setAlignment(Qt.AlignCenter)
        self.imgFondo_label.setScaledContents(True)


        self.verticalLayout_2.addWidget(self.imgFondo_label)

        icon7 = QIcon()
        icon7.addFile(u":/luffy/LS.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.Fondos, icon7, "")
        self.salaControl_tab = QWidget()
        self.salaControl_tab.setObjectName(u"salaControl_tab")
        self.salaControl_tab.setStyleSheet(u"QWidget#salaControl_tab{\n"
"	background-image: url(:/luffy/LSHD.jpg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.salaControl_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.apanio = QLabel(self.salaControl_tab)
        self.apanio.setObjectName(u"apanio")
        self.apanio1 = QLabel(self.salaControl_tab)
        self.apanio1.setObjectName(u"apanio1")
        self.apanio2 = QLabel(self.salaControl_tab)
        self.apanio2.setObjectName(u"apanio2")
        self.apanio3 = QLabel(self.salaControl_tab)
        self.apanio3.setObjectName(u"apanio3")
        self.apanio4 = QLabel(self.salaControl_tab)
        self.apanio4.setObjectName(u"apanio4")
        self.apanio5 = QLabel(self.salaControl_tab)
        self.apanio5.setObjectName(u"apanio5")
        

        self.verticalLayout.addWidget(self.apanio)
        self.verticalLayout.addWidget(self.apanio1)
        self.verticalLayout.addWidget(self.apanio2)
        self.verticalLayout.addWidget(self.apanio3)
        self.verticalLayout.addWidget(self.apanio4)
        self.verticalLayout.addWidget(self.apanio5)

        self.gB_SC = QGroupBox(self.salaControl_tab)
        self.gB_SC.setObjectName(u"gB_SC")
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(12)
        font.setBold(False)
        self.gB_SC.setFont(font)
        self.gB_SC.setStyleSheet(u"QGroupBox{\n"
"	 background-color: rgb(255, 255, 255);\n"
"	border: 2px solid black;\n"
"	 border-radius: 10px ;\n"
"}")
        self.gridLayout = QGridLayout(self.gB_SC)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(6, 14, 6, 6)
        self.capVistos_label = QLabel(self.gB_SC)
        self.capVistos_label.setObjectName(u"capVistos_label")
        font1 = QFont()
        font1.setFamilies([u"Ink Free"])
        font1.setPointSize(20)
        font1.setUnderline(True)
        self.capVistos_label.setFont(font1)
        self.capVistos_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.capVistos_label, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mas3_button = QPushButton(self.gB_SC)
        self.mas3_button.setObjectName(u"mas3_button")
        self.mas3_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.mas3_button, 1, 1, 1, 1)

        self.capTotales_label = QLabel(self.gB_SC)
        self.capTotales_label.setObjectName(u"capTotales_label")
        self.capTotales_label.setFont(font1)
        self.capTotales_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.capTotales_label, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.anteriorWallpapaer_button = QPushButton(self.gB_SC)
        self.anteriorWallpapaer_button.setObjectName(u"anteriorWallpapaer_button")
        font2 = QFont()
        font2.setFamilies([u"Ink Free"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.anteriorWallpapaer_button.setFont(font2)
        self.anteriorWallpapaer_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.anteriorWallpapaer_button, 2, 0, 1, 1)

        self.mas10_button = QPushButton(self.gB_SC)
        self.mas10_button.setObjectName(u"mas10_button")
        self.mas10_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.mas10_button, 2, 1, 1, 1)

        self.porcentajeVisto_label = QLabel(self.gB_SC)
        self.porcentajeVisto_label.setObjectName(u"porcentajeVisto_label")
        self.porcentajeVisto_label.setFont(font1)

        self.gridLayout.addWidget(self.porcentajeVisto_label, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mas5_button = QPushButton(self.gB_SC)
        self.mas5_button.setObjectName(u"mas5_button")
        self.mas5_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.mas5_button, 1, 2, 1, 1)

        self.posteriorWallpapaper_button = QPushButton(self.gB_SC)
        self.posteriorWallpapaper_button.setObjectName(u"posteriorWallpapaper_button")
        self.posteriorWallpapaper_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.posteriorWallpapaper_button, 2, 2, 1, 1)

        self.mas1_button = QPushButton(self.gB_SC)
        self.mas1_button.setObjectName(u"mas1_button")
        self.mas1_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.mas1_button, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.gB_SC)

        icon8 = QIcon()
        icon8.addFile(u":/logo/lawLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.salaControl_tab, icon8, "")
        self.historial = QWidget()
        self.historial.setObjectName(u"historial")
        self.historial.setStyleSheet(u"QWidget{\n"
"background-color: rgb(127, 48, 252)\n"
"}\n"
"\n"
"QGroupBox{\n"
"background-color: rgb(255, 255, 0)\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgb(255, 255, 0)\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QTableView{\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.historial)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_historial = QGroupBox(self.historial)
        self.groupBox_historial.setObjectName(u"groupBox_historial")
        self.groupBox_historial.setStyleSheet(u"QGroupBox {\n"
" font: 24pt \"Ink Free\";\n"
"text-decoration: underline;\n"
"}\n"
"QLabel{\n"
" font: 16pt \"Ink Free\";\n"
"}")
        self.formLayout = QFormLayout(self.groupBox_historial)
        self.formLayout.setObjectName(u"formLayout")
        self.capitulo_label = QLabel(self.groupBox_historial)
        self.capitulo_label.setObjectName(u"capitulo_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.capitulo_label)

        self.capitulo_LE = QLineEdit(self.groupBox_historial)
        self.capitulo_LE.setObjectName(u"capitulo_LE")
        self.capitulo_LE.setPlaceholderText("Número de capítulo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.capitulo_LE)

        self.titulo_label = QLabel(self.groupBox_historial)
        self.titulo_label.setObjectName(u"titulo_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.titulo_label)

        self.titulo_LE = QLineEdit(self.groupBox_historial)
        self.titulo_LE.setObjectName(u"titulo_LE")
        self.titulo_LE.setPlaceholderText("Título del capítulo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.titulo_LE)

        self.dia_label = QLabel(self.groupBox_historial)
        self.dia_label.setObjectName(u"dia_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.dia_label)

        self.dia_LE = QLineEdit(self.groupBox_historial)
        self.dia_LE.setObjectName(u"dia_LE")
        self.dia_LE.setPlaceholderText("Día y hora en la que se vió el capítulo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dia_LE)

        self.personas_label = QLabel(self.groupBox_historial)
        self.personas_label.setObjectName(u"personas_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.personas_label)

        self.personas_LE = QLineEdit(self.groupBox_historial)
        self.personas_LE.setObjectName(u"personas_LE")
        self.personas_LE.setPlaceholderText("Personas que vieron el capítulo")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.personas_LE)


        self.verticalLayout_6.addWidget(self.groupBox_historial)


        self.tablaDB = QTableView(self.historial)
        self.tablaDB.setObjectName(u"tablaDB")
        self.tablaDB.showFullScreen()

        self.verticalLayout_6.addWidget(self.tablaDB)

        icon9 = QIcon()
        icon9.addFile(u":/logo/historialLogo.jfif", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.historial, icon9, "")
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setStyleSheet(u"QWidget#main_tab{\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.main_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.subirIMG_label = QLabel(self.main_tab)
        self.subirIMG_label.setObjectName(u"subirIMG_label")
        self.subirIMG_label.setMinimumSize(QSize(600, 338))
        self.subirIMG_label.setScaledContents(True)
        self.subirIMG_label.setBaseSize(QSize(0, 0))
        self.subirIMG_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.subirIMG_label.setPixmap(QPixmap(u":/luffy/imgGaleria.jpg"))
        self.subirIMG_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.subirIMG_label)

        self.fondos_CB = QComboBox(self.main_tab)
        self.fondos_CB.setObjectName(u"fondos_CB")
        self.fondos_CB.setCursor(QCursor(Qt.PointingHandCursor))
        self.fondos_CB.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(255, 255, 135);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(0, 0, 0);\n"
"font: 16pt \"Ink Free\";\n"
"text-align:center;\n"
"padding: 2px;\n"
"}\n")

        self.verticalLayout_4.addWidget(self.fondos_CB)

        icon10 = QIcon()
        icon10.addFile(u":/logo/logoOnePiece2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon10)
        self.tabs.addTab(self.main_tab, icon10, "")

        self.horizontalLayout_5.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 18))
        self.menuCap = QMenu(self.menubar)
        self.menuCap.setObjectName(u"menuCap")
        self.menuAnadir_Cap = QMenu(self.menuCap)
        self.menuAnadir_Cap.setObjectName(u"menuAnadir_Cap")
        icon11 = QIcon()
        icon11.addFile(u":/Actions/database--plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuAnadir_Cap.setIcon(icon11)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuCap.menuAction())
        self.menuCap.addAction(self.menuAnadir_Cap.menuAction())
        self.menuCap.addAction(self.actionEditar_Cap)
        self.menuCap.addAction(self.actionEliminar_Cap)
        self.menuAnadir_Cap.addAction(self.action_1_Cap)
        self.menuAnadir_Cap.addAction(self.action_3_Cap)
        self.menuAnadir_Cap.addAction(self.action_5_Cap)
        self.menuAnadir_Cap.addAction(self.action_10_Cap)
        self.menuAnadir_Cap.addAction(self.actionActual_Cap)
        self.toolBar.addAction(self.action_1_Cap)
        self.toolBar.addAction(self.action_3_Cap)
        self.toolBar.addAction(self.action_5_Cap)
        self.toolBar.addAction(self.action_10_Cap)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"One Piece", None))
        self.action_1_Cap.setText(QCoreApplication.translate("MainWindow", u"+1 Cap\u00edtulo", None))
#if QT_CONFIG(shortcut)
        self.action_1_Cap.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.action_3_Cap.setText(QCoreApplication.translate("MainWindow", u"+3 Cap\u00edtulos", None))
#if QT_CONFIG(shortcut)
        self.action_3_Cap.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.action_5_Cap.setText(QCoreApplication.translate("MainWindow", u"+5 Cap\u00edtulos", None))
#if QT_CONFIG(shortcut)
        self.action_5_Cap.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+5", None))
#endif // QT_CONFIG(shortcut)
        self.action_10_Cap.setText(QCoreApplication.translate("MainWindow", u"+10 Cap\u00edtulos", None))
#if QT_CONFIG(shortcut)
        self.action_10_Cap.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+0", None))
#endif // QT_CONFIG(shortcut)
        self.actionEditar_Cap.setText(QCoreApplication.translate("MainWindow", u"Editar Cap\u00edtulos", None))
#if QT_CONFIG(shortcut)
        self.actionEditar_Cap.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionEliminar_Cap.setText(QCoreApplication.translate("MainWindow", u"Eliminar Cap\u00edtulos", None))
#if QT_CONFIG(shortcut)
        self.actionEliminar_Cap.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionActual_Cap.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir los que quiera", None))
        self.imgFondo_label.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.Fondos), QCoreApplication.translate("MainWindow", u"Fondos", None))
        self.gB_SC.setTitle(QCoreApplication.translate("MainWindow", u"", None))
        self.capVistos_label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos vistos: 0", None))
        self.mas3_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +3 cap a Visto", None))
        self.capTotales_label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos totales: 0", None))
        self.anteriorWallpapaer_button.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.mas10_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +10 cap a Visto", None))
        self.porcentajeVisto_label.setText(QCoreApplication.translate("MainWindow", u"Visto: 0%", None))
        self.mas5_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +5 cap a Visto", None))
        self.posteriorWallpapaper_button.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.mas1_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +1 cap a Visto", None))
        self.tabs.setTabText(self.tabs.indexOf(self.salaControl_tab), QCoreApplication.translate("MainWindow", u"Sala de Control", None))
        self.groupBox_historial.setTitle(QCoreApplication.translate("MainWindow", u"Datos de los cap\u00edtulos vistos:", None))
        self.capitulo_label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulo", None))
        self.titulo_label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.dia_label.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.personas_label.setText(QCoreApplication.translate("MainWindow", u"Personas", None))
        self.tabs.setTabText(self.tabs.indexOf(self.historial), QCoreApplication.translate("MainWindow", u"Historial", None))
        self.subirIMG_label.setText("")
        self.fondos_CB.setCurrentText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"Galer\u00eda", None))
        self.menuCap.setTitle(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos", None))
        self.menuAnadir_Cap.setTitle(QCoreApplication.translate("MainWindow", u"A\u00f1adir Cap\u00edtulos", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

