from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.PrologObjects import Authors


class ListAuthorWindow(QWidget):
    def __init__(self, parent=None):
        super(ListAuthorWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listAuthorUi.ui', self)
        self.model = QStandardItemModel(self.ui.authorListView)
        self.loadAuthors()

    def loadAuthors(self):
        authors = Authors()
        for author in authors:
            item = QStandardItem()
            item.setText(author.JoinName())
            self.model.appendRow(item)
