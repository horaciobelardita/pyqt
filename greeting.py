# Simple Aplicacion que segun la hora del sistema y
# un string ingresado recibe un saludo

from PyQt5 import QtWidgets, QtCore
import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(QtWidgets.QLabel("Ingrese su nombre"))
        self.userInput = QtWidgets.QLineEdit()
        okButton = QtWidgets.QPushButton('Ok', centralWidget)
        okButton.clicked.connect(self.on_ok_clicked)
        hbox.addWidget(self.userInput)
        hbox.addWidget(okButton)
        centralWidget.setLayout(hbox)

    def on_ok_clicked(self):
        name = self.userInput.text()
        if not name:
            return
        hs = QtCore.QTime.currentTime().hour()
        if hs < 12:
            QtWidgets.QMessageBox.about(self, 'Hola', 'Buen dia, {}'.format(name))
        elif hs > 12 and hs < 17:
            QtWidgets.QMessageBox.about(self, 'Hola', 'Buenas Tardes, {}'.format(name))
        else:
            QtWidgets.QMessageBox.about(self, 'Hola', 'Buenas noches, {}'.format(name))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
