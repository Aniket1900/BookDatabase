from PyQt5 import QtWidgets, uic
from .AddAuthor import AddAuthorWindow
from .ListAuthor import ListAuthorWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/Main.ui', self)

        self.ui.addAuthorButton.clicked.connect(self.addAuthor)
        self.ui.authorListButton.clicked.connect(self.listAuthor)

    def addAuthor(self):
        authorWindow = AddAuthorWindow()
        authorWindow.show()

    def listAuthor(self):
        listWindow = ListAuthorWindow()
        listWindow.show()
