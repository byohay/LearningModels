from LearningModels.evolvability.classic_model.mutation_probability import MutationProbability

__author__ = 'yben_000'


class ConjunctionMutationProbability(MutationProbability):
    def __init__(self, neighborhood_finder):
        self.neighborhood_finder = neighborhood_finder

    def get_relational_probability(self, representation, other_rep, epsilon):
        """ Complexity: n

        :param representation:
        :param other_rep:
        :param epsilon:
        :return:
        """
        rep_plus_and_rep_minus_neighborhood = self.neighborhood_finder.get_rep_plus_and_rep_minus(representation)

        if other_rep in rep_plus_and_rep_minus_neighborhood:
            return 1 / float(len(rep_plus_and_rep_minus_neighborhood)) / 2

        plus_minus_neigh = self.neighborhood_finder.get_rep_plus_minus(representation)

        return 1 / float(len(plus_minus_neigh)) / 2
