from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel
from Models.PrologObjects import Books


class ListGenreWindow(QWidget):
    def __init__(self, parent=None):
        super(ListBookWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listBookUi.ui', self)
        self.loadGenres()

    def loadBooks(self):
        model = QStandardItemModel(self.ui.bookListView)
        books = Books()

        for book in books:
            book.setCheckable(True)
            model.appendRow(genre)

        self.ui.bookListView.setModel(model)
