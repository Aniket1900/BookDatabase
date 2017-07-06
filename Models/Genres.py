from . import prolog
from .Genre import Genre


class Genres(object):
    def __init__(self):
        self.genres = list(prolog.query("genre(Name)"))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.genres) == 0:
            raise StopIteration()
        else:
            return Genre(**self.genres.pop(0))
