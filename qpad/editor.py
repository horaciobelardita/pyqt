from PyQt4.QtGui import QTextEdit

class TextEdit(QTextEdit):

    def __init__(self):
        super(TextEdit, self).__init__()
        self.is_new = True
        self.filename = 'new_file'
