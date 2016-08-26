from PyQt4 import QtGui
import sys, os


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        # etiqueta y boton para archivo vendedores
        sellers_button = QtGui.QPushButton('Archivo Vendedores', self)
        sellers_button.clicked.connect(self.__ask_sellers_file)
        self.sellers_label = QtGui.QCheckBox("Falta archivo vendedores")
        self.sellers_label.setCheckState(True)
        self.sellers_label.stateChanged.connect(self.__check)
        # etiqueta y boton para archivo novedades
        news_button = QtGui.QPushButton('Archivo Novedades', self)
        news_button.clicked.connect(self.__ask_news_file)
        self.news_label = QtGui.QCheckBox("Falta archivo novedad")
        self.news_label.setCheckState(True)
        self.news_label.stateChanged.connect(self.__check)
        # tabla
        self.table = QtGui.QTableWidget()
        self.table.hide()
        # creo el boton procesar y lo desabilito
        self.process_button = QtGui.QPushButton("Procesar", self)
        self.process_button.setEnabled(False)
        self.process_button.clicked.connect(self.__process_file)
        # layouts
        grid = QtGui.QGridLayout()
        grid.addWidget(sellers_button, 0, 0)
        grid.addWidget(self.sellers_label, 0, 1)
        grid.addWidget(news_button, 1, 0)
        grid.addWidget(self.news_label, 1, 1)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addLayout(grid)
        vbox.addWidget(self.table)
        vbox.addWidget(self.process_button)


    def __check(self):
        if not self.sellers_label.checkState() and  not self.news_label.checkState():
            self.process_button.setEnabled(True)

    def __ask_news_file(self):
        directory = os.path.dirname(__file__)
        extension = '(*.txt)'
        self.news_file = QtGui.QFileDialog.getOpenFileName(self, directory, extension)
        if self.news_file:
            self.news_label.setCheckState(False)

    def __upload_sellers(self):
        sellers = {}
        with open(self.sellers_file) as f:
            line = f.readline()
            while line != '':
                record = line.split(',')
                # dict[cod_vendedor] = nombre_apellido
                sellers[int(record[0])] = record[1]
                line = f.readline()
        return sellers

    def __create_matriz(self, rows, columns):
        m = []
        for i in range(rows):
            m.append([0] * columns)
        return m

    def __process_file(self):
        self.__prepare_table()
        self.sellers = self.__upload_sellers()
        rows = len(self.sellers) + 1
        columns = 6
        matriz = self.__create_matriz(rows, columns)
        with open(self.news_file, 'r') as f:
            line = f.readline()
            while line != '':
                record = line.split(',')
                # codigo de sucursal
                cod_suc = int(record[0])
                # codigo de vendedor
                cod_v = int(record[1])
                # importe
                imp = float(record[4])
                # cantidad
                cant = int(record[5])
                # acumular los importes en la matriz
                matriz[cod_v-1][cod_suc-1] += imp * cant
                matriz[rows-1][cod_suc-1] += imp * cant
                matriz[cod_v-1][5] += imp * cant
                line = f.readline()
        for cod, name in self.sellers.items():
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(cod-1, 0, QtGui.QTableWidgetItem(str(cod)))
            self.table.setItem(cod-1, 1, QtGui.QTableWidgetItem(name))
            self.table.setItem(cod-1, 2, QtGui.QTableWidgetItem(str(matriz[cod-1][0])))
            self.table.setItem(cod-1, 3, QtGui.QTableWidgetItem(str(matriz[cod-1][1])))
            self.table.setItem(cod-1, 4, QtGui.QTableWidgetItem(str(matriz[cod-1][2])))
            self.table.setItem(cod-1, 5, QtGui.QTableWidgetItem(str(matriz[cod-1][3])))
            self.table.setItem(cod-1, 6, QtGui.QTableWidgetItem(str(matriz[cod-1][4])))
            self.table.setItem(cod-1, 7, QtGui.QTableWidgetItem(str(matriz[cod-1][5])))
        self.table.show()
        self.setGeometry(0, 0, 1024, 768)

    def __ask_sellers_file(self):
        directory = os.path.dirname(__file__)
        extension = '(*.txt)'
        self.sellers_file = QtGui.QFileDialog.getOpenFileName(self, directory, extension)
        if self.sellers_file:
            self.sellers_label.setCheckState(False)

    def __prepare_table(self):
        self.table.setColumnCount(8)
        headers = [
            'COD. VENDEDOR',
            'NOMBRE Y APELLIDO',
            '1',
            '2',
            '3',
            '4',
            '5',
            'TOTAL'
            ]
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 300)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
