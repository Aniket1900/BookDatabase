from . import warp, unwarp, prolog


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
