from math import log
from LearningModels.evolvability.with_population.monotone_conjunction_algorithm.conjunction_algorithm import \
    MutationConjunctionAlgorithm

__author__ = 'yben_000'


class RecombinationConjunctionAlgorithm(MutationConjunctionAlgorithm):
    def __init__(self, recombinator, length, epsilon, performance_oracle, population_factor=1):
        super(RecombinationConjunctionAlgorithm, self).__init__(recombinator, length, epsilon,
                                                                performance_oracle, population_factor)

        self.generation_size = int(log(self.length / self.epsilon)**2)*self.parallel_time_steps
