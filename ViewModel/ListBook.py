from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.Books import Books


class ListBookWindow(QWidget):
    def __init__(self, parent=None):
        super(ListBookWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listBookUi.ui', self)
        self.loadBooks()

    def loadBooks(self):
        model = QStandardItemModel(self.ui.bookListView)
        books = Books()

        for book in books:
            item = QStandardItem(book.Title())
            item.setCheckable(True)
            model.appendRow(item)

        self.ui.bookListView.setModel(model)
