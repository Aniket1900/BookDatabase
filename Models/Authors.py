from . import prolog
from .Author import Author


class Authors(object):
    def __init__(self):
        self.authors = list(prolog.query("author(Name,Surname)"))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.authors) == 0:
            raise StopIteration()
        else:
            return Author(**self.authors.pop(0))
