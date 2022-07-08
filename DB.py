from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView,QLineEdit,QComboBox

from prueba import Ui_MainWindow
class DB(Ui_MainWindow):

    def __init__(self):
        super().__init__()

    def lanzarDB(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("onepi.sqlite")

        self.db.open()
        print("exito")