from PyQt4 import QtGui
import sys
import os

class App(QtGui.QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__()

        self.combo = QtGui.QComboBox()
        lista = ['item1', 'item2', 'item3']
        for item in lista:
            self.combo.addItem(item)
        self.line_edit = QtGui.QLineEdit()
        self.label_combo = QtGui.QLabel("")
        self.label_line = QtGui.QLabel("")

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.combo)
        vbox.addWidget(self.line_edit)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.label_combo)
        hbox.addWidget(self.label_line)
        vbox.addLayout(hbox)

        self.combo.currentIndexChanged.connect(
            lambda: self.label_combo.setText(self.combo.currentText())
        )
        self.line_edit.textChanged.connect(self.slot_2)

    def slot_1(self):
        self.label_combo.setText(self.combo.currentText())

    def slot_2(self):
        self.label_line.setText(self.line_edit.text())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
