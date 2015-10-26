import random
from LearningModels.evolvability.with_population.natural_process_mutation_calculator import \
    NaturalProcessMutationCalculator

__author__ = 'yben_000'


class HGTProcess(NaturalProcessMutationCalculator):
    def __init__(self, HGT_factor, length):
        self.length = length
        self.chance_to_pass_genes = HGT_factor

    def compute_percent_of_number_of_reps_in_population(self, population):
        self.fraction_of_reps_that_has_1 = list()

        for gene in xrange(self.length):
            summation = 0

            for x in population:
                summation += x[gene]

            self.fraction_of_reps_that_has_1.append(float(summation) / len(population))

    def get_a_mutation_from_the_reps(self, first_rep, other_population):
        """ This method gets a single representations and a population of representations.
            It starts from the single one and mutates according to the HGT_factor.
            If the HGT_factor is high, there is a high chance of mutating according to other_population.
            It is based on the following assumption:
            If a function is of the form (1, 0, 1), it means that the first gene, say A,
            is present at the genome AND is at the right index. The right index is determined according
            to the ideal function f.
            So, if a genome receives the gene A, but in the wrong index, it doesn't count as if he
            has the gene.
            Example: the ideal function f is (1, 0, 0), and the representation is (0, 0, 1), so
            it can receive the first gene, but we have also to consider the probability that it will be
            in the right index.

            To conclude, we need to do the following computation: the probability to receive a gene
            at the right index is: HGT_factor*(1/n)*(number_of_representations_with_this_gene_in_the_population)

            UPDATE: to make it more realistic, we move only ONE GENE and don't divide the probability by
                    the length of the genome.
        :param first_rep:
        :param other_population:
        :return:
        """

        if len(other_population) is 0:
            return first_rep

        single_mutation = list(first_rep)
        genes_indices = range(self.length)
        genes_transferring = self.get_number_of_genes_transferring()

        for _ in xrange(genes_transferring):
            gene_index = self.get_random_gene_index(genes_indices)

            if self.is_chance_of_gene_passing_occurred() and\
               random.random() < self.get_fraction_of_reps_with_gene(gene_index, single_mutation[gene_index]):
                single_mutation[gene_index] = 1-single_mutation[gene_index]

            genes_indices.remove(gene_index)

        return tuple(single_mutation)

    def get_number_of_genes_transferring(self):
        return random.randint(1, self.length)

    def get_random_gene_index(self, genes_indices):
        return random.choice(genes_indices)

    def is_chance_of_gene_passing_occurred(self):
        return random.random() < self.chance_to_pass_genes

    def get_fraction_of_reps_with_gene(self, gene_index, value):
        """ For value == 0 it should return self.fraction_of_reps_that_has_1[gene_index]
            For value == 1 it should return 1 - self.fraction_of_reps_that_has_1[gene_index]
        """
        return value + (1 - 2 * value) * self.fraction_of_reps_that_has_1[gene_index]
