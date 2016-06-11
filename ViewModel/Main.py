from PyQt5 import QtCore, QtWidgets, uic

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        uic.loadUi('Views/Main.ui', self)
