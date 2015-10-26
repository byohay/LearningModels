from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import \
    MonotoneConjunctionNeighborhood

__author__ = 'yben_000'


class PrecompMonotoneConjunctionNeighborhood(MonotoneConjunctionNeighborhood):
    def __init__(self, representation_class):
        self.neighbors_dict = dict()
        self.rep_plus_and_rep_minus_dict = dict()
        self.rep_plus_minus_dict = dict()

        for rep in representation_class:
            self.rep_plus_and_rep_minus_dict[rep] = super(PrecompMonotoneConjunctionNeighborhood, self).get_rep_plus_and_rep_minus(rep)
            self.rep_plus_minus_dict[rep] = super(PrecompMonotoneConjunctionNeighborhood, self).get_rep_plus_minus(rep)
            self.neighbors_dict[rep] = self.rep_plus_minus_dict[rep] | self.rep_plus_and_rep_minus_dict[rep]

    def get_neighborhood_of_rep(self, rep):
        return self.neighbors_dict[rep]

    def get_rep_plus_and_rep_minus(self, rep):
        return self.rep_plus_and_rep_minus_dict[rep]

    def get_rep_plus_minus(self, rep):
        return self.rep_plus_minus_dict[rep]
