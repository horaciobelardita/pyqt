# Simple Aplicacion que segun la hora del sistema y
# un string ingresado recibe un saludo

from PyQt5 import QtWidgets, QtCore
import sys

class MainWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        # self.setFixedSize(self.geometry().width(), self.geometry().height())
        self.setFixedSize(600, 300)
        buttonGroup = QtWidgets.QGridLayout()
        btn1 = QtWidgets.QPushButton('+', self)
        btn1.clicked.connect(self.on_btn1_clicked)
        btn2 = QtWidgets.QPushButton('-', self)
        btn2.clicked.connect(self.on_btn2_clicked)
        btn3 = QtWidgets.QPushButton('*', self)
        btn3.clicked.connect(self.on_btn3_clicked)
        btn4 = QtWidgets.QPushButton('/', self)
        btn4.clicked.connect(self.on_btn4_clicked)

        buttonGroup.addWidget(btn1, 0, 0)
        buttonGroup.addWidget(btn2, 0, 1)
        buttonGroup.addWidget(btn3, 1, 0)
        buttonGroup.addWidget(btn4, 1, 1)

        self.numberOne = QtWidgets.QLineEdit()
        self.numberTwo = QtWidgets.QLineEdit()
        self.resultLabel = QtWidgets.QLabel("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        grid = QtWidgets.QGridLayout(self)
        grid.addWidget(self.numberOne, 0, 0)
        grid.addWidget(self.numberTwo, 0, 1)
        grid.addLayout(buttonGroup, 1, 0)
        grid.addWidget(self.resultLabel, 1, 1)

    def on_btn1_clicked(self):
        # boton de suma
        result = float(self.numberOne.text()) + float(self.numberTwo.text())
        self.resultLabel.setText(str(result))

    def on_btn2_clicked(self):
        # boton de resta
        result = float(self.numberOne.text()) - float(self.numberTwo.text())
        self.resultLabel.setText(str(result))

    def on_btn3_clicked(self):
        # boton de multiplicacion
        result = float(self.numberOne.text()) * float(self.numberTwo.text())
        self.resultLabel.setText(str(result))

    def on_btn4_clicked(self):
        # boton de division
        numberTwo = float(self.numberTwo.text())
        if numberTwo == 0:
            QtWidgets.QMessageBox.critical(self, 'Error', '<font color=red>Error division por 0',
            QtWidgets.QMessageBox.Cancel)
            self.numberTwo.setFocus()
            return
        result = float(self.numberOne.text()) / numberTwo
        self.resultLabel.setText(str(result))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
