from fractions import Fraction
from evolvability.monotone_conjunction.performance_oracle_with_tolerance import PerformanceOracleWithTolerance

__author__ = 'Ben'


class PerformanceOracleWithTolerancePrecise(PerformanceOracleWithTolerance):
    def __init__(self, concept_class, tolerance_param):
        self.concept_class = concept_class
        self.tolerance_param = tolerance_param

    def get_real_performance(self, representation, conjunction = None):
        if conjunction is None:
            conjunction = self.concept_class.ideal_function

        union, intersection, in_rep_not_in_ideal, in_ideal_not_in_rep = self.get_variables_of_correlation(representation, conjunction)

        real_perf = Fraction(2**-union) + (1 - Fraction(2**-intersection)) + Fraction(2**-intersection)*(1 - Fraction(2**-in_rep_not_in_ideal)) *\
                                                                                                        (1 - Fraction(2**-in_ideal_not_in_rep))

        return real_perf
