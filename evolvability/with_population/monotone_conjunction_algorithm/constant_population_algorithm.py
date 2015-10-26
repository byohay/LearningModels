from LearningModels.evolvability.with_population.monotone_conjunction_algorithm.conjunction_algorithm import \
    MutationConjunctionAlgorithm

__author__ = 'yben_000'


class ConstantPopulationMutationConjunctionAlgorithm(MutationConjunctionAlgorithm):
    def __init__(self, mutator, length, epsilon, performance_oracle, population_size, population_factor=1):
        super(ConstantPopulationMutationConjunctionAlgorithm, self).__init__(mutator, length, epsilon, performance_oracle)

        self.population_size = int(population_size * population_factor)