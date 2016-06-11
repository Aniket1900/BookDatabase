from PyQt5 import QtWidgets, uic


class AddAuthorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddAuthorWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/addAuthorUi.ui', self)
