from PyQt4 import QtGui
import sys
import os

class App(QtGui.QDialog):

    def __init__(self, parent=None):
        super(App, self).__init__()
        self.setWindowTitle('Contador de lineas')
        self.lines = 0
        vbox = QtGui.QVBoxLayout(self)

        open_button = QtGui.QPushButton('Abrir Archivo', self)
        open_button.clicked.connect(self.dialog)
        self.label = QtGui.QLabel("")
        self.label.hide()
        vbox.addWidget(open_button)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def open_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.lines += 1
            self.show_lines(self.lines)

    def show_lines(self, lines):
        self.label.setText(str(lines))
        self.label.show()

    def dialog(self):
        directory = os.path.dirname(__file__)
        extensions = '(*.txt)'
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Archivo', directory, extensions)
        if filename:
            self.open_file(filename)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
