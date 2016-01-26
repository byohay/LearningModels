from random import choice
from conjunction import Conjunction

__author__ = 'yben_000'


class MonotoneConjunction(Conjunction):
    def __init__(self, n):
        self.n = n
        self.ideal_function = tuple([choice([0, 1]) for _ in xrange(self.n)])

