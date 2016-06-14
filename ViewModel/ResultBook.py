from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.Books import Books


class ResultListBookWindow(QWidget):
    def __init__(self, books, parent=None):
        super(ResultListBookWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listBookUi.ui', self)
        self.loadBooks(books)

    def loadBooks(self, books):
        model = QStandardItemModel(self.ui.bookListView)

        for book in books:
            item = QStandardItem(book.Title())
            model.appendRow(item)

        self.ui.bookListView.setModel(model)
