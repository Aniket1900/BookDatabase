from PyQt5 import QtWidgets, uic
from Models.Author import Author


class AddAuthorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddAuthorWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/addAuthorUi.ui', self)
        self.ui.addAuthorButton.clicked.connect(self.newAuthor)

    def newAuthor(self):
        name = self.ui.lineEditNameAuthor.text()
        surname = self.ui.lineEditSurnameAuthor.text()
        author = Author(name, surname)
        author.save()
        self.close()
