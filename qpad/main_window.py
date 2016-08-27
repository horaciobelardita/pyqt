import sys, os
from PyQt4 import QtGui, Qt
from status_bar import StatusBar
from editor import TextEdit

ROOT_FOLDER = os.path.dirname(__file__)
ICONS_FOLDER = os.path.join(ROOT_FOLDER, 'icons')


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800, 600)
        self.setWindowTitle("QPad")
        # central widget
        self.text = TextEdit()
        self.text.cursorPositionChanged.connect(self.update_statusbar)
        self.setCentralWidget(self.text)
        # Actions
        self.__create_actions()
        # Menu
        self.__create_menu(self.menuBar())
        # Toolbar
        self.__create_toolbar(QtGui.QToolBar())
        # Status Bar
        self.status = StatusBar()
        self.setStatusBar(self.status)

    def __create_menu(self, menu):
        # menus
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu('Edit')
        menu_file.addAction(self.new_action)
        menu_file.addAction(self.open_action)
        menu_file.addSeparator()
        menu_file.addAction(self.save_action)
        menu_file.addAction(self.save_as_action)
        menu_file.addSeparator()
        menu_file.addAction(self.exit_action)
        menu_edit.addAction(self.cut_action)
        menu_edit.addAction(self.copy_action)
        menu_edit.addAction(self.paste_action)
        menu_edit.addSeparator()
        menu_edit.addAction(self.undo_action)

    def __create_actions(self):
        # actions
        self.new_action = QtGui.QAction('New', self)
        self.new_action.setShortcut('Ctrl+N')
        self.new_action.setStatusTip('New File')
        self.new_action.triggered.connect(self.new)
        self.new_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'new.png')))
        self.new_action.setShortcut('Ctrl+N')

        self.save_action = QtGui.QAction('Save', self)
        self.save_action.setStatusTip('Save File')
        self.save_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'save.png')))
        self.save_action.triggered.connect(self.save)
        self.save_action.setShortcut('Ctrl+S')

        self.save_as_action = QtGui.QAction('Save As', self)
        self.save_as_action.setStatusTip('Save as file')
        self.save_as_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'save.png')))
        self.save_as_action.triggered.connect(self.save_as)

        self.exit_action = QtGui.QAction('Quit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('close the application')
        self.exit_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'exit.png')))
        self.exit_action.triggered.connect(self.close)

        self.open_action = QtGui.QAction('Open', self)
        self.open_action.setStatusTip('Open File')
        self.open_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'open.png')))
        self.open_action.triggered.connect(self.open)
        self.open_action.setShortcut('Ctrl+O')

        self.cut_action = QtGui.QAction('Cut', self)
        self.cut_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'cut.png')))
        self.cut_action.setShortcut('Ctrl+X')

        self.copy_action = QtGui.QAction('Copy', self)
        self.copy_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'copy.png')))
        self.copy_action.triggered.connect(self.copy)
        self.copy_action.setShortcut('Ctrl+C')

        self.paste_action = QtGui.QAction('Paste', self)
        self.paste_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'paste.png')))
        self.paste_action.setToolTip('Paste')
        self.paste_action.setShortcut('Ctrl+V')

        self.undo_action = QtGui.QAction('Undo', self)
        self.undo_action.setIcon(QtGui.QIcon(os.path.join(ICONS_FOLDER, 'undo.png')))
        self.undo_action.setShortcut('Ctrl+Z')

    def __create_toolbar(self, toolbar):
        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.save_as_action)
        toolbar.addAction(self.copy_action)
        toolbar.addAction(self.paste_action)
        toolbar.addSeparator()
        toolbar.addAction(self.undo_action)
        toolbar.addSeparator()
        toolbar.addAction(self.exit_action)
        self.addToolBar(toolbar)

    def update_statusbar(self):
        line = self.text.textCursor().blockNumber() + 1
        column = self.text.textCursor().columnNumber()
        self.status.update_label(line, column)

    def new(self):
        self.text.setPlainText("")

    def open(self):
        _file = QtGui.QFileDialog.getOpenFileName(self, "Open a file")
        if _file:
            self.filename = _file
            with open(_file, 'r') as f:
                content = f.read()
            self.text.setPlainText(content)
            self.text.is_new = False
            self.text.filename = _file

    def copy(self):
        self.text.copy()

    def paste(self):
        self.text.paste()

    def cut(self):
        self.text.cut()

    def undo(self):
        self.text.undo()

    def save(self):
        if self.text.is_new:
            self.save_as()
        else:
            content = self.text.toPlainText()
            with open(self.text.filename, 'w') as f:
                f.write(content)

    def save_as(self):
        _file = QtGui.QFileDialog.getSaveFileName()
        if _file:
            self.text.filename = _file
            self.text.is_new = False
            self.save()

    def closeEvent(self, event):
        if self.text.is_new:
            flags = QtGui.QMessageBox.Yes
            flags |= QtGui.QMessageBox.No
            flags |= QtGui.QMessageBox.Cancel
            r = QtGui.QMessageBox.information(self, 'Modificado!',
                                        'Desea guardar los cambios antes de salir',
                                         flags)
        if r == QtGui.QMessageBox.Yes:
            self.save()
        elif r == QtGui.QMessageBox.No:
            event.accept()
        else:
            event.ignore()
