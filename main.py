# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QLineEdit, QComboBox
from PySide6.QtCore import QUrl
from PySide6.QtGui import (QPixmap)
from datetime import datetime

from ui_main import Ui_MainWindow
import webScraping
import DB



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lastCap = webScraping.ObtenerUltimoCapitulo().get_last_episode()
        self.currentCap = 410
        self.capActual = str(self.currentCap)
        print(self.lastCap)
        self.porcentaje = self.obtenerPorcentajeYDiferencia(self.currentCap, int(self.lastCap))

        self.action_1_Cap.triggered.connect(self.nueva)
        self.actionEditar_Cap.triggered.connect(self.modificar)
        self.actionEliminar_Cap.triggered.connect(self.borrar)
        self.mas1_button.clicked.connect(self.nueva)

        #self.webEngine.load(QUrl("https://www3.animeflv.net/ver/one-piece-tv-100"))
    
        #self.imgFondo_label.setPixmap(QPixmap("logoOnePiece2.png"))

        

        self.conectar()

    def avanzarHastaUltimoCap():
            print("Me pican los cocos")
    a= 102-87
    num = a
    for i in range(num):
        avanzarHastaUltimoCap()

    def obtenerPorcentajeYDiferencia(self, currentCap, lastCap):
        porcentaje = (currentCap*100) / lastCap
        rendondeo = round(porcentaje, 2)
        diferencia = lastCap - currentCap

        self.porcentajeVisto_label.setText(
            ("Porcentaje: " + str(rendondeo)+"%"))
        self.capVistos_label.setText("Capítulos vistos: "+str(currentCap))
        self.capTotales_label.setText("Capítulos totales: "+str(lastCap))

        # Hacer if con un num random por opening y ending

        # if  self.capActual < 

        if diferencia == 0:
            self.gB_SC.setTitle("Llegaste al último capítulo")
        if diferencia > 0:
            self.gB_SC.setTitle("Faltan "+str(diferencia)+" capítulos")
        # print("Diferencia: " + str(diferencia))
        if self.capActual.endswith("0"):
            self.gB_SC.setTitle("Otros 10 capítulos fuera") # Si el capítulo actual termina en 0, es porque estamos en el capítulo 10 
        if self.capActual.endswith("00"):
            self.gB_SC.setTitle("Ya te has ventilado otros 100 capítulos, ya queda menos") # Si el capítulo actual termina en 00, es porque estamos en el capítulo 100
            

    def conectar(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("OnePieceDB.sqlite")

        self.db.open()

        # Deshabilitamos la edición del cuadro de texto del ID
        # self.capitulo_LE.setEnabled(False)
        # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=self.db)
        self.modelo.setTable("capvistos")
        self.modelo.select()
        # Renombramos las cabeceras de la tabla
        self.modelo.setHeaderData(0, Qt.Horizontal, "Capítulo")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Título")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Día")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Personas")
        self.tablaDB.setModel(self.modelo)
        # Ajustamos el tamaño de las columnas al contenido
        self.tablaDB.resizeColumnsToContents()
        self.tablaDB.isFullScreen()
        # Deshabilitamos la edición directa de la tabla
        self.tablaDB.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Establecemos que se seleccionen filas completas en lugar de celdas individuales
        self.tablaDB.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaDB.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Creamos la señal: Cuando cambie la seleccion, ejecuta self.seleccion
        self.tablaDB.selectionModel().selectionChanged.connect(self.seleccion)
        # Creamos la señal: Cuando se ejecute la acción Modificar, ejecuta self.modificar
        #self.actionModificar.triggered.connect(self.modificar)
        # Creamos la señal: Cuando se ejecute la acción Insertar, ejecuta self.nueva
        #self.actionInsertar.triggered.connect(self.nueva)
        # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
        #self.actionEliminar.triggered.connect(self.borrar)

        # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
        self.fila = -1

    def seleccion(self, seleccion):
        # Recuerda que indexes almacena los índices de la selección
        if seleccion.indexes():
            # Nos quedamos con la fila del primer índice (solo se puede seleccionar una fila)
            self.fila = seleccion.indexes()[0].row()
            # Obtenemos los valores id, titulo y artista del modelo en esa fila
            id = self.modelo.index(self.fila, 0).data()
            titulo = self.modelo.index(self.fila, 1).data()
            dia = self.modelo.index(self.fila, 2).data()
            personas = self.modelo.index(self.fila, 3).data()
            # Modificamos los campos del formulario para establecer esos valores
            self.capitulo_LE.setText(str(id))
            self.titulo_LE.setText(str(titulo))
            self.dia_LE.setText(str(dia))
            self.personas_LE.setText(str(personas))

        else:
            # Si no hay selección,  ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
            self.fila = -1

    def modificar(self):
        # Si es una fila válida la seleccionada
        if self.fila >= 0:
            # Obtenemos los valores de los campos del formulario
            id = self.capitulo_LE.text()
            titulo = self.titulo_LE.text()
            dia = self.dia_LE.text()
            personas = self.personas_LE.text()
            # Actualizamos los campos en el modelo
            self.modelo.setData(self.modelo.index(self.fila, 1), id)
            self.modelo.setData(self.modelo.index(self.fila, 1), titulo)
            self.modelo.setData(self.modelo.index(self.fila, 2), dia)
            self.modelo.setData(self.modelo.index(self.fila, 3), personas)
            # Ejecutamos los cambios en el modelo
            self.modelo.submit()

    def nueva(self):
        # Guardamos en la variable nuevaFila el número de filas del modelo
        nuevaFila = self.modelo.rowCount()
        # Insertamos una nueva fila en el modelo en la posición de ese valor
        self.modelo.insertRow(nuevaFila)
        # Seleccionamos la fila nueva
        self.tablaDB.selectRow(nuevaFila)
        # Ponemos en blanco el texto del título en el formulario
        dia=(datetime.today().strftime("%d/%m/%Y-%H:%M"))
        # Ponemos el comboBox de artistas al primero de la lista
        self.personas_LE.setText("")
        self.titulo_LE.setText("")
        # Establecemos en blanco los valores (título y artista) de esa nueva fila
        self.modelo.setData(self.modelo.index(nuevaFila, 1), "")
        self.modelo.setData(self.modelo.index(nuevaFila, 2), dia)
        self.modelo.setData(self.modelo.index(nuevaFila, 3), "")
        self.modelo.setData(self.modelo.index(nuevaFila, 4), "")
        # Ejecutamos los cambios en el modelo
        self.modelo.submit()

    def borrar(self):
        # Si es una fila válida la seleccionada
        if self.fila >= 0:
            # Borramos la fila en el modelo
            self.modelo.removeRow(self.fila)
            # Actualizamos la tabla
            self.modelo.select()
            # Y ponemos la fila actual a -1
            self.fila = -1
            # Reseteamos los valores en los campos del formulario
            self.capitulo_LE.setText("")
            self.titulo_LE.setText("")
            self.dia_LE.setText("")
            self.personas_LE.setText("")
            


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
