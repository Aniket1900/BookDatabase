from PyQt5 import QtWidgets, uic
from .AddAuthor import AddAuthorWindow
from .AddBook import AddBookWindow
from .ListAuthor import ListAuthorWindow
from .AddGenre import AddGenreWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/Main.ui', self)

        self.ui.addAuthorButton.clicked.connect(self.addAuthor)
        self.ui.addBookButton.clicked.connect(self.addBook)
        self.ui.authorListButton.clicked.connect(self.listAuthor)
        self.ui.addGenreButton.clicked.connect(self.addGenre)

    def addAuthor(self):
        authorWindow = AddAuthorWindow()
        authorWindow.show()

    def listAuthor(self):
        listWindow = ListAuthorWindow()
        listWindow.show()

    def addBook(self):
        bookWindow = AddBookWindow()
        bookWindow.show()

    def addGenre(self):
        genreWindow = AddGenreWindow()
        genreWindow.show()
