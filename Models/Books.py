from . import prolog
from .Book import Book


class Books(object):
    def __init__(self):
        self.books = list(prolog.query("book(Title)"))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.genres) == 0:
            raise StopIteration()
        else:
            return Book(**self.genres.pop(0))
