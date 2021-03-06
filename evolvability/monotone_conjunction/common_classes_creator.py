from fractions import Fraction
from math import log

from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_mutation_probability import \
    ConjunctionMutationProbability
from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import \
    MonotoneConjunctionNeighborhood
from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood_output_one import \
    ConjunctionNeighborhoodOutputOne
from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_tolerance import \
    ConjunctionTolerance
from evolvability.classic_model.monotone_conjunction_algorithm.precomp_neighborhood import \
    PrecompMonotoneConjunctionNeighborhood
from evolvability.global_functions import get_set_of_all_representations_with_length
from evolvability.monotone_conjunction.performance_oracle_with_precomp import PerformanceOracleWithPrecomp
from evolvability.monotone_conjunction.performance_oracle_with_tolerance import PerformanceOracleWithTolerance
from evolvability.monotone_conjunction.performance_oracle_with_tolerance_precise import \
    PerformanceOracleWithTolerancePrecise
from evolvability.with_population.HGT.HGT_process import HGTProcess
from evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations
from evolvability.with_population.recombination.recombination_process import RecombinationProcess

__author__ = 'yben_000'


class CommonClassesCreator(object):
    def __init__(self, is_neigh_precomp=True, is_using_output_one_neigh=True):
        self.length = 100
        self.epsilon = Fraction(2**-55)
        self.number_of_activations = 20
        self.number_of_mutations_from_mutator = 50
        self.population_size = 75

        self.tolerance = ConjunctionTolerance(self.length, self.epsilon)
        self.tau = 0  # (self.epsilon / Decimal(self.length))**Decimal(3) * log(1/self.epsilon)

        self.representation_class = None

        if is_neigh_precomp:
            self.representation_class = get_set_of_all_representations_with_length(self.length)
            self.mutation_neighborhood = PrecompMonotoneConjunctionNeighborhood(self.representation_class)
        elif is_using_output_one_neigh:
            self.mutation_neighborhood = ConjunctionNeighborhoodOutputOne()
        else:
            self.mutation_neighborhood = MonotoneConjunctionNeighborhood()

        self.mutation_probability = ConjunctionMutationProbability(self.mutation_neighborhood)

        self.recombination_factor = 1

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

    def get_recombination_factor(self):
        return self.recombination_factor

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

    def set_recombination_factor(self, recombination_factor):
        self.recombination_factor = recombination_factor

    def create_recombination_process(self, rate=1):
        self.natural_process = RecombinationProcess(rate)

    def get_natural_process(self):
        return self.natural_process

    def get_mutation_probability(self):
        return self.mutation_probability

    def get_perf_without_precomp(self, concept_class):
        return PerformanceOracleWithTolerancePrecise(concept_class, self.tau)

    def get_perf(self, concept_class):
        if self.representation_class is None:
            self.representation_class = get_set_of_all_representations_with_length(self.length)

        return PerformanceOracleWithPrecomp(concept_class, self.tau, self.representation_class)
