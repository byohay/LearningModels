from numpy import random

__author__ = 'yben_000'


class OneSidedPerformanceOracleWithTolerance(object):
    def __init__(self, concept_class, tolerance_param):
        self.concept_class = concept_class
        self.tolerance_param = tolerance_param

    def get_real_performance(self, representation, conjunction=None):
        if conjunction is None:
            conjunction = self.concept_class.ideal_function

        number_of_ones_in_rep = sum(representation)
        number_of_ones_in_ideal = sum(conjunction)
        in_ideal_not_in_rep = 0

        if number_of_ones_in_ideal is 0:
            return 1

        for i, j in zip(representation, conjunction):
            if i is 0 and j is 1:
                in_ideal_not_in_rep += 1

        real_perf = 1 - ((2 ** -number_of_ones_in_rep) * (1 - 2 ** -in_ideal_not_in_rep) /
                         (1 - 2 ** -number_of_ones_in_ideal))

        return real_perf

    def get_estimated_performance(self, representation):
        return self.get_real_performance(representation) + random.uniform(-self.tolerance_param, self.tolerance_param)
