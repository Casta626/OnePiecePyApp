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
from PySide6.QtWidgets import (QApplication, QColumnView, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import recursos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(745, 503)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setStyleSheet(u"QTabWidget{\n"
"background-image: url(:/luffy/merry.jpg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	qproperty-scaledContents: true;\n"
"}")
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setStyleSheet(u"QWidget{\n"
"    background-image: url(:/luffy/gear5.jpg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	qproperty-scaledContents: true;\n"
"}\n"
"\n"
"QLabel{\n"
"background-image: url(:/luffy/gear4TankMan.jpg);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-image: url(:/luffy/gear4TankMan.jpg);\n"
"}\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.main_tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        icon = QIcon()
        icon.addFile(u":/luffy/logoOnePiece.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.main_tab, icon, "")
        self.salaControl_tab = QWidget()
        self.salaControl_tab.setObjectName(u"salaControl_tab")
        self.salaControl_tab.setStyleSheet(u"QWidget{\n"
"background-image: url(:/luffy/merry.jpg);\n"
"	background-repeat: no-repeat;\n"
"	background-position: center;\n"
"	qproperty-scaledContents: true;\n"
"}\n"
"\n"
"QLabel{\n"
"background-image: url(:/luffy/gear4TankMan.jpg);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-image: url(:/luffy/gear4TankMan.jpg);\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.salaControl_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.salaControl_tab)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"background-image: url(:/luffy/gear4TankMan.jpg);\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.label_3 = QLabel(self.salaControl_tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_2 = QLabel(self.salaControl_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.salaControl_tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_2 = QPushButton(self.salaControl_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.salaControl_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButton_3 = QPushButton(self.salaControl_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

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
"QColumnView{\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.historial)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.historial)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.columnView = QColumnView(self.historial)
        self.columnView.setObjectName(u"columnView")

        self.verticalLayout_6.addWidget(self.columnView)

        self.tabs.addTab(self.historial, "")

        self.horizontalLayout_5.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 745, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabs.setTabText(self.tabs.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"One Piece", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos totales: 0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Visto: 0%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulos vistos: 0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +1 cap a Visto", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +3 cap a Visto", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +5 cap a Visto", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir +10 cap a Visto", None))
        self.tabs.setTabText(self.tabs.indexOf(self.salaControl_tab), QCoreApplication.translate("MainWindow", u"Sala de Control", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos de los cap\u00edtulos vistos:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cap\u00edtulo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Personas", None))
        self.tabs.setTabText(self.tabs.indexOf(self.historial), QCoreApplication.translate("MainWindow", u"Historial", None))
    # retranslateUi

