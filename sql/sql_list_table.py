from PyQt5 import QtSql, QtWidgets
import sys

def main():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName('db.sqlite')
    if db.open():
        print 'Conexion con exito!!'
    else:
        print db.lastError().text()
    query = '''CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100));'''
    cursor = QtSql.QSqlQuery()
    cursor.prepare(query)
    if cursor.exec_():
        print 'Tabla creado con exito!'
    else:
        print cursor.lastError().text()

class SqlViewer(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(SqlViewer, self).__init__()
        self.setupUi()
        self.__openDatabase()
        self.__setupStates()

    def setupUi(self):
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        centralWidget = QtWidgets.QWidget(self)
        vbox = QtWidgets.QVBoxLayout(centralWidget)
        self.tableWidget = QtWidgets.QTableWidget()
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.itemClicked.connect(self.on_list_clicked)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.listWidget)
        centralWidget.setLayout(vbox)
        self.setCentralWidget(centralWidget)

    def __openDatabase(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setDatabaseName('test')
        self.db.setHostName("localhost");
        self.db.setUserName("root");
        self.db.setPassword("horacio");
        if self.db.open():
            self.statusBar.showMessage("Conexion con exito!", 3000)
        else:
            QtWidgets.QMessageBox.critical(self, 'Error Fatal!', self.db.lastError().text())
            QtWidgets.qApp.quit()

    def __setupStates(self):
        query = 'SELECT * FROM DEPARTAMENTOS;'
        cursor = QtSql.QSqlQuery()
        cursor.prepare(query)
        self.states = {}
        if cursor.exec_():
            while cursor.next():
                self.states[cursor.value(1)] = "SELECT * FROM LOCALIDADES WHERE ID_DEPARTAMENTO = {} ".format(cursor.value(0))
            self.states['Todos'] = "SELECT * FROM LOCALIDADES;"
            self.listWidget.addItems(self.states.keys())
            self.__prepareTable()
        else:
            QtWidgets.QMessageBox.critical(self, 'Error Fatal!', cursor.lastError().text())

    def __prepareTable(self):
        self.tableWidget.setColumnCount(4)
        headers = ['ID DEPARTAMENTO', 'DEPARTAMENTO', 'ID LOCALIDAD', 'LOCALIDAD']
        self.tableWidget.setHorizontalHeaderLabels(headers)
        # establecer el ancho de las columnas
        for i in range(4):
            self.tableWidget.setColumnWidth(i, 200)
        # desabilitar la edicion de los datos de la Tabla
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # habilitar la seleccion de la linea completa
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

    def __updateTable(self, state):
        query = self.states[state]
        cursor = QtSql.QSqlQuery()
        cursor.prepare(query)
        if cursor.exec_():
            self.tableWidget.setRowCount(0)
            self.statusBar.showMessage('Query executado con exito!', 2500)
            row = 0
            while cursor.next():
                idLocalidad = str(cursor.value(0))
                idDeparamento = str(cursor.value(1))
                nombreLocalidad = str(cursor.value(2))
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(idDeparamento))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(state))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(idLocalidad))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(nombreLocalidad))
                row += 1
        else:
            print cursor.lastError().text()


    def on_list_clicked(self, item):
        self.__updateTable(item.data(0))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SqlViewer()
    window.show()
    sys.exit(app.exec_())
