from PyQt4 import QtGui
import sys
import subprocess
import os


class App(QtGui.QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__()

        vbox = QtGui.QVBoxLayout(self)

        open_button = QtGui.QPushButton('Abrir Script')
        vbox.addWidget(open_button)
        open_button.clicked.connect(self.run)

    def open_file(self):
        directory = os.path.dirname(__file__)
        extension = '(*.py)'
        self.filename = str(QtGui.QFileDialog.getOpenFileName(self, 'Abrir Script', directory, extension))

    def run(self):
        self.open_file()
        if self.filename:
            comando = ['python', self.filename]
            try:
                subprocess.call(comando)
            except:
                QtGui.QMessageBox.information(self, 'Error!',
                'Error, no se puede ejecutar el script')
        # else:
        #     QtGui.QMessageBox.warning(self, 'Error', 'Debe abrir un archivo')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
