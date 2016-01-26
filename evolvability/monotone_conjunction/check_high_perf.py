from random import choice
from evolvability.monotone_conjunction.performance_oracle_with_tolerance import \
    PerformanceOracleWithTolerance
from monotone_conjunctions import MonotoneConjunction

__author__ = 'ben'


def check_high_perf():
    length = 40
    concept_class = MonotoneConjunction(length)
    perf = PerformanceOracleWithTolerance(concept_class, 0)

    highest_perf_except_for_1 = 0
    for i in xrange(10000000):
        rep = tuple([choice([0, 1]) for _ in xrange(length)])

        current_perf = perf.get_estimated_performance(rep)

        if current_perf != 1:
            highest_perf_except_for_1 = max(highest_perf_except_for_1, current_perf)

    print highest_perf_except_for_1

