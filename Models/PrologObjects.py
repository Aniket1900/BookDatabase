from pyswip import Prolog

prolog = Prolog()


class Book(object):
    def __init__(self):
        pass


class Author(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def save(self):
        prolog.assertz("author({},{})".format(self.name, self.surname))
        pass


class Authors(object):
    def __init__(self):
        self.authors = list(prolog.query("author(X,Y)"))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.authors.lengt == 0:
            raise StopIteration()
        else:
            return Author(*self.authors.popleft())
