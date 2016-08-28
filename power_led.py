from PyQt5 import QtWidgets, QtSerialPort
import sys

class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Control de encendido')
        self.setFixedSize(300, 300)
        self.arduino = QtSerialPort.QSerialPort()
        self.arduino_available = False
        self.__get_information()
        self.__setup_arduino()
        self.setupUi()

    def __get_information(self):
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            if port.hasVendorIdentifier() and port.hasProductIdentifier():
                self.port_name = port.portName()
                self.arduino_available = True

    def __setup_arduino(self):
        # abrir y configurar el serialport
        if self.arduino_available:
            self.arduino.setPortName(self.port_name)
            if self.arduino.open(QtCore.QIODevice.WriteOnly):
                self.arduino.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
            else:
                # dar un mensaje de error
                QtWidgets.QMessageBox.warning(self, 'Error!', "Error: {}".format(self.arduino.error()))
        else:
            QtWidgets.QMessageBox.warning(self, 'Error!', "Conecte su Arduino")
            sys.exit()

    def setupUi(self):
        power_button = QtWidgets.QPushButton('ENCENDER', self)
        off_button = QtWidgets.QPushButton('APAGAR', self)
        power_button.clicked.connect(self.on_power_clicked)
        off_button.clicked.connect(self.on_off_clicked)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(power_button)
        vbox.addWidget(off_button)


    def on_power_clicked(self):
        if self.arduino.isWritable():
            self.arduino.write("1")

    def on_off_clicked(self):
        if self.arduino.isWritable():
            self.arduino.write("0")

    def __del__(self):
        if self.arduino.isOpen():
            self.arduino.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
