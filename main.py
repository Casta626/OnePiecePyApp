# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QLineEdit, QComboBox

from prueba import Ui_MainWindow
import webScraping
import DB





class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lastCap = webScraping.ObtenerUltimoCapitulo().get_last_episode()
        self.currentCap = 400
        self.capActual = str(self.currentCap)
        print(self.lastCap)
        self.porcentaje = self.obtenerPorcentajeYDiferencia(self.currentCap,int(self.lastCap))
        self.conectar()
        #self.database = DB.DB()
        #self.database.conectar()
        self.imagenFondo = "gear5.jpg"
        #self.capVistos_label.setText("Capítulos vistos: "+str(self.currentCap))
        #self.capTotales_label.setText("Capítulos totales: "+str(self.lastCap))

    def obtenerPorcentajeYDiferencia(self,currentCap,lastCap):
        porcentaje = (currentCap*100) / lastCap 
        rendondeo = round(porcentaje, 2)
        diferencia = lastCap - currentCap

        self.porcentajeVisto_label.setText(("Porcentaje: " + str(rendondeo)+"%"))
        self.capVistos_label.setText("Capítulos vistos: "+str(currentCap))
        self.capTotales_label.setText("Capítulos totales: "+str(lastCap))

        if diferencia == 0:
            print("Llegaste al último capítulo")
        if diferencia > 0:
            print("Faltan "+str(diferencia)+" capítulos")
        #print("Diferencia: " + str(diferencia))
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
        self.tablaDB.setModel(self.modelo)
        # Ajustamos el tamaño de las columnas al contenido
        self.tablaDB.resizeColumnsToContents()

        print("exito")
           
            






if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()