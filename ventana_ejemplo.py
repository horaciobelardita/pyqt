import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(800, 600)
        self.setWindowTitle('Pyqt')
        # botones
        button = QtGui.QPushButton('Cerrar', self)
        button.clicked.connect(QtGui.qApp.quit)
        button1 = QtGui.QPushButton('OK', self)

        line_edit = QtGui.QLineEdit()

        other_button = QtGui.QPushButton('Otro boton', self)
        other = QtGui.QPushButton('Otro', self)
        line_edit2 = QtGui.QLineEdit()
        # labels
        label = QtGui.QLabel("<h3>Etiqueta</h3>", self)
        # layouts
        hbox = QtGui.QHBoxLayout(self)
        hbox.addWidget(button)
        hbox.addWidget(button1)
        hbox.addWidget(label)
        hbox.addWidget(line_edit)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(other_button)
        vbox.addWidget(other)
        vbox.addWidget(line_edit2)

        hbox.addLayout(vbox)

        

        self.setLayout(hbox)

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
