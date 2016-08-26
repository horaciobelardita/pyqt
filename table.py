from PyQt4 import QtGui
import sys, os, random

ROOT_FOLDER = os.path.dirname(__file__)
ICONS_FOLDER = os.path.join(ROOT_FOLDER, 'icons')


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800, 600)

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout(self)

        self.table = QtGui.QTableWidget(self)

        button = QtGui.QPushButton('Preparar Tabla', self)
        button.clicked.connect(self.prepare)

        insert_button = QtGui.QPushButton('Insertar Registro', self)
        insert_button.clicked.connect(self.insert)

        btn1 = QtGui.QPushButton('Eliminar primera fila', self)
        btn1.clicked.connect(self.delete_first)
        btn2 = QtGui.QPushButton('Eliminar ultima fila', self)
        btn2.clicked.connect(self.delete_last)
        btn3 = QtGui.QPushButton('Eliminar fila actual', self)
        btn3.clicked.connect(self.delete_current)
        btn4 = QtGui.QPushButton('Borrar todo', self)
        btn4.clicked.connect(self.delete_all)
        self.line_name = QtGui.QLineEdit()
        self.line_surname = QtGui.QLineEdit()
        self.line_age = QtGui.QLineEdit()
        self.line_class = QtGui.QLineEdit()
        btn5 = QtGui.QPushButton('Modificar', self)
        btn5.clicked.connect(self.modify)

        self.table.itemClicked.connect(self.item_clicked)

        vbox.addWidget(button)
        vbox.addWidget(insert_button)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(self.line_name)
        vbox.addWidget(self.line_surname)
        vbox.addWidget(self.line_age)
        vbox.addWidget(self.line_class)
        vbox.addWidget(btn5)

        hbox.addWidget(self.table)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

    def delete_first(self):
        self.table.removeRow(0)

    def delete_last(self):
        self.table.removeRow(self.table.rowCount() - 1)

    def delete_current(self):
        self.table.removeRow(self.f)

    def item_clicked(self, item):
        # obtener la fila actual
        self.f = item.row()
        # obtener los datos de la fila actual
        name = self.table.item(self.f, 0)
        surname = self.table.item(self.f, 1)
        age = self.table.item(self.f, 2)
        clase = self.table.item(self.f, 3)

        # setear los line edit
        self.line_name.setText(name.text())
        self.line_surname.setText(surname.text())
        self.line_age.setText(age.text())
        self.line_class.setText(clase.text())

    def modify(self):
        self.table.setItem(self.f, 0, QtGui.QTableWidgetItem(self.line_name.text()))
        self.table.setItem(self.f, 1, QtGui.QTableWidgetItem(self.line_surname.text()))
        self.table.setItem(self.f, 2, QtGui.QTableWidgetItem(self.line_age.text()))
        self.table.setItem(self.f, 3, QtGui.QTableWidgetItem(self.line_class.text()))

    def delete_all(self):
        self.table.setRowCount(0)

    def prepare(self):
        self.table.setColumnCount(4)
        headers = ['Nombre', 'Apellido', 'Edad', 'Clase']
        # agregar los encabezados de columnas
        self.table.setHorizontalHeaderLabels(headers)
        # setear el ancho de las columnas
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 180)
        self.table.setColumnWidth(2, 50)
        self.table.setColumnWidth(3, 70)

    def insert(self):
        # inserta un registro nuevo al final de la tabla
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QtGui.QTableWidgetItem("{}".format(random.randint(1, 100))))
        self.table.setItem(self.table.rowCount() - 1, 1, QtGui.QTableWidgetItem("{}".format(random.randint(1, 100))))
        self.table.setItem(self.table.rowCount() - 1, 2, QtGui.QTableWidgetItem("{}".format(random.randint(1, 100))))
        self.table.setItem(self.table.rowCount() - 1, 3, QtGui.QTableWidgetItem("{}".format(random.randint(1, 100))))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
