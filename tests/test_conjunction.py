import unittest
from LearningModels.conjunction import Conjunction

__author__ = 'yben_000'


class TestConjunction(unittest.TestCase):
    def setUp(self):
        self.conjunction = Conjunction(6)

    def test_is_function_answering_yes_on_sample__answer_no(self):
        function = [1, 1, -1, 0, -1, 0]

        x = [1, 1, 1, 1, -1, 1]

        self.assertEqual(False, self.conjunction.is_function_answering_yes_on_sample(x, function))

    def test_is_function_answering_yes_on_sample__answer_yes(self):
        function = [1, 1, -1, 0, -1, 0]

        x = [1, 1, -1, 1, -1, 1]

        self.assertEqual(True, self.conjunction.is_function_answering_yes_on_sample(x, function))

    def test_get_random_false_sample(self):
        for i in xrange(10000):
            function = [1, 1, -1, 0, -1, 0]
            self.conjunction.ideal_function = function

            sample = self.conjunction.get_random_false_sample()

            self.assertEqual(False, self.conjunction.is_function_answering_yes_on_sample(sample, function))
