from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
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
            item = QStandardItem(genre.Name())
            item.setCheckable(True)
            model.appendRow(item)

        self.ui.genreListView.setModel(model)
