from PyQt4 import QtGui
import sys, os

ROOT_FOLDER = os.path.dirname(__file__)
ICONS_FOLDER = os.path.join(ROOT_FOLDER, 'icons')


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setMinimumSize(400, 300)
        # QAction Salir
        self.exit_action = QtGui.QAction('Salir', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Salir de la Aplicacion')
        self.exit_action.triggered.connect(self.close)
        self.exit_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'exit.png')))
        # QAction nuevo
        self.new_action = QtGui.QAction('Nuevo', self)
        self.new_action.setShortcut('Ctrl+N')
        self.new_action.setStatusTip('Nuevo Archivo')
        self.new_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'new.png')))
        # central widget
        widget = QtGui.QTextEdit()
        self.setCentralWidget(widget)

        # barra de herramientas
        self.toolbar = QtGui.QToolBar(self)
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(self.exit_action)
        self.addToolBar(self.toolbar)
        # barra de estado
        self.setStatusBar(QtGui.QStatusBar())
        # menu
        menu = self.menuBar()
        file_menu = menu.addMenu('Archivo')
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.exit_action)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
