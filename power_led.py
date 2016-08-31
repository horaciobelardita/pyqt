from PyQt5 import QtWidgets, QtSerialPort
import serial
import sys


class PowerDialog(QtWidgets.QDialog):

    def __init__(self, parent, port):
        super(PowerDialog, self).__init__(parent)
        self.arduino = serial.Serial()
        self.arduino.port = port
        self.arduino.baudrate = 9600
        self.arduino.open()
        self.setupUi()


    def setupUi(self):
        power_button = QtWidgets.QPushButton('ENCENDER', self)
        off_button = QtWidgets.QPushButton('APAGAR', self)
        power_button.clicked.connect(self.on_power_clicked)
        off_button.clicked.connect(self.on_off_clicked)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(power_button)
        vbox.addWidget(off_button)


    def on_power_clicked(self):
        self.arduino.write('h')

    def on_off_clicked(self):
        self.arduino.write('l')

    def __del__(self):
        if self.arduino.is_open:
            self.arduino.close()



class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Control de encendido')
        self.setupUi()
        self.__get_information()

    def __get_information(self):
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            if port.hasVendorIdentifier() and port.hasProductIdentifier():
                self.listWidget.addItem(port.systemLocation())

    def setupUi(self):
        vbox = QtWidgets.QVBoxLayout(self)
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.itemClicked.connect(self.on_list_clicked)
        self.connectButton = QtWidgets.QPushButton("Conectar", self)
        self.connectButton.setEnabled(False)
        self.connectButton.clicked.connect(self.on_connect_clicked)
        vbox.addWidget(self.listWidget)
        vbox.addWidget(self.connectButton)

    def on_connect_clicked(self):
        dialog = PowerDialog(self, self.portName)
        dialog.exec_()

    def on_list_clicked(self, item):
        self.portName = item.data(0)
        self.connectButton.setEnabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())