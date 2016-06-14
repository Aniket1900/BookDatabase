from pyswip import Prolog

prolog = Prolog()


def unwarp(str):
    return str.rstrip("'")


def warp(str):
    return "'"+str+"'"
