import unittest

from mock.mock import Mock

from evolvability.monotone_conjunction.performance_oracle_with_tolerance import PerformanceOracleWithTolerance

__author__ = 'yben_000'


class TestPerformanceOracleWithTolerance(unittest.TestCase):
    def setUp(self):
        self.tolerance_param = 0.00001
        self.concept_class = Mock()
        self.perf = PerformanceOracleWithTolerance(self.concept_class, self.tolerance_param)

    def test_one_perf_example(self):

        self.concept_class.ideal_function = (0, 1, 0, 0, 1)

        self.assertAlmostEqual(0.125 * 6, self.perf.get_estimated_performance((0, 0, 1, 0, 1)),
                               delta=self.tolerance_param)
