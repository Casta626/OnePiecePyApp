import cv2
import os
from importlib.metadata import SelectableGroups
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QTableView, QPushButton, QDialog, QFormLayout, QLabel, QLineEdit, QDialogButtonBox, QMessageBox
from PySide6.QtGui import (QPixmap)
from datetime import datetime

from ui_main import Ui_MainWindow
import webScraping
from VentanaEmergente import Ventana

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 200
        self.setMinimumSize(self.window_width, self.window_height)

        file_filter = "Archivo .png, .jpg, .jpeg (*.png *.jpg *.jpeg);"
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption="Seleciona una o más imágenes",
            filter=file_filter,
        )
        files_names = response[0]
        


        output_images_path = "Imagenes_Galeria_Prueba"
        if not os.path.exists(output_images_path):
            os.mkdir(output_images_path)


        for i in files_names:
            image = cv2.imread(i)
            dividirRuta = i.split("/")
            numMaxRuta = len(dividirRuta)
            print(numMaxRuta)
            nombreArchivo= (dividirRuta[numMaxRuta-1])
            if i is None:
                continue

            cv2.imwrite(output_images_path + "/" + nombreArchivo, image)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget {font-size: 35px;}")
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')