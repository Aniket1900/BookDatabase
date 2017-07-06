from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Models.Book import Book
from Models.Author import Author
from Models.Genre import Genre
from Models.Authors import Authors
from Models.Genres import Genres


class AddBookWindow(QWidget):
    def __init__(self, parent=None):
        super(AddBookWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/addBookUi.ui', self)
        self.ui.addBookButton.clicked.connect(self.addBook)
        self.loadAuthors()
        self.loadGenres()

    def loadAuthors(self):
        self.authorModel = QStandardItemModel(self.ui.authorListView)
        authors = Authors()

        for author in authors:
            item = QStandardItem(author.JoinName())
            item.setCheckable(True)
            self.authorModel.appendRow(item)

        self.ui.authorListView.setModel(self.authorModel)

    def loadGenres(self):
        self.genreModel = QStandardItemModel(self.ui.genreListView)
        genres = Genres()

        for genre in genres:
            item = QStandardItem(genre.Name())
            item.setCheckable(True)
            self.genreModel.appendRow(item)

        self.ui.genreListView.setModel(self.genreModel)

    def addBook(self):
        authors = []
        genres = []

        for i in range(0, self.authorModel.rowCount()):
            item = self.authorModel.item(i)
            if item.checkState():
                authors.append(Author(*item.text().split(" ")))

        for i in range(0, self.genreModel.rowCount()):
            item = self.genreModel.item(i)
            if item.checkState():
                genres.append(Genre(item.text()))

        title = self.ui.bookTitleLineEdit.text()
        year = self.ui.yearSpinBox.value()
        mark = self.ui.markSpinBox.value()
        book = Book(title, year, mark, authors, genres)
        book.save()
        self.close()
