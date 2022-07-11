# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QLineEdit, QComboBox
from datetime import datetime

from prueba import Ui_MainWindow
import webScraping
import DB


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lastCap = webScraping.ObtenerUltimoCapitulo().get_last_episode()
        self.currentCap = 400
        self.capActual = str(self.currentCap)
        print(self.lastCap)
        self.porcentaje = self.obtenerPorcentajeYDiferencia(
            self.currentCap, int(self.lastCap))
        self.conectar()
        # self.database = DB.DB()
        # self.database.conectar()
        self.imagenFondo = "gear5.jpg"
        # self.capVistos_label.setText("Capítulos vistos: "+str(self.currentCap))
        # self.capTotales_label.setText("Capítulos totales: "+str(self.lastCap))

    def obtenerPorcentajeYDiferencia(self, currentCap, lastCap):
        porcentaje = (currentCap*100) / lastCap
        rendondeo = round(porcentaje, 2)
        diferencia = lastCap - currentCap

        self.porcentajeVisto_label.setText(
            ("Porcentaje: " + str(rendondeo)+"%"))
        self.capVistos_label.setText("Capítulos vistos: "+str(currentCap))
        self.capTotales_label.setText("Capítulos totales: "+str(lastCap))

        if diferencia == 0:
            print("Llegaste al último capítulo")
        if diferencia > 0:
            print("Faltan "+str(diferencia)+" capítulos")
        # print("Diferencia: " + str(diferencia))
        if self.capActual.endswith("00"):
            print("Ya te has ventilado otros 100 capítulos, ya queda menos")

    def conectar(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("onepi.sqlite")

        self.db.open()

        # Deshabilitamos la edición del cuadro de texto del ID
        # self.capitulo_LE.setEnabled(False)
        # Creamos un modelo relacional de SQL
        self.modelo = QSqlRelationalTableModel(db=self.db)
        self.modelo.setTable("capvistos")
        self.modelo.select()
        # Renombramos las cabeceras de la tabla
        self.modelo.setHeaderData(0, Qt.Horizontal, "Capítulo")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Día")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Personas")
        self.tablaDB.setModel(self.modelo)
        # Ajustamos el tamaño de las columnas al contenido
        self.tablaDB.resizeColumnsToContents()
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
            dia = self.modelo.index(self.fila, 1).data()
            personas = self.modelo.index(self.fila, 2).data()
            # Modificamos los campos del formulario para establecer esos valores
            self.capitulo_LE.setText(str(id))
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
            producto = self.dia_LE.text()
            precio = self.personas_LE.text()
            # Actualizamos los campos en el modelo
            self.modelo.setData(self.modelo.index(self.fila, 1), id)
            self.modelo.setData(self.modelo.index(self.fila, 2), producto)
            self.modelo.setData(self.modelo.index(self.fila, 3), precio)
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
        self.dia_LE.setText(datetime.today().strftime("%d/%m/%Y"))
        # Ponemos el comboBox de artistas al primero de la lista
        self.personas_LE.setText("")
        # Establecemos en blanco los valores (título y artista) de esa nueva fila
        self.modelo.setData(self.modelo.index(nuevaFila, 1), "")
        self.modelo.setData(self.modelo.index(nuevaFila, 2), "")
        self.modelo.setData(self.modelo.index(nuevaFila, 3), "")
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
            self.dia_LE.setText("")
            self.personas_LE.setText("")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
