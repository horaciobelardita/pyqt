import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Saludar')

        vbox = QtGui.QVBoxLayout(self)

        button = QtGui.QPushButton('Saludar', self)
        button.clicked.connect(self.greeting)

        close_button = QtGui.QPushButton('Salir', self)
        close_button.clicked.connect(self.close)

        self.label = QtGui.QLabel("")
        self.label.hide()

        vbox.addWidget(button)
        vbox.addWidget(close_button)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def greeting(self):
        self.label.setText('<h1>Hola Mundo!!!</h1>')
        self.label.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
