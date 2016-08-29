from PyQt5 import QtSql, QtWidgets
import sys

class Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__()
        self.setupUi()
        self.__openDatabase()

    def setupUi(self):
        hbox = QtWidgets.QHBoxLayout(self)
        inputGroup = QtWidgets.QGridLayout()
        inputGroup.addWidget(QtWidgets.QLabel("DEPARTAMENTO"), 0, 0)
        self.userInput = QtWidgets.QLineEdit()
        inputGroup.addWidget(self.userInput, 0, 1)
        insertButton = QtWidgets.QPushButton("INSERTAR", self)
        insertButton.clicked.connect(self.on_insert_clicked)
        inputGroup.addWidget(insertButton, 1, 0, 1, 2)
        vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.tableView = QtWidgets.QTableView(self)
        vbox.addWidget(self.tableView)
        vbox.addWidget(self.label)
        hbox.addLayout(vbox)
        hbox.addLayout(inputGroup)

    def __openDatabase(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setDatabaseName('test')
        self.db.setHostName("localhost");
        self.db.setUserName("root");
        self.db.setPassword("horacio");
        if not self.db.open():
            QtWidgets.QMessageBox.critical(self, 'Error Fatal!', self.db.lastError().text())
            QtWidgets.qApp.quit()
            # self.__setupTable()
        else:
            model = QtSql.QSqlTableModel(self, self.db)
            model.setTable("DEPARTAMENTOS")
            self.tableView.setModel(model)
            # selecciona los datos y muestra en la tabla
            model.select()
            self.label.setText("Conexion con exito!")

    def on_insert_clicked(self):
        state = self.userInput.text()
        if not state:
            QtWidgets.QMessageBox.warning(self, "Atencion", "Datos invalidos")
        else:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO DEPARTAMENTOS (NOMBRE_DEPARTAMENTO) VALUES (?);")
            query.bindValue(0, state)
            if query.exec_():
                QtWidgets.QMessageBox.information(self, 'Suceso', 'Departamento agregado con exito!')
                self.userInput.setText("")
                # actualizar los datos de la tabla
                self.tableView.model().select()
            else:
                QtWidgets.QMessageBox.warning(self, 'Error', 'No se ha podido agregar, error: {}'.format(query.lastError().text()))



    def __setupTable(self):
        model = QtSql.QSqlQueryModel(self)
        model.setQuery("SELECT * FROM DEPARTAMENTOS;")
        self.tableView.setModel(model)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())
