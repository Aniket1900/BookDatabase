from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.Authors import Authors
from Models.Author import Author
from Models.Books import Books
from .ResultBook import ResultListBookWindow


class ListAuthorWindow(QWidget):
    def __init__(self, parent=None):
        super(ListAuthorWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listAuthorUi.ui', self)
        self.ui.authorBookButton.clicked.connect(self.authorBook)
        self.loadAuthors()

    def loadAuthors(self):
        self.authorModel = QStandardItemModel(self.ui.authorListView)
        authors = Authors()

        for author in authors:
            item = QStandardItem(author.JoinName())
            item.setCheckable(True)
            self.authorModel.appendRow(item)

        self.ui.authorListView.setModel(self.authorModel)

    def authorBook(self):
        for i in range(0, self.authorModel.rowCount()):
            item = self.authorModel.item(i)
            if item.checkState():
                books = Books(1, (Author(*item.text().split(" "))))
                form = ResultListBookWindow(books)
                form.show()
