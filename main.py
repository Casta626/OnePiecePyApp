# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


from prueba import Ui_MainWindow
import webScraping
import DB





class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        lastCap = webScraping.ObtenerUltimoCapitulo().get_last_episode()
        currentCap = 334
        print(lastCap)
        self.obtenerPorcentajeYDiferencia(currentCap,int(lastCap))
        self.database = DB.DB()
        self.database.conectar()

    def obtenerPorcentajeYDiferencia(self,currentCap,lastCap):
        porcentaje = (currentCap*100) / lastCap 
        rendondeo = round(porcentaje, 2)
        diferencia = lastCap - currentCap

        print("Porcentaje: " + str(rendondeo)+"%")
        print("Diferencia: " + str(diferencia))
        return rendondeo,diferencia

           
            






if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()