import unittest

from mock.mock import Mock
from LearningModels.evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations

__author__ = 'yben_000'


class TestNeighborhoodWithPopulation(unittest.TestCase):
    def setUp(self):
        self.number_of_activations = 2
        self.mutation_neighborhood = Mock()
        self.natural_process = Mock()

        def return_itself(*args):
            return args[0]

        self.mutation_neighborhood.get_neighborhood_of_representation.side_effect = return_itself
        self.natural_process.get_a_mutation_from_the_reps.side_effect = return_itself

    def test_no_mutation(self):
        self.mutation_factor = 0
        self.neighborhood_calc = NeighborhoodWithOtherRepresentations(self.number_of_activations, self.mutation_neighborhood,
                                                                      self.mutation_factor, self.natural_process)

        first_rep = (1, 3, 5)
        second_rep = (2, 4, 6)

        self.neighborhood_calc.get_neighborhood(first_rep, second_rep)

        self.assertEqual(0, self.mutation_neighborhood.get_neighborhood_of_representation.call_count)

    def test_mutation_called_based_on_mutation_factor(self):
        self.mutation_factor = 1
        self.neighborhood_calc = NeighborhoodWithOtherRepresentations(self.number_of_activations, self.mutation_neighborhood,
                                                                      self.mutation_factor, self.natural_process)

        first_rep = (1, 3, 5)
        second_rep = (2, 4, 6)

        self.neighborhood_calc.get_neighborhood(first_rep, second_rep)

        self.assertEqual(self.number_of_activations, self.mutation_neighborhood.get_neighborhood_of_representation.call_count)
