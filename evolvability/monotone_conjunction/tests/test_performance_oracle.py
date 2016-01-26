import unittest

from mock.mock import Mock

from evolvability.monotone_conjunction.performance_oracle import PerformanceOracle

__author__ = 'yben_000'


class TestPerformanceOracle(unittest.TestCase):
    def setUp(self):
        self.concept_class = Mock()
        self.representation_class = [(0, 1, 1)]
        selection_size = 5

        self.performance_oracle = PerformanceOracle(self.concept_class, self.representation_class,
                                                    selection_size)

    def test_simple_perf(self):

        self.concept_class.is_function_answering_yes_on_sample.side_effect = [True, True, False, False, True, False,
                                                                              False, True, True, False]

        representation = [1, 0, 0]

        self.assertEqual(0.4, self.performance_oracle.get_estimated_performance(representation))
