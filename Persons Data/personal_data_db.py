# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtSql, QtCore
import sys

class Table(QtWidgets.QWidget):

    def __init__(self, parent=None , db=None):
        super(Table, self).__init__()
        self.setupUi()
        self.db = db
        self.__connectDatabase()

    def setupUi(self):
        hbox = QtWidgets.QHBoxLayout()
        self.newButton = QtWidgets.QPushButton("Nuevo", self)
        deleteButton = QtWidgets.QPushButton("Eliminar", self)
        hbox.addWidget(self.newButton)
        hbox.addWidget(deleteButton)
        vbox = QtWidgets.QVBoxLayout(self)
        self.table = QtWidgets.QTableWidget(self)
        self.__setupTable()
        vbox.addWidget(self.table)
        vbox.addLayout(hbox)

    def __setupTable(self):
        self.table.setColumnCount(4)
        headers = ['ID', 'NOMBRE', 'EMAIL', 'FECHA CUMPLEAÑO']
        self.table.setColumnWidth(3, 200)
        self.table.setHorizontalHeaderLabels(headers)

    def __connectDatabase(self):
        if self.db.open():
            self.cursor = QtSql.QSqlQuery(self.db)
            query = 'SELECT * FROM Persons;'
            if self.cursor.exec_(query):
                self.__fillTable()
            self.db.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error {} !!".format(self.db.lastError().text()))

    def __fillTable(self):
        row = 0
        while self.cursor.next():
            self.table.insertRow(row)
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(self.cursor.value(0))))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.cursor.value(1))))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.cursor.value(2))))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.cursor.value(3))))
            row += 1


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.sqlite3')
        self.setupUi()

    def setupUi(self):
        # configure MainWindow
        self.setFixedSize(800, 600)
        menubar = QtWidgets.QMenuBar(self)
        fileMenu = QtWidgets.QMenu("Archivo", self)
        newAction = QtWidgets.QAction("Nuevo", self)
        newAction.triggered.connect(self.on_new_triggered)
        fileMenu.addAction(newAction)
        menubar.addMenu(fileMenu)
        self.setMenuBar(menubar)

        centralWidget = Table(self, self.db)
        centralWidget.newButton.clicked.connect(self.on_new_triggered)
        self.setCentralWidget(centralWidget)


    def on_new_triggered(self):
        dialog = NewDialog(self, self.db)
        dialog.exec_()


class NewDialog(QtWidgets.QDialog):

    def __init__(self, parent=None, db=None):
        super(NewDialog, self).__init__()
        self.setupUi()
        self.db = db
        self.__connectDatabase()

    def setupUi(self):
        # configure centralWidget
        grid = QtWidgets.QGridLayout()
        grid.addWidget(QtWidgets.QLabel("Nombre"), 0, 0)
        grid.addWidget(QtWidgets.QLabel("Email"), 1, 0)
        grid.addWidget(QtWidgets.QLabel("Fecha de cumpleaños"), 2, 0)

        self.saveButton = QtWidgets.QPushButton('Guardar', self)
        self.saveButton.clicked.connect(self.on_save_clicked)
        newButton = QtWidgets.QPushButton('Nuevo', self)
        newButton.clicked.connect(self.on_new_clicked)
        cancelButton = QtWidgets.QPushButton('Cancelar', self)
        cancelButton.clicked.connect(self.on_cancel_clicked)

        self.nameInput = QtWidgets.QLineEdit()
        self.nameInput.textEdited.connect(self.saveButton.show)
        self.emailInput = QtWidgets.QLineEdit()
        self.emailInput.textEdited.connect(self.saveButton.show)
        self.birthDateInput = QtWidgets.QDateEdit()
        self.birthDateInput.setCalendarPopup(True)
        self.birthDateInput.setDisplayFormat("yyyy/MM/dd")
        self.birthDateInput.editingFinished.connect(self.saveButton.show)

        previousButton = QtWidgets.QPushButton("Previo", self)
        previousButton.clicked.connect(self.on_previous_clicked)
        previousButton.clicked.connect(self.saveButton.hide)
        nextButton = QtWidgets.QPushButton("Siguiente", self)
        nextButton.clicked.connect(self.on_next_clicked)
        nextButton.clicked.connect(self.saveButton.hide)

        grid.addWidget(self.nameInput, 0, 1)
        grid.addWidget(self.emailInput, 1, 1)
        grid.addWidget(self.birthDateInput, 2, 1)
        grid.addWidget(previousButton, 3, 0)
        grid.addWidget(nextButton, 3, 1)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(newButton)
        vbox.addWidget(self.saveButton)
        vbox.addWidget(cancelButton)
        vbox.addStretch()

        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addLayout(grid)
        hbox.addLayout(vbox)


    # connect to the database
    def __connectDatabase(self):
        if self.db.open():
            self.cursor = QtSql.QSqlQuery(self.db)
            query = 'SELECT name, email, birthDate FROM Persons;'
            self.cursor.exec_(query)
            if self.cursor.isActive():
                self.cursor.first()
                self.__fillForm()
            # self.parent.statusBar.showMessage("Conexion con exito!!", 3000)
            self.saveButton.hide()
            self.newRecord = False
        else:
            QtWidgets.QMessageBox.warning(self, "Error {} !!".format(self.db.lastError().text()))
            # self.parent.statusBar.showMessage("Error {} !!".format(self.db.lastError().text()), 3000)
            self.reject()


    def __fillForm(self):
        self.nameInput.setText(self.cursor.value(0))
        self.emailInput.setText(self.cursor.value(1))
        date = self.cursor.value(2).split('-')
        y = int(date[0])
        m = int(date[1])
        d = int(date[2])
        self.birthDateInput.setDate(QtCore.QDate(y, m, d))

    def on_previous_clicked(self):
        if not self.cursor.previous():
            self.cursor.last()
        self.__fillForm()

    def on_next_clicked(self):
        if not self.cursor.next():
            self.cursor.first()
        self.__fillForm()

    def on_save_clicked(self):
        name = str(self.nameInput.text())
        if name.strip() == '':
            self.statusBar.showMessage('El nombre no esta completo', 3000)
            self.nameInput.setFocus()
            return
        if not self.newRecord:
            updateCursor = QtSql.QSqlQuery(self.db)
            updateCursor.prepare("UPDATE Persons SET name = :name, email = :email, birthDate = :date ")
            updateCursor.bindValue(':name', name)
            updateCursor.bindValue(':email', self.emailInput.text())
            updateCursor.bindValue(':date', self.birthDateInput.date())
            if updateCursor.exec_():
                # self.statusBar.showMessage('Registro actualizado!', 3000)
                QtWidgets.QMessageBox.information(self, 'Exito', 'Registro actualizado')
            else:
                QtWidgets.QMessageBox.critical(self, 'Exito', 'Error, {}'.format(updateCursor.lastError().text()))
                # self.statusBar.showMessage('Error, {}'.format(updateCursor.lastError().text()), 3000)
        else:
            updateCursor = QtSql.QSqlQuery(self.db)
            updateCursor.prepare("INSERT INTO Persons (name, email, birthDate) VALUES (:name, :email, :date);")
            updateCursor.bindValue(':name', self.nameInput.text())
            updateCursor.bindValue(':email', self.emailInput.text())
            updateCursor.bindValue(':date', self.birthDateInput.date())
            if updateCursor.exec_():
                QtWidgets.QMessageBox.information(self, 'Exito', 'Registro guardado')
                # self.statusBar.showMessage('Registro Guardado!', 3000)
            else:
                # self.statusBar.showMessage('Error, {}'.format(updateCursor.lastError().text()), 3000)
                QtWidgets.QMessageBox.critical(self, 'Error', 'Registro no actualizado')

    def on_new_clicked(self):
        self.nameInput.clear()
        self.emailInput.clear()
        self.newRecord = True

    def on_cancel_clicked(self):
        self.reject()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
