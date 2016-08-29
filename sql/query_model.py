from PyQt5 import QtSql, QtWidgets
import sys

class Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__()
        self.setupUi()
        self.__openDatabase()

    def setupUi(self):
        vbox = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel()
        self.tableView = QtWidgets.QTableView(self)
        vbox.addWidget(self.tableView)
        vbox.addWidget(self.label)

    def __openDatabase(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setDatabaseName('test')
        self.db.setHostName("localhost");
        self.db.setUserName("root");
        self.db.setPassword("horacio");
        if self.db.open():
            self.__setupTable()
            self.label.setText("Conexion con exito!")
        else:
            QtWidgets.QMessageBox.critical(self, 'Error Fatal!', self.db.lastError().text())
            QtWidgets.qApp.quit()


    def __setupTable(self):
        model = QtSql.QSqlQueryModel(self)
        model.setQuery("SELECT * FROM DEPARTAMENTOS;")
        self.tableView.setModel(model)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())
