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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QTableView, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)
import recursos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1269, 912)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
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
"\n"
"QPushButton {\n"
" font: 20pt \"Ink Free\";\n"
" border: 1px solid black;\n"
" border-radius: 5px ;\n"
" background-color: rgb(255, 255, 135);\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.imagenFondo = "merry2.jpg"
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setStyleSheet(u"QWidget#main_tab{\n"
"    background-image: url(:/luffy/"+self.imagenFondo+");\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"}\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.main_tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        icon = QIcon()
        icon.addFile(u":/luffy/logoOnePiece.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.main_tab, icon, "")
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

        self.verticalLayout.addWidget(self.apanio)

        self.apanio_2 = QLabel(self.salaControl_tab)
        self.apanio_2.setObjectName(u"apanio_2")
        self.apanio_2.setMaximumSize(QSize(400, 16777215))
        

        self.verticalLayout.addWidget(self.apanio_2)

        self.apanio_3 = QLabel(self.salaControl_tab)
        self.apanio_3.setObjectName(u"apanio_3")

        self.verticalLayout.addWidget(self.apanio_3)

        self.apanio_4 = QLabel(self.salaControl_tab)
        self.apanio_4.setObjectName(u"apanio_4")

        self.verticalLayout.addWidget(self.apanio_4)

        self.apanio_5 = QLabel(self.salaControl_tab)
        self.apanio_5.setObjectName(u"apanio_5")

        self.verticalLayout.addWidget(self.apanio_5)

        self.apanio_6 = QLabel(self.salaControl_tab)
        self.apanio_6.setObjectName(u"apanio_6")

        self.verticalLayout.addWidget(self.apanio_6)

        self.apanio_7 = QLabel(self.salaControl_tab)
        self.apanio_7.setObjectName(u"apanio_7")

        self.verticalLayout.addWidget(self.apanio_7)

        self.apanio_8 = QLabel(self.salaControl_tab)
        self.apanio_8.setObjectName(u"apanio_8")

        self.verticalLayout.addWidget(self.apanio_8)

        self.gB_SC = QGroupBox(self.salaControl_tab)
        self.gB_SC.setObjectName(u"gB_SC")
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(18)
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

        self.capTotales_label = QLabel(self.gB_SC)
        self.capTotales_label.setObjectName(u"capTotales_label")
        self.capTotales_label.setFont(font1)
        self.capTotales_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.capTotales_label, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.porcentajeVisto_label = QLabel(self.gB_SC)
        self.porcentajeVisto_label.setObjectName(u"porcentajeVisto_label")
        self.porcentajeVisto_label.setFont(font1)

        self.gridLayout.addWidget(self.porcentajeVisto_label, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mas1_button = QPushButton(self.gB_SC)
        self.mas1_button.setObjectName(u"mas1_button")

        self.gridLayout.addWidget(self.mas1_button, 1, 0, 1, 1)

        self.mas3_button = QPushButton(self.gB_SC)
        self.mas3_button.setObjectName(u"mas3_button")

        self.gridLayout.addWidget(self.mas3_button, 1, 1, 1, 1)

        self.mas5_button = QPushButton(self.gB_SC)
        self.mas5_button.setObjectName(u"mas5_button")

        self.gridLayout.addWidget(self.mas5_button, 1, 2, 1, 1)

        self.mas10_button = QPushButton(self.gB_SC)
        self.mas10_button.setObjectName(u"mas10_button")

        self.gridLayout.addWidget(self.mas10_button, 2, 1, 1, 1)

        self.anteriorWallpapaer_button = QPushButton(self.gB_SC)
        self.anteriorWallpapaer_button.setObjectName(u"anteriorWallpapaer_button")
        font2 = QFont()
        font2.setFamilies([u"Ink Free"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.anteriorWallpapaer_button.setFont(font2)

        self.gridLayout.addWidget(self.anteriorWallpapaer_button, 2, 0, 1, 1)

        self.posteriorWallpapaper_button = QPushButton(self.gB_SC)
        self.posteriorWallpapaper_button.setObjectName(u"posteriorWallpapaper_button")

        self.gridLayout.addWidget(self.posteriorWallpapaper_button, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.gB_SC)

        self.tabs.addTab(self.salaControl_tab, "")
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
        self.groupBox = QGroupBox(self.historial)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.capitulo_label = QLabel(self.groupBox)
        self.capitulo_label.setObjectName(u"capitulo_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.capitulo_label)

        self.capitulo_LE = QLineEdit(self.groupBox)
        self.capitulo_LE.setObjectName(u"capitulo_LE")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.capitulo_LE)

        self.dia_label = QLabel(self.groupBox)
        self.dia_label.setObjectName(u"dia_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dia_label)

        self.dia_LE = QLineEdit(self.groupBox)
        self.dia_LE.setObjectName(u"dia_LE")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dia_LE)

        self.personas_label = QLabel(self.groupBox)
        self.personas_label.setObjectName(u"personas_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.personas_label)

        self.personas_LE = QLineEdit(self.groupBox)
        self.personas_LE.setObjectName(u"personas_LE")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.personas_LE)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.tablaDB = QTableView(self.historial)
        self.tablaDB.setObjectName(u"tablaDB")

        self.verticalLayout_6.addWidget(self.tablaDB)

        self.tabs.addTab(self.historial, "")

        self.horizontalLayout_5.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1269, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabs.setTabText(self.tabs.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"One Piece", None))
        self.apanio.setText("")
        self.apanio_2.setText("")
        self.apanio_3.setText("")
        self.apanio_4.setText("")
        self.apanio_5.setText("")
        self.apanio_6.setText("")
        self.apanio_7.setText("")
        self.apanio_8.setText("")
        self.gB_SC.setTitle("")
        self.capVistos_label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos vistos: 0", None))
        self.capTotales_label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos totales: 0", None))
        self.porcentajeVisto_label.setText(QCoreApplication.translate("MainWindow", u"Visto: 0%", None))
        self.mas1_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +1 cap a Visto", None))
        self.mas3_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +3 cap a Visto", None))
        self.mas5_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +5 cap a Visto", None))
        self.mas10_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +10 cap a Visto", None))
        self.anteriorWallpapaer_button.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.posteriorWallpapaper_button.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.tabs.setTabText(self.tabs.indexOf(self.salaControl_tab), QCoreApplication.translate("MainWindow", u"Sala de Control", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos de los cap\u00edtulos vistos:", None))
        self.capitulo_label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulo", None))
        self.dia_label.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.personas_label.setText(QCoreApplication.translate("MainWindow", u"Personas", None))
        self.tabs.setTabText(self.tabs.indexOf(self.historial), QCoreApplication.translate("MainWindow", u"Historial", None))
    # retranslateUi

