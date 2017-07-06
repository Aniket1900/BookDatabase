from . import warp, unwarp, prolog


class Genre(object):
    def __init__(self, Name):
        self.name = unwarp(Name)

    def Name(self):
        return self.name

    def save(self):
        prolog.assertz("genre({})".format(warp(self.name)))
