from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.PrologObjects import Authors


class AddBookWindow(QWidget):
    def __init__(self, parent=None):
        super(AddBookWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/addBookUi.ui', self)
        self.loadAuthors()

    def loadAuthors(self):
        model = QStandardItemModel(self.ui.authorListView)
        authors = Authors()

        for author in authors:
            item = QStandardItem(author.JoinName())
            item.setCheckable(True)
            model.appendRow(item)

        self.ui.authorListView.setModel(model)
