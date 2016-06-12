from PyQt5 import QtWidgets, uic
from Models.PrologObjects import Genre


class AddGenreWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddGenreWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/addGenreUi.ui', self)
        self.ui.addGenreButton.clicked.connect(self.newGenre)

    def newAuthor(self):
        name = self.ui.lineEditNameGenre.text()
        genre = Genre(name)
        genre.save()
        self.close()
