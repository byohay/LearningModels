import unittest

from mock.mock import Mock

from LearningModels.evolvability.classic_model.mutator import Mutator

__author__ = 'yben_000'


class TestMutator(unittest.TestCase):
    def setUp(self):
        self.neighborhood = Mock()
        self.performance = Mock()
        self.tolerance = Mock()
        self.mutation_probability = Mock()
        self.mutation_probability.get_relational_probability.return_value = 0.2
        epsilon = 1
        self.selection_size = 1

        self.mutator = Mutator(self.neighborhood, self.performance, self.tolerance, self.mutation_probability, epsilon)

        self.tolerance.get_tolerance.return_value = 2**-5
    def set_neighborhood(self):
        neighborhood = set()

        neighborhood.add(self.expected_rep)
        neighborhood.add((1, 1, 0, 0))
        neighborhood.add((1, 0, 0, 1))

        self.neighborhood.get_neighborhood_of_representation.return_value = neighborhood

    def test_mutator__one_in_bene(self):
        representation = (1, 1, 0, 1)
        perf_of_representation = 0.2
        self.expected_rep = (1, 1, 1, 1)
        perf_of_expected_representation = 0.2 + self.tolerance.get_tolerance.return_value

        def perf_returns(rep):
            if rep == representation:
                return perf_of_representation
            if rep == self.expected_rep:
                return perf_of_expected_representation

            return 0

        self.set_neighborhood()
        self.performance.get_estimated_performance.side_effect = perf_returns

        self.assertEqual(self.expected_rep, self.mutator.evolutionary_step(representation))

    def test_mutator__two_in_neut(self):
        representation = (1, 1, 0, 1)
        self.expected_rep = set()
        self.expected_rep.add((1, 1, 1, 1))
        self.expected_rep.add((0, 0, 0, 0))

        self.performance.get_estimated_performance.return_value = 0
        self.neighborhood.get_neighborhood_of_representation.return_value = self.expected_rep

        self.assertIn(self.mutator.evolutionary_step(representation), self.expected_rep)
