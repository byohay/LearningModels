import unittest

from mock.mock import Mock

from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_mutation_probability import ConjunctionMutationProbability

__author__ = 'yben_000'


class TestConjunctionMutationProbability(unittest.TestCase):
    def setUp(self):
        self.neighbors_finder = Mock()

        self.conjunction_mutation_probability = ConjunctionMutationProbability(self.neighbors_finder)

    def set_return_value_of_get_rep_plus_and_rep_minus(self):
        returned_neighborhood = set()
        returned_neighborhood.add((1, 0, 0, 1))
        returned_neighborhood.add((1, 1, 0, 0))
        returned_neighborhood.add((0, 1, 0, 1))
        returned_neighborhood.add((1, 1, 1, 1))
        self.neighbors_finder.get_rep_plus_and_rep_minus.return_value = returned_neighborhood

    def test_get_probability_of_rep_from_plus(self):
        representation = [1, 1, 0, 1]

        self.set_return_value_of_get_rep_plus_and_rep_minus()

        probability = self.conjunction_mutation_probability.get_relational_probability(representation, (1, 0, 0, 1), 1)
        self.assertEqual(0.125, probability)

    def test_get_probability_of_rep_from_plus_minus(self):
        """ the representation itself appears in the group r+- and therefore that's the param passed to 'get_relational_probability'
        :return:
        """
        representation = [0, 0, 0, 0]

        self.set_return_value_of_get_rep_plus_and_rep_minus()

        self.neighbors_finder.get_rep_plus_minus.return_value = [(0, 0, 0, 0)]

        probability = self.conjunction_mutation_probability.get_relational_probability(representation, (0, 0, 0, 0), 1)
        self.assertEqual(0.5, probability)
