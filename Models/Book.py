from . import warp, unwarp, prolog


class Book(object):
    def __init__(self, Author, Title, Genres):
        self.author = Author
        self.title = unwarp(Title)
        self.genres = Genres

    def Title(self):
        return self.title

    def save(self):
        pass
