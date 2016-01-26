from evolvability.classic_model.neighborhood import Neighborhood

__author__ = 'yben_000'


class MonotoneConjunctionNeighborhood(Neighborhood):
    def __init__(self):
        pass

    def get_neighborhood_of_rep(self, rep):
        return self.get_rep_plus_and_rep_minus(rep) | self.get_rep_plus_minus(rep)

    def get_rep_plus_minus(self, rep):
        return set()

    def get_rep_plus_and_rep_minus(self, rep):
        rep_plus_and_rep_minus = set()
        rep_plus_and_rep_minus.add(tuple(rep))

        rep = list(rep)

        for i in xrange(len(rep)):
            rep_plus_and_rep_minus.add(tuple(rep[:i] + [1 - rep[i]] + rep[i+1:]))

        return rep_plus_and_rep_minus
