from pyswip import Prolog

prolog = Prolog()
prolog.assertz("author('Juliusz', 'Verne')")
prolog.assertz("genre('przygodowa')")
prolog.assertz("book('Tajemicza wyspa', 1874, 8)")
prolog.assertz("genre('przygodowa', 'Tajemnicza wyspa')")
prolog.assertz("author('Juliusz', 'Werne', 'Tajemicza wyspa')")
prolog.query("author(Name, Surname, Title, Year, Rank) :- "
             "author(Name, Surname, Title), book(Title, Year, Rank).")


def unwarp(str):
    return str.rstrip("'")


def warp(str):
    return "'"+str+"'"
