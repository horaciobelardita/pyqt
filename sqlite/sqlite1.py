from PySide import QtGui, QtSql, QtCore
import sys

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.__create_database()
        self.__create_table_users()
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumSize(800, 600)
        self.name_input = QtGui.QLineEdit()
        self.surname_input = QtGui.QLineEdit()
        self.age_input = QtGui.QLineEdit()
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel("Nombre"), 0, 0)
        grid.addWidget(self.name_input, 0, 1)
        grid.addWidget(QtGui.QLabel("Apellido"), 1, 0)
        grid.addWidget(self.surname_input, 1, 1)
        grid.addWidget(QtGui.QLabel("Edad"), 2, 0)
        grid.addWidget(self.age_input, 2, 1)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        btn = QtGui.QPushButton('Agregar Usuario', self)
        btn.clicked.connect(self.__insert_user)
        self.dataGrid = QtGui.QTableWidget()
        self.__prepare_table()
        vbox.addWidget(btn)
        vbox.addWidget(self.dataGrid)
        show_btn = QtGui.QPushButton('Mostrar', self)
        show_btn.clicked.connect(self.__show_data)
        vbox.addWidget(show_btn)
        self.setLayout(vbox)

    def __prepare_table(self):
        self.dataGrid.setColumnCount(3)
        headers = ['Nombre', 'Apellido', 'Edad']
        self.dataGrid.setHorizontalHeaderLabels(headers)
        self.dataGrid.verticalHeaderVisible = False

    def __insert_user(self):
        query = '''INSERT INTO users
        (name,surname,age) VALUES (:id, :surname, :age)'''
        cursor = QtSql.QSqlQuery()
        cursor.prepare(query)
        cursor.bindValue(":id", self.name_input.text())
        cursor.bindValue(":surname", self.surname_input.text())
        cursor.bindValue(":age", self.age_input.text())
        if cursor.exec_():
            QtGui.QMessageBox.information(self, 'Exito!!', 'Usuario creado con exito!')
        else:
            print 'No se ha podido insertar el usuario'

    def __show_data(self):
        query = "SELECT * FROM users"
        cursor = QtSql.QSqlQuery()
        cursor.prepare(query)
        if cursor.exec_():
            self.dataGrid.setRowCount(0)
            while cursor.next():
                name = cursor.value(1)
                surname = cursor.value(2)
                age = cursor.value(3)
                self.dataGrid.insertRow(self.dataGrid.rowCount())
                name_item = QtGui.QTableWidgetItem(str(name))
                name_item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.dataGrid.setItem(self.dataGrid.rowCount() - 1, 0, name_item)
                surname_item = QtGui.QTableWidgetItem(str(surname))
                surname_item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.dataGrid.setItem(self.dataGrid.rowCount() - 1, 1, surname_item)
                age_item = QtGui.QTableWidgetItem(str(age))
                age_item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.dataGrid.setItem(self.dataGrid.rowCount() - 1, 2, age_item)


    def __create_table_users(self):
        query = '''CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100),
        surname VARCHAR(100),
        age INTEGER NOT NULL)'''
        consult = QtSql.QSqlQuery()
        consult.prepare(query)
        if consult.exec_():
            print 'Tabla creada con exito'
        else:
            print 'No se ha creado la tabla'

    def __create_database(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('db.sqlite')
        if self.db.open():
            print "Base de Datos creada con exito"
        else:
            print "Error en la conexion"



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
