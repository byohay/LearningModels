from decimal import Decimal
from numpy import random

__author__ = 'yben_000'

class PerformanceOracleWithTolerance(object):
    def __init__(self, concept_class, tolerance_param):
        self.concept_class = concept_class
        self.tolerance_param = tolerance_param

    def get_real_performance(self, representation, conjunction = None):
        if conjunction is None:
            conjunction = self.concept_class.ideal_function

        union = 0
        intersection = 0
        in_rep_not_in_ideal = 0
        in_ideal_not_in_rep = 0

        for i, j in zip(representation, conjunction):
            if i is 1 or j is 1:
                union += 1

            if i is 1 and j is 1:
                intersection += 1
            elif i is 1 and j is 0:
                in_rep_not_in_ideal += 1
            elif i is 0 and j is 1:
                in_ideal_not_in_rep += 1

        real_perf = Decimal(2**-union) + (Decimal(1) - Decimal(2**-intersection)) + Decimal(2**-intersection)*(Decimal(1) - Decimal(2**-in_rep_not_in_ideal)) *\
                                                                            (Decimal(1) - Decimal(2**-in_ideal_not_in_rep))

        return real_perf

    def get_estimated_performance(self, representation):
        tolerance = Decimal(random.uniform(-self.tolerance_param, self.tolerance_param))
        real_perf = self.get_real_performance(representation)
        if tolerance + real_perf > 1:
            return 1
        elif tolerance + real_perf < -1:
            return -1

        return tolerance + real_perf
