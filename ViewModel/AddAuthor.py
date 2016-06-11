from PyQt5 import QtCore, QtWidgets, uic

class AddAuthorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddAuthorWindow, self).__init__(parent=parent)
        uic.loadUi('Views/addAuthorUi.ui', self)
