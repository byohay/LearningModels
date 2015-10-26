import unittest

from mock import Mock

from LearningModels.PAC.PAC_Algorithm import PAC_Algorithm

__author__ = 'yben_000'


class TestPACAlgorithm(unittest.TestCase):
    def setUp(self):
        self.oracle = Mock()
        self.pac_alg = PAC_Algorithm(self.oracle, 4)

    def test_get_current_hypo(self):
        with self.assertRaises(ValueError):
            self.pac_alg.get_current_hypo()

    def test_eliminate_unfit_from_current_hypo(self):
        sample = [1, -1, 1, 1]

        self.pac_alg.eliminate_unfit_from_current_hypo(sample)
        self.assertEqual([1, -1, 1, 1], self.pac_alg.get_current_hypo())

        sample2 = [1, -1, -1, 1]

        self.pac_alg.eliminate_unfit_from_current_hypo(sample2)
        self.assertEqual([1, -1, 0, 1], self.pac_alg.get_current_hypo())
