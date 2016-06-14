from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.Authors import Authors


class ListAuthorWindow(QWidget):
    def __init__(self, parent=None):
        super(ListAuthorWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listAuthorUi.ui', self)
        self.loadAuthors()

    def loadAuthors(self):
        model = QStandardItemModel(self.ui.authorListView)
        authors = Authors()

        for author in authors:
            item = QStandardItem(author.JoinName())
            item.setCheckable(True)
            model.appendRow(item)

        self.ui.authorListView.setModel(model)
