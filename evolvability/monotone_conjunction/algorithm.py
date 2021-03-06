from fractions import Fraction

__author__ = 'yben_000'


class MonotoneConjunctionAlgorithm(object):
    def __init__(self, performance_oracle, epsilon):
        self.performance_oracle = performance_oracle
        self.epsilon = epsilon

    def is_representation_exists_that_is_almost_as_ideal_function(self, population):
        for rep in population:
            if self.is_representation_similar_to_ideal(rep):
                return True

        return False

    def get_min_distance_from_epsilon(self, population):
        max_perf = 0

        for rep in population:
            max_perf = max(self.performance_oracle.get_real_performance(rep), max_perf)

        return (1 - max_perf) - self.epsilon

    def is_representation_similar_to_ideal(self, rep):
        return 1 - self.performance_oracle.get_real_performance(rep) < self.epsilon
