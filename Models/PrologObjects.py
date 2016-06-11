from pyswip import Prolog

prolog = Prolog()


def unwarp(str):
    return str.rstrip("'")


def warp(str):
    return "'"+str+"'"


class Book(object):
    def __init__(self, Name):
        self.name = Name


class Author(object):
    def __init__(self, Name, Surname):
        self.name = unwarp(Name)
        self.surname = unwarp(Surname)

    def Name(self):
        return self.name

    def Surname(self):
        return self.surname

    def JoinName(self):
        return ' '.join([self.name, self.surname])

    def save(self):
        prolog.assertz("author({},{})".format(warp(self.name), warp(self.
                                                                    surname)))


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
