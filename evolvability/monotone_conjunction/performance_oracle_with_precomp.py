from numpy import random

from evolvability.monotone_conjunction.performance_oracle_with_tolerance import PerformanceOracleWithTolerance

__author__ = 'yben_000'


class PerformanceOracleWithPrecomp(PerformanceOracleWithTolerance):
    def __init__(self, concept_class, tolerance_param, representation_class):
        self.concept_class = concept_class
        self.tolerance_param = tolerance_param

        self.real_perf = dict()

        for rep in representation_class:
            self.real_perf[rep] = super(PerformanceOracleWithPrecomp, self).get_real_performance(rep)

    def get_estimated_performance(self, representation):
        return self.real_perf[tuple(representation)] + random.uniform(-self.tolerance_param, self.tolerance_param)

    def get_real_performance(self, representation):
        return self.real_perf[tuple(representation)]
