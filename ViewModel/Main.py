from PyQt5 import QtWidgets, uic
from .AddAuthor import AddAuthorWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/Main.ui', self)

        self.ui.addAuthorButton.clicked.connect(self.addAuthor)

    def addAuthor(self):
        self.authorWindow = AddAuthorWindow()
        self.authorWindow.show()
