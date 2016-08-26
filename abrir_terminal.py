from PyQt4 import QtGui
import sys
from subprocess import Popen


class App(QtGui.QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__()

        vbox = QtGui.QVBoxLayout(self)

        self.combo = QtGui.QComboBox()
        btn = QtGui.QPushButton('Run!')
        terminales = [
            'xterm',
            'gnome-terminal',
            'lxterminal',
            'terminator'
        ]
        for terminal in terminales:
            self.combo.addItem(terminal)

        vbox.addWidget(self.combo)
        vbox.addWidget(btn)

        btn.clicked.connect(self.run)

    def run(self):
        comando = str(self.combo.currentText())
        try:
            Popen(comando)
        except:
            QtGui.QMessageBox.information(self, 'Error!',
            '{} no esta instalado'.format(comando))
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
