from PyQt5 import QtWidgets, uic
from Models.PrologObjects import Authors


class AddAuthorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddAuthorWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listAuthorUi.ui', self)
        self.model = QtWidgets.QStandardItemModel(self.ui.authorListView)
        self.loadAuthors()

    def loadAuthors(self):
        authors = Authors()
        for author in authors:
            pass
