# This Python file uses the following encoding: utf-8
import cv2    
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QMessageBox, QTableView
from PySide6.QtGui import QPixmap,  QIntValidator
from datetime import datetime

from ui_main import Ui_MainWindow
import webScraping
from VentanaEmergente import Ventana


class MainWindow(QMainWindow, Ui_MainWindow, Ventana):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lastCap = webScraping.ObtenerUltimoCapitulo().get_last_episode()
        self.currentCap = 0
    
        self.actualizarUltimoCap()

        self.capActual = str(self.currentCap)
        self.porcentaje = self.obtenerPorcentajeYDiferencia(self.currentCap, int(self.lastCap))

        self.actualizarGaleriaCB()
        
        self.fondos_CB.currentIndexChanged.connect(self.cambiarFondo)
        self.subirIMG_label.clicked.connect(self.galeria)
        
        self.action_1_Cap.triggered.connect(self.nueva1)
        self.action_3_Cap.triggered.connect(self.nueva3)
        self.action_5_Cap.triggered.connect(self.nueva5)
        self.action_10_Cap.triggered.connect(self.nueva10)

        self.actionActual_Cap.triggered.connect(self.abrirVentanaExtra)

        self.actionEditar_Cap.triggered.connect(self.modificar)
        self.actionEliminar_Cap.triggered.connect(self.borrar)

        self.mas1_button.clicked.connect(self.nueva1)
        self.mas3_button.clicked.connect(self.nueva3)
        self.mas5_button.clicked.connect(self.nueva5)
        self.mas10_button.clicked.connect(self.nueva10)

        # self.webEngine.load(QUrl("https://www3.animeflv.net/ver/one-piece-tv-100"))

        # self.imgFondo_label.setPixmap(QPixmap("logoOnePiece2.png"))

        self.conectar()

        self.dialog = Ventana(self)

    def actualizarUltimoCap(self):
        self.currentCap = int(self.ObtenerUltimoCapVisto())
        porcentaje = int(self.currentCap*100) / int(self.lastCap)
        rendondeo = round(porcentaje, 2)
        diferencia = int(self.lastCap) - int(self.currentCap)

        self.porcentajeVisto_label.setText(
            ("Porcentaje: " + str(rendondeo)+"%"))
        self.capVistos_label.setText("Capítulos vistos: "+str(self.currentCap))
        self.capTotales_label.setText("Capítulos totales: "+str(self.lastCap))
        if diferencia == 0:
            self.gB_SC.setTitle("Llegaste al último capítulo")
        if diferencia > 0:
            self.gB_SC.setTitle("Faltan "+str(diferencia)+" capítulos")
        # print("Diferencia: " + str(diferencia))
        #if self.capActual.endswith("0"):
            # Si el capítulo actual termina en 0, es porque estamos en el capítulo 10
            #self.gB_SC.setTitle("Otros 10 capítulos fuera")
        #if self.capActual.endswith("00"):
            # Si el capítulo actual termina en 00, es porque estamos en el capítulo 100
            #self.gB_SC.setTitle(
                #"Ya te has ventilado otros 100 capítulos, ya queda menos")
        
        # Hacer los textos sorpresa del Group Box

        ######################################
    def abrirVentanaExtra(self):
        self.dialog.ok_boton.clicked.connect(self.avanzarHastaCapActual)
        self.dialog.cancel_boton.clicked.connect(self.dialog.close)

        self.dialog.show()


    def avanzarHastaCapActual(self):
        self.lastCap2 = webScraping.ObtenerUltimoCapitulo().get_last_episode()
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("OnePieceDB.sqlite")

        self.db.open()
        
        self.currentCap = int(self.ObtenerUltimoCapVisto())

        # integers 1 to 9999
        validator = QIntValidator(1, 9999)

        self.dialog.capInf_LE.setValidator(validator)

        print("Aqui "+self.dialog.capInf_LE.text())

        diferencia = int(self.dialog.capInf_LE.text()) - int(self.currentCap)

        print(diferencia)

        print(self.lastCap2)

        if int(self.dialog.capInf_LE.text()) < int(self.lastCap2):
            if diferencia < int(self.lastCap2):
                if diferencia > 0:
                    for i in range(diferencia):
                        print(i)
                        self.nueva1()
        


        self.db.close()

    
####################################################
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
            # Si el capítulo actual termina en 0, es porque estamos en el capítulo 10
            self.gB_SC.setTitle("Otros 10 capítulos fuera")
        if self.capActual.endswith("00"):
            # Si el capítulo actual termina en 00, es porque estamos en el capítulo 100
            self.gB_SC.setTitle(
                "Ya te has ventilado otros 100 capítulos, ya queda menos")

    def conectar(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("OnePieceDB.sqlite")

        self.db.open()

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
        # self.actionModificar.triggered.connect(self.modificar)
        # Creamos la señal: Cuando se ejecute la acción Insertar, ejecuta self.nueva
        # self.actionInsertar.triggered.connect(self.nueva)
        # Creamos la señal: Cuando se ejecute la acción Eliminar, ejecuta self.borrar
        # self.actionEliminar.triggered.connect(self.borrar)

        # Ponemos la fila inicial a un valor que indica que no está seleccionada ninguna fila
        self.fila = -1

    

    def ObtenerUltimoCapVisto(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("OnePieceDB.sqlite")

        self.db.open()
        # Creamos una query para obtener todos los artistas de la tabla Artist
        self.sql = QSqlQuery("SELECT MAX (id) FROM capvistos", db=self.db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        while self.sql.next():
                     #self.comboBoxDescripcionDB.addItem(self.sql.value(0))
                     #print(self.comboBoxDescripcionDB)
            return(str(self.sql.value(0)))
        

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
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("OnePieceDB.sqlite")
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
            self.db.close()

    def nueva(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("OnePieceDB.sqlite")

        self.db.open()
        # Guardamos en la variable nuevaFila el número de filas del modelo
        nuevaFila = self.modelo.rowCount()
        # Insertamos una nueva fila en el modelo en la posición de ese valor
        self.modelo.insertRow(nuevaFila)
        # Seleccionamos la fila nueva
        self.tablaDB.selectRow(nuevaFila)
        # Ponemos en blanco el texto del título en el formulario
        dia = (datetime.today().strftime("%d/%m/%Y-%H:%M"))
        # Ponemos el comboBox de artistas al primero de la lista
        self.personas_LE.setText("")
        self.titulo_LE.setText("")
        # Establecemos en blanco los valores (título y artista) de esa nueva fila
        self.modelo.setData(self.modelo.index(nuevaFila, 1), "")
        self.modelo.setData(self.modelo.index(nuevaFila, 2), dia)
        self.modelo.setData(self.modelo.index(nuevaFila, 3), "")
        self.modelo.setData(self.modelo.index(nuevaFila, 4), "")

        # Ejecutamos los cambios en el modelo

        #self.capVistos_label.setText("Capítulos Vistos:"+self.ObtenerUltimoCapVisto())


        self.modelo.submit()
        self.db.close()

    def nueva1(self):
        self.nueva()
        self.actualizarUltimoCap()


    def nueva3(self):
        veces = 3
        for i in range(veces):
            self.nueva1()

    def nueva5(self):
        veces = 5
        for i in range(veces):
            self.nueva1()

    def nueva10(self):
        veces = 10
        for i in range(veces):
            self.nueva1()

    def borrar(self):
        
        # Si es una fila válida la seleccionada
        if self.fila >= 0:
            self.db = QSqlDatabase("QSQLITE")
            self.db.setDatabaseName("OnePieceDB.sqlite")
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
            self.db.close()

            self.actualizarUltimoCap()

    def galeria(self):
        #input_images_path = "Imagenes"
        #files_names = os.listdir(input_images_path)
        
        file_filter = "Archivo .png, .jpg, .jpeg (*.png *.jpg *.jpeg);"
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Seleciona una o más imágenes",
            filter=file_filter,
        )
        files_names = response[0]
        


        output_images_path = "Imagenes_Galeria"
        if not os.path.exists(output_images_path):
            os.mkdir(output_images_path)


        for i in files_names:
            image = cv2.imread(i)
            dividirRuta = i.split("/")
            numMaxRuta = len(dividirRuta)
            #print(numMaxRuta)
            nombreArchivo= (dividirRuta[numMaxRuta-1])
            if i is None:
                continue

            cv2.imwrite(output_images_path + "/" + nombreArchivo, image)

        self.actualizarGaleriaCB()

    def actualizarGaleriaCB(self):
        galeria = 'Imagenes_Galeria'
        if not os.path.exists(galeria):
            os.mkdir(galeria)
        listaArchivos = os.listdir(galeria)
        

        for archivo in listaArchivos:
            if archivo.endswith(".jpg"):
                self.fondos_CB.addItem(archivo)
                if archivo is None:
                    continue
            if archivo.endswith(".png"):
                self.fondos_CB.addItem(archivo)
                if archivo is None:
                    continue
            if archivo.endswith(".jpeg"):
                self.fondos_CB.addItem(archivo)
                if archivo is None:
                    continue

    def cambiarFondo(self):
        self.imgFondo_label.setPixmap(QPixmap("Imagenes_Galeria/"+str(self.fondos_CB.currentText())))
        


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
