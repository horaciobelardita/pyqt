from PyQt5 import QtSerialPort, QtCore, QtWidgets
import sys

ARDUINO_VENDOR_ID = '' # port.vendorIdentifier()

ARDUINO_PRODUCT_ID = '' # port.productIdentifier()

class Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__()
        self.setupUi()
        self.arduino = QtSerialPort.QSerialPort()
        self.arduino_available = False
        # self.__get_information()
        self.__configure()

    def __configure(self):
        # abrir y configurar el serialport
        # if self.arduino_available:
        self.arduino.setPortName('ttyACM0')
        if self.arduino.open(QtCore.QIODevice.WriteOnly):
            self.arduino.setBaudRate(QtSerialPort.QSerialPort.Baud9600)
        else:
        # dar un mensaje de error
            QtWidgets.QMessageBox.warning(self, 'Error!', str(self.arduino.error()))

    def __get_information(self):
        # averiguar el vendor and product id
        # print 'numero de puertos {}'.format(len(QtSerialPort.QSerialPortInfo.availablePorts()))
        # for port in QtSerialPort.QSerialPortInfo.availablePorts():
        #     if port.hasVendorIdentifier():
        #         print port.vendorIdentifier()
        #     if port.hasProductIdentifier():
        #         print port.productIdentifier()
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            print port.portName()
            if port.hasVendorIdentifier() and port.hasProductIdentifier():
                if port.vendorIdentifier() == ARDUINO_VENDOR_ID:
                    if port.productIdentifier() == ARDUINO_PRODUCT_ID:
                        self.port_name = port.portName()
                        self.arduino_available = True

    def setupUi(self):
        self.setFixedSize(560, 160)
        self.setWindowTitle('Controlador LED')
        grid = QtWidgets.QGridLayout(self)

        self.red_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.red_slider.valueChanged.connect(self.on_red_changed)
        self.green_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.green_slider.valueChanged.connect(self.on_green_changed)
        self.blue_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.blue_slider.valueChanged.connect(self.on_blue_changed)

        self.red_slider.setRange(0, 255)
        self.green_slider.setRange(0, 255)
        self.blue_slider.setRange(0, 255)

        self.red_label = QtWidgets.QLabel("0")
        self.green_label = QtWidgets.QLabel("0")
        self.blue_label = QtWidgets.QLabel("0")

        red = '''<h2 style="color:red;">LED ROJO</h2>'''
        grid.addWidget(QtWidgets.QLabel(red), 0, 0)
        grid.addWidget(self.red_slider, 0, 1)
        grid.addWidget(self.red_label, 0, 2)
        green = '''<h2 style="color:green;">LED VERDE</h2>'''
        grid.addWidget(QtWidgets.QLabel(green), 1, 0)
        grid.addWidget(self.green_slider, 1, 1)
        grid.addWidget(self.green_label, 1, 2)
        blue = '''<h2 style="color:blue;">LED AZUL</h2>'''
        grid.addWidget(QtWidgets.QLabel(blue), 2, 0)
        grid.addWidget(self.blue_slider, 2, 1)
        grid.addWidget(self.blue_label, 2, 2)
        self.setLayout(grid)

    def on_red_changed(self, value):
        self.red_label.setText(str(value))
        self.update_rgb('r' + str(value))

    def on_blue_changed(self, value):
        self.blue_label.setText(str(value))
        self.update_rgb('b' + str(value))

    def on_green_changed(self, value):
        self.green_label.setText(str(value))
        self.update_rgb('g' + str(value))

    def update_rgb(self, command):
        if self.arduino.isWritable():
            self.arduino.write(command)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error!', 'No se puede escribir al puerto serial')


    def __del__(self):
        if self.arduino.isOpen():
            self.arduino.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
