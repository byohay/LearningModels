from random import randint

from LearningModels.evolvability.global_functions import get_selection_size_for_perf
from LearningModels.evolvability.with_population.mutation_algorithm import MutationAlgorithm

__author__ = 'yben_000'


class MutationConjunctionAlgorithm(MutationAlgorithm):
    def __init__(self, mutator, length, epsilon, performance_oracle, population_factor=1):
        super(MutationConjunctionAlgorithm, self).__init__(mutator, length, epsilon, performance_oracle)

        self.number_of_processors = self.length / 10
        self.parallel_time_steps = 3 * self.length / self.number_of_processors
        """ This number is taken from Kanade's reduction. The reduction needs a population of the number of processors
            to the power of 7.
            Afterwards, he shows that the parallel CSQ can learn conjunctions in constant time, that is,
            it needs 3n queries to be made.
            Because it can learn conjunctions, it can of course learn monotone conjunctions.
            Now, if we choose n processes, the population number will be very large. So, we choose a small number
            of processors in favor of parallel time steps. that means we need to multiply the population size by
            the number of those steps.
            If I choose the number sqrt(n), we will need 3*sqrt(n) time steps to get all the needed queries.
            For n=10, an appropriate number of processors will be 1/5*n, so that n^7 is the population size.
        """
        self.population_size = (self.number_of_processors**7)*self.parallel_time_steps * population_factor

    def get_random_function(self):
        return [randint(0, 1) for _ in xrange(self.length)]
