import unittest
from LearningModels.evolvability.with_population.recombination.recombination_process import RecombinationProcess

__author__ = 'yben_000'


class TestRecombinationProcess(unittest.TestCase):
    def setUp(self):
        self.process = RecombinationProcess()

    def test_get_recomb_of_two_reps_without_mutation(self):

        first_rep = (1, 3, 5)
        second_rep = (2, 4, 6)

        desc_rep = self.process.get_a_mutation_from_the_reps(first_rep, second_rep)

        self.assertIn(desc_rep[0], [1, 2])
        self.assertIn(desc_rep[1], [3, 4])
        self.assertIn(desc_rep[2], [5, 6])
