import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(800, 600)
        self.setWindowTitle('Pyqt')

        grid = QtGui.QGridLayout(self)

        btn_1 = QtGui.QPushButton('1', self)
        btn_2 = QtGui.QPushButton('2', self)
        btn_3 = QtGui.QPushButton('3', self)
        btn_4 = QtGui.QPushButton('4', self)
        btn_5 = QtGui.QPushButton('5', self)
        btn_6 = QtGui.QPushButton('6', self)
        btn_7 = QtGui.QPushButton('Salir', self)

        # forma Pythonica
        btn_1.clicked.connect(self.on_click)
        btn_2.clicked.connect(self.on_click)
        btn_7.clicked.connect(self.close)
        # estilo c++
        self.connect(btn_3, QtCore.SIGNAL('clicked()'), self.on_click)

        grid.addWidget(btn_1, 0, 0)
        grid.addWidget(btn_2, 0, 1)
        grid.addWidget(btn_3, 1, 0)
        grid.addWidget(btn_4, 1, 1)
        grid.addWidget(btn_5, 2, 0)
        grid.addWidget(btn_6, 2, 1)
        grid.addWidget(btn_7, 3, 0, 1, 2)

    def on_click(self):
        print 'clicked'

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
