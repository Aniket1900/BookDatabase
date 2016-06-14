from . import prolog
from .Book import Book
from .Author import Author
from .Genre import Genre


class Books(object):
    def __init__(self):
        self.books = list(prolog.query("book(Title, Year, Rate)"))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if len(self.genres) == 0:
            raise StopIteration()
        else:
            authorsList = list(prolog.query("authors(Name, Surname, {})".
                                            format(self.books['Title'])))
            authors = []
            for authorEntry in authorsList:
                authors.append(Author(**authorEntry))

            genreList = list(prolog.query("genre(Name, {})".
                                          format(self.books['Title'])))
            genres = []
            for genreEntry in genreList:
                genres.append(Genre(**genreEntry))

            return Book(**self.books.pop(0), Authors=authors, Genres=genres)
