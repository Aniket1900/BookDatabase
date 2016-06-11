from pyswip import Prolog

prolog = Prolog()


class Book(object):
    def __init__(self):
        pass


class Author(object):
    def __init__(self, X, Y):
        self.name = X
        self.surname = Y

    def Name(self):
        return self.name

    def Surname(self):
        return self.surname

    def JoinName(self):
        return ' '.join([self.name, self.surname])

    def save(self):
        print(self.name, ' ', self.surname)
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
        if len(self.authors) == 0:
            raise StopIteration()
        else:
            print(self.authors[0])
            return Author(**self.authors.pop(0))
