from pyswip import Prolog

prolog = Prolog()


class Book():
    def __init__(self):
        pass


class Author():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        prolog.assertz("author({},{})".format(name, surname))

    def save(self):
        pass
