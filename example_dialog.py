# Simple Aplicacion que segun la hora del sistema y
# un string ingresado recibe un saludo

from PyQt5 import QtWidgets, QtCore
import sys

class Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__()
        self.setupUi()
        self.rejected.connect(QtWidgets.qApp.quit)

    def setupUi(self):
        grid = QtWidgets.QGridLayout(self)
        buttonGroup = QtWidgets.QHBoxLayout()
        okButton = QtWidgets.QPushButton('Ok', self)
        okButton.clicked.connect(self.on_ok_clicked)
        cancelButton = QtWidgets.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.on_cancel_clicked)
        buttonGroup.addStretch()
        buttonGroup.addWidget(okButton)
        buttonGroup.addWidget(cancelButton)
        self.userInput = QtWidgets.QLineEdit()
        self.userInput.placeholderText = "Inserte su nombre de usuario"
        grid.addWidget(self.userInput, 0, 0, 1, 2)
        grid.addLayout(buttonGroup, 1, 0, 1, 2)

    def on_cancel_clicked(self):
        self.reject()

    def on_ok_clicked(self):
        user = self.userInput.text()
        if user != 'admin':
            QtWidgets.QMessageBox.warning(self, 'Error!', '<font color=red>Usuario no valido!')
        else:
            QtWidgets.QMessageBox.about(self, 'Error!', '<font color=green>Usuario valido!')
            self.accept()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        dialog = Dialog(self)
        dialog.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
