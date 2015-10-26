from random import choice
from time import time

__author__ = 'yben_000'


class PerformanceOracle:
    def __init__(self, concept_class, selection_size):
        self.concept_class = concept_class
        self.selection_size = selection_size

    def get_estimated_performance(self, representation):
        """ TODO: consider making this with matrix multiplication

        :param representation:
        :return:
        """
        summation = 0

        samples = [tuple(self.concept_class.get_random_sample()) for _ in xrange(self.selection_size)]
        for sample in samples:
            if (self.concept_class.is_function_answering_yes_on_sample(sample) ==
                    self.concept_class.is_function_answering_yes_on_sample(sample, representation)):
                summation += 1

        return (1 / float(self.selection_size)) * summation
