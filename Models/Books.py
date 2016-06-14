from . import prolog, warp
from .Book import Book
from .Author import Author
from .Genre import Genre


class Books(object):
    def __init__(self):
        self.books = list(prolog.query("book(Title, Year, Mark)"))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.books) == 0:
            raise StopIteration()
        else:
            authorsList = list(prolog.query("author(Name, Surname, {})".
                                            format(warp(self.books[0]["Title"]))))
            authors = []
            for authorEntry in authorsList:
                authors.append(Author(**authorEntry))

            genreList = list(prolog.query("genre(Name, {})".
                                          format(warp(self.books[0]["Title"]))))
            genres = []
            for genreEntry in genreList:
                genres.append(Genre(**genreEntry))

            return Book(**self.books.pop(0), Authors=authors, Genres=genres)
