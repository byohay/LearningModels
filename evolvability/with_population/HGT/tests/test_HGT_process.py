import unittest
from evolvability.with_population.HGT.HGT_process import HGTProcess
from mock import patch
from evolvability.with_population.HGT.HGT_process_constant_genes_number import \
    HGTProcessConstantGenesNumber

__author__ = 'yben_000'


class TestHGTProcess(unittest.TestCase):
    def setUp(self):
        self.rep = (0, 1, 0)
        self.length = 3
        self.population = [(1, 0, 1), (0, 0, 1), (0, 1, 1)]
        self.HGT_factor = 1

    def test_no_HGT_process(self):
        self.HGT_factor = 0
        self.HGT_process = HGTProcessConstantGenesNumber(self.HGT_factor, self.length, 1)

        mutated_rep = self.HGT_process.get_a_mutation_from_the_reps(self.rep, self.population)

        self.assertEqual(self.rep, mutated_rep)

    def test_HGT_process_occurred(self):
        self.HGT_process = HGTProcessConstantGenesNumber(self.HGT_factor, self.length, 1)
        gene_index = 2
        self.HGT_process.compute_percent_of_number_of_reps_in_population(self.population)

        with patch.object(self.HGT_process, 'get_random_gene_index') as mock_func:
            mock_func.return_value = gene_index

            mutated_rep = self.HGT_process.get_a_mutation_from_the_reps(self.rep, self.population)

            self.assertEqual(1, mutated_rep[gene_index])

    def test_compute_percent_of_number_of_reps_in_population(self):
        self.HGT_process = HGTProcessConstantGenesNumber(self.HGT_factor, self.length, 1)

        self.HGT_process.compute_percent_of_number_of_reps_in_population(self.population)

        self.assertEqual([3**-1, 3**-1, 1], self.HGT_process.fraction_of_reps_that_has_1)

    def test_HGT_process_3_times(self):
        number_of_genes = 3
        self.HGT_process = HGTProcessConstantGenesNumber(self.HGT_factor, self.length, number_of_genes)

        with patch.object(self.HGT_process, 'get_fraction_of_reps_with_gene') as mock_func:
            mock_func.return_value = 1
            mutated_rep = self.HGT_process.get_a_mutation_from_the_reps(self.rep, self.population)
            self.assertEqual((1, 0, 1), mutated_rep)
