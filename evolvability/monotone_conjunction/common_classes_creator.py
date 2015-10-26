from math import log

from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_mutation_probability import \
    ConjunctionMutationProbability
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import \
    MonotoneConjunctionNeighborhood
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_tolerance import \
    ConjunctionTolerance
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.precomp_neighborhood import \
    PrecompMonotoneConjunctionNeighborhood
from LearningModels.evolvability.global_functions import get_set_of_all_representations_with_length
from LearningModels.evolvability.monotone_conjunction.performance_oracle_with_precomp import PerformanceOracleWithPrecomp
from LearningModels.evolvability.monotone_conjunction.performance_oracle_with_tolerance import PerformanceOracleWithTolerance
from LearningModels.evolvability.with_population.HGT.HGT_process import HGTProcess
from LearningModels.evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations
from LearningModels.evolvability.with_population.recombination.recombination_process import RecombinationProcess

__author__ = 'yben_000'


class CommonClassesCreator(object):
    def __init__(self, is_neigh_precomp=True):
        self.length = 40
        self.epsilon = 2**-31
        self.number_of_activations = 10
        self.number_of_mutations_from_mutator = 40
        self.population_size = 200

        self.tolerance = ConjunctionTolerance(self.length, self.epsilon)
        self.tau = (self.epsilon / self.length)**3 * log(1/self.epsilon)

        self.representation_class = None

        if is_neigh_precomp:
            self.representation_class = get_set_of_all_representations_with_length(self.length)
            self.mutation_neighborhood = PrecompMonotoneConjunctionNeighborhood(self.representation_class)
        else:
            self.mutation_neighborhood = MonotoneConjunctionNeighborhood()

        self.mutation_probability = ConjunctionMutationProbability(self.mutation_neighborhood)

    def frange(self, x, y, jump):
        list_range = list()
        while x <= y:
            list_range.append(x)
            x += jump

        return list_range

    def get_common_classes(self):
        return self.length, self.epsilon, self.mutation_neighborhood, self.tolerance

    def set_simulation_variables(self, HGT_factor, mutation_factor, population_factor):
        self.HGT_factor = HGT_factor
        self.mutation_factor = mutation_factor
        self.population_factor = population_factor

    def get_simulation_variables(self):
        return self.HGT_factor, self.mutation_factor, self.population_factor

    def get_HGT_factor(self):
        return self.HGT_factor

    def get_mutation_factor(self):
        return self.mutation_factor

    def get_population_size(self):
        return self.population_size

    def get_population_size_and_factor(self):
        return self.population_size, self.population_factor

    def get_number_of_activations(self):
        return self.number_of_activations


    def get_neighborhood_with_other_representations(self, mutation_factor):
        return NeighborhoodWithOtherRepresentations(self.number_of_mutations_from_mutator,
                                                    self.mutation_neighborhood,
                                                    mutation_factor, self.natural_process)

    def create_next_HGT_process(self, HGT_factor):
        self.natural_process = HGTProcess(HGT_factor, self.length)

    def create_recombination_process(self):
        self.natural_process = RecombinationProcess()

    def get_natural_process(self):
        return self.natural_process

    def get_mutation_probability(self):
        return self.mutation_probability

    def get_perf_without_precomp(self, concept_class):
        return PerformanceOracleWithTolerance(concept_class, self.tau)

    def get_perf(self, concept_class):
        if self.representation_class is None:
            self.representation_class = get_set_of_all_representations_with_length(self.length)

        return PerformanceOracleWithPrecomp(concept_class, self.tau, self.representation_class)
