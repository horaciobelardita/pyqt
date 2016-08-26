from PyQt4 import QtGui
import sys, os


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800, 600)
        # widgets
        self.table = QtGui.QTableWidget(self)
        process_button = QtGui.QPushButton('Procesar', self)
        # layout
        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(QtGui.QLabel("TABLA DE BANCOS"))
        vbox.addWidget(self.table)
        vbox.addWidget(process_button)
        self.setLayout(vbox)
        # prepara las columnas para la tabla
        self.__prepare_table()
        # conexion
        process_button.clicked.connect(self.process)

    def __create_matrix(self, rows, columns):
        '''Retorna un matriz de rows x columns de 2 dimensiones'''
        m = []
        for i in range(rows):
            m.append([0] * columns)
        return m

    def __upload_banks(self):
        '''Retorna los bancos en una matriz leidos desde el
        archivo maestro de bancos'''
        directory = os.path.dirname(__file__)
        extensions = '(*.txt)'
        filename = QtGui.QFileDialog.getOpenFileName(self, directory, extensions)
        if filename:
            with open(filename, 'r') as f:
                # lectura de la cantidad de registros de BANCOS
                # creacion de la matriz
                lines = f.readlines()
                rows = len(lines)
                matriz = self.__create_matrix(rows, 2)
                f.seek(0, 0)
                line = f.readline()
                cr = 0
                # procesamiento del archivo de BANCOS
                # y carga en la matriz
                while line != '':
                    record = line.split(',')
                    matriz[cr][0] = record[0]
                    matriz[cr][1] = record[1]
                    cr += 1
                    line = f.readline()
            return matriz

    def __sort(self, matrix):
        '''Retorna la matriz ordenada por descripcion en orden alfabetico'''
        rows = len(matrix)
        columns = len(matrix[0])
        i = 0
        while i < rows:
            j = i
            while j < rows:
                if matrix[i][1] > matrix[j][1]:
                    aux = matrix[i][1]
                    aux_1 = matrix[i][0]
                    matrix[i][1] = matrix[j][1]
                    matrix[i][0] = matrix[j][0]
                    matrix[j][1] = aux
                    matrix[j][0] = aux_1
                j += 1
            i += 1
        return matrix

    def process(self):
        matriz = self.__upload_banks()
        matriz = self.__sort(matriz)
        rows = len(matriz)
        columns = len(matriz[0])
        for i in range(rows):
            self.table.insertRow(self.table.rowCount())
            for j in range(columns):
                self.table.setItem(i, j, QtGui.QTableWidgetItem(matriz[i][j]))


    def __prepare_table(self):
        # establezco el numero de columnas para la tabla
        self.table.setColumnCount(2)
        # agregar los encabezados de columnas
        headers = ['Codigo', 'Descripcion']
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
