from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import (QRect)
class Ventana(QDialog):

    def __init__(self, *args, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        self.setWindowTitle("Ventana emergente")
        self.setFixedSize(400, 200)
        self.cancel_boton = QPushButton(self)
        self.cancel_boton.setText("Cancelar")
        self.cancel_boton.setGeometry(QRect(225, 100, 100, 30))
        self.ok_boton = QPushButton(self)
        self.ok_boton.setText("Enviar")
        self.ok_boton.setGeometry(QRect(75, 100, 100, 30))

        self.capInf_LE = QLineEdit(self)
        self.capInf_LE.setGeometry(QRect(50, 50, 300, 20))
        self.capInf_LE.setPlaceholderText("Ingrese el último capítulo que vió") 

        self.setStyleSheet("QLineEdit { background-color: white; border: 2px solid black; }" "\n"
                            "QPushButton {\n"
" font: 20pt \"Ink Free\";\n"
" border: 1px solid black;\n"
" border-radius: 5px ;\n"
" background-color: rgb(255, 255, 135);\n"
"}\n"
"QDialog {\n"
" background-color: deepskyblue;\n"
"}\n")

if __name__ == "__main__":  
    app = QApplication([])
    dialog = Ventana()
    dialog.show()
    app.exec()