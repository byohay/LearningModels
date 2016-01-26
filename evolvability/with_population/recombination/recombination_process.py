from itertools import izip
import random
from evolvability.with_population.natural_process_mutation_calculator import \
    NaturalProcessMutationCalculator

__author__ = 'yben_000'


class RecombinationProcess(NaturalProcessMutationCalculator):
    def __init__(self, rate=1):
        self.rate = rate

    def get_a_mutation_from_the_reps(self, first_rep, second_rep):
        """ For a large number_of_desc, it might be faster to compute in advance all
            the possible descendants. It would take 2**n worst case, which is not very
            efficient...
        :param first_rep:
        :param second_rep:
        :return:
        """

        if random.random() > self.rate:
            return random.choice([first_rep, second_rep])

        single_descendant = list()

        for i, j in izip(first_rep, second_rep):
            single_descendant.append((random.choice([i, j])))

        return tuple(single_descendant)
