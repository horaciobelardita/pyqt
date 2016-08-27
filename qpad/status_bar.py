from PyQt4.QtGui import QStatusBar, QLabel

class StatusBar(QStatusBar):

    def __init__(self):
        super(StatusBar, self).__init__()
        self.pos_cursor = "Linea: %s Columna: %s"
        self.line_column = QLabel(self.pos_cursor % (1, 0))
        self.addWidget(self.line_column)

    def update_label(self, line, column):
        self.line_column.setText(self.pos_cursor % (line, column))
