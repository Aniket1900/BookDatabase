from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel
from Models.PrologObjects import Genres


class ListGenreWindow(QWidget):
    def __init__(self, parent=None):
        super(ListGenreWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/listGenreUi.ui', self)
        self.loadGenres()

    def loadGenres(self):
        model = QStandardItemModel(self.ui.genreListView)
        genres = Genres()

        for genre in genres:
            genre.setCheckable(True)
            model.appendRow(genre)

        self.ui.genreListView.setModel(model)
