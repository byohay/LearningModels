from random import choice
from evolvability.monotone_conjunction.one_sided_performance_oracle import OneSidedPerformanceOracle
from evolvability.monotone_conjunction.one_sided_performance_oracle_with_tolerance import \
    OneSidedPerformanceOracleWithTolerance

from evolvability.monotone_conjunction.performance_oracle import PerformanceOracle
from evolvability.monotone_conjunction.performance_oracle_with_tolerance import PerformanceOracleWithTolerance
from monotone_conjunctions import MonotoneConjunction

__author__ = 'yben_000'


def get_rep_at_least_as_ideal_for_one_sided(length, concept_class, random_func):
    for j in xrange(length):
        if concept_class.ideal_function[j] is not 0:
            random_func[j] = concept_class.ideal_function[j]

    return random_func


def test_one_sided_performance_with_tolerance(length):
    concept_class = MonotoneConjunction(length)

    one_sided_performance = OneSidedPerformanceOracle(concept_class, 10000)
    one_sided_performance_with_tolerance = OneSidedPerformanceOracleWithTolerance(concept_class, 0)

    random_func = [choice([0, 1]) for _ in xrange(length)]

    print one_sided_performance.get_estimated_performance(random_func)
    print one_sided_performance_with_tolerance.get_estimated_performance(random_func)
    print


def test_performance_with_tolerance(length):
    concept_class = MonotoneConjunction(length)

    performance = PerformanceOracle(concept_class, 100)
    performance_with_tolerance = PerformanceOracleWithTolerance(concept_class, 0)

    random_func = tuple([choice([0, 1]) for _ in xrange(length)])
    print performance.get_estimated_performance(random_func)
    print performance_with_tolerance.get_estimated_performance(random_func)
    print

if __name__ == "__main__":
    for i in xrange(100):
        test_performance_with_tolerance(i)
        test_one_sided_performance_with_tolerance(i)
