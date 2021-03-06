from fractions import Fraction

__author__ = 'yben_000'


class ConjunctionTolerance(object):
    def __init__(self, length, epsilon):
        self.length = length

    def get_tolerance(self, *args):
        return Fraction(2**(-2*self.length - 1))
