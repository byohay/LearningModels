from itertools import izip
import distance

from LearningModels.evolvability.classic_model.neighborhood import Neighborhood

__author__ = 'yben_000'


class MonotoneConjunctionNeighborhood(Neighborhood):
    def __init__(self):
        pass

    def get_neighborhood_of_rep(self, rep):
        return self.get_rep_plus_and_rep_minus(rep) | self.get_rep_plus_minus(rep)

    def get_rep_plus_minus(self, rep):
        rep_plus_minus = set()
        rep = list(rep)

        rep_plus_minus.add(tuple(rep))

        index_of_0 = list()
        index_of_1 = list()

        for i in xrange(len(rep)):
            if rep[i] == 1:
                index_of_1.append(i)
            else:
                index_of_0.append(i)

        for i in index_of_1:
            for j in index_of_0:
                if j <= i:
                    rep_plus_minus.add(tuple(rep[:j] + [1] + rep[j+1:i] + [0] + rep[i+1:]))
                else:
                    rep_plus_minus.add(tuple(rep[:i] + [0] + rep[i+1:j] + [1] + rep[j+1:]))

        return rep_plus_minus

    def get_rep_plus_and_rep_minus(self, rep):
        rep_plus_and_rep_minus = set()
        rep = list(rep)

        for i in xrange(len(rep)):
            rep_plus_and_rep_minus.add(tuple(rep[:i] + [1 - rep[i]] + rep[i+1:]))

        return rep_plus_and_rep_minus
