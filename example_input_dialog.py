from PyQt5 import QtWidgets, QtCore
import sys

class Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__()
        self.setupUi()

    def setupUi(self):
        dataGroup = QtWidgets.QGridLayout(self)
        dataGroup.addWidget(QtWidgets.QLabel("Nombre"), 0, 0)
        dataGroup.addWidget(QtWidgets.QLabel("Peso"), 1, 0)
        dataGroup.addWidget(QtWidgets.QLabel("Edad"), 2, 0)
        dataGroup.addWidget(QtWidgets.QLabel("Sexo"), 3, 0)

        self.nameInput = QtWidgets.QLineEdit()
        self.nameInput.setReadOnly(True)
        self.weightInput = QtWidgets.QLineEdit()
        self.weightInput.setReadOnly(True)
        self.ageInput = QtWidgets.QLineEdit()
        self.ageInput.setReadOnly(True)
        self.genderInput = QtWidgets.QLineEdit()
        self.genderInput.setReadOnly(True)

        self.nameButton = QtWidgets.QPushButton("...", self)
        self.nameButton.clicked.connect(self.on_name_clicked)
        self.weightButton = QtWidgets.QPushButton("...", self)
        self.weightButton.clicked.connect(self.on_weight_clicked)
        self.ageButton = QtWidgets.QPushButton("...", self)
        self.ageButton.clicked.connect(self.on_age_clicked)
        self.genderButton = QtWidgets.QPushButton("...", self)
        self.genderButton.clicked.connect(self.on_gender_clicked)

        dataGroup.addWidget(self.nameInput, 0, 1)
        dataGroup.addWidget(self.weightInput, 1, 1)
        dataGroup.addWidget(self.ageInput, 2, 1)
        dataGroup.addWidget(self.genderInput, 3, 1)

        dataGroup.addWidget(self.nameButton, 0, 2)
        dataGroup.addWidget(self.weightButton, 1, 2)
        dataGroup.addWidget(self.ageButton, 2, 2)
        dataGroup.addWidget(self.genderButton, 3, 2)

    def on_name_clicked(self):
        name, ok = QtWidgets.QInputDialog.getText(self, 'Ingresar Nombre',
        'Ingrese nombre del cliente',
        )
        # validar que el usuario haya clickeado en ok y ingresado un nombre
        if ok and name:
            self.nameInput.setText(name)

    def on_weight_clicked(self):
        weight, ok = QtWidgets.QInputDialog.getDouble(self, "Ingresar Peso",
        "Ingresar Peso del cliente", 50)
        if ok:
            self.weightInput.setText(str(weight))

    def on_age_clicked(self):
        age, ok = QtWidgets.QInputDialog.getInt(self, 'Ingresar Edad',
        'Ingrese la edad del cliente')
        if ok:
            self.ageInput.setText(str(age))

    def on_gender_clicked(self):
        items = ['Masculino', 'Femenino']
        gender, ok = QtWidgets.QInputDialog.getItem(self, "Ingresar Sexo",
        'Seleccione el sexo del cliente', items)
        if ok:
            self.genderInput.setText(gender)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        centralWidget = Widget(self)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
