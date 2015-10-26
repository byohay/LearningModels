from math import log
from LearningModels.DNF import DNF
from LearningModels.evolvability.DNF.one_side_performance_oracle_with_tolerance import DNFOneSidePerformanceOracleWithTolerance
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_evolvability_algorithm import \
    ConjunctionEvolvabilityAlgorithm
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_mutation_probability import \
    ConjunctionMutationProbability
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import \
    MonotoneConjunctionNeighborhood
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_tolerance import \
    ConjunctionTolerance
from LearningModels.evolvability.classic_model.mutator import Mutator
from LearningModels.evolvability.monotone_conjunction.one_sided_performance_oracle_with_tolerance import \
    OneSidedPerformanceOracleWithTolerance
from LearningModels.evolvability.monotone_conjunction.performance_oracle_with_tolerance import \
    PerformanceOracleWithTolerance
from LearningModels.evolvability.with_population.HGT.HGT_mutator import HGT_Mutator
from LearningModels.evolvability.with_population.HGT.HGT_process import HGTProcess
from LearningModels.evolvability.with_population.monotone_conjunction_algorithm.constant_population_algorithm import \
    ConstantPopulationMutationConjunctionAlgorithm
from LearningModels.evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations
from LearningModels.evolvability.with_population.recombination.recombination_process import RecombinationProcess
from LearningModels.evolvability.with_population.recombination.recombinator import Recombinator

__author__ = 'yben_000'


def learn_DNF__recombination():
    dnf = DNF()
    length = 58
    epsilon = (2**-53)
    tau = (epsilon / length)**3 * log(1/epsilon)

    tolerance = ConjunctionTolerance(length, epsilon)
    conjunction_performance_oracle = OneSidedPerformanceOracleWithTolerance(dnf, tau)
    performance_oracle = DNFOneSidePerformanceOracleWithTolerance(dnf, tau, epsilon,
                                                                  conjunction_performance_oracle)
    mutation_neighborhood = MonotoneConjunctionNeighborhood()

    recomb_rate = 0.35
    natural_process = RecombinationProcess(recomb_rate)

    neighborhood = NeighborhoodWithOtherRepresentations(length, mutation_neighborhood,
                                                        0.1, natural_process)

    recombinator = Recombinator(neighborhood, performance_oracle, tolerance, epsilon)
    algorithm = ConstantPopulationMutationConjunctionAlgorithm(recombinator, length, epsilon, performance_oracle, 75)

    print algorithm.learn_ideal_function_until_match()


def learn_DNF__basic_model():
    dnf = DNF()
    length = 58
    epsilon = (2**-53)
    tau = (epsilon / length)**3 * log(1/epsilon)

    tolerance = ConjunctionTolerance(length, epsilon)
    conjunction_performance_oracle = OneSidedPerformanceOracleWithTolerance(dnf, tau)
    performance_oracle = DNFOneSidePerformanceOracleWithTolerance(dnf, tau, epsilon,
                                                                  conjunction_performance_oracle)
    mutation_neighborhood = MonotoneConjunctionNeighborhood()
    mutation_probability = ConjunctionMutationProbability(mutation_neighborhood)

    mutator = Mutator(mutation_neighborhood, performance_oracle, tolerance, mutation_probability, epsilon)
    algorithm = ConjunctionEvolvabilityAlgorithm(mutator, length, epsilon, performance_oracle)

    print algorithm.learn_ideal_function_until_match()

def learn_DNF__HGT():
    dnf = DNF()
    length = 58
    epsilon = (2**-53)
    tau = (epsilon / length)**3 * log(1/epsilon)

    tolerance = ConjunctionTolerance(length, epsilon)
    conjunction_performance_oracle = OneSidedPerformanceOracleWithTolerance(dnf, tau)
    performance_oracle = DNFOneSidePerformanceOracleWithTolerance(dnf, tau, epsilon,
                                                                  conjunction_performance_oracle)
    mutation_neighborhood = MonotoneConjunctionNeighborhood()

    natural_process = HGTProcess(0.35, length)

    neighborhood = NeighborhoodWithOtherRepresentations(length, mutation_neighborhood,
                                                        0.1, natural_process)

    HGT_mutator = HGT_Mutator(neighborhood, performance_oracle, tolerance, epsilon, natural_process)
    algorithm = ConstantPopulationMutationConjunctionAlgorithm(HGT_mutator, length, epsilon, performance_oracle, 75)

    print algorithm.learn_ideal_function_until_match()

if __name__ == "__main__":
    learn_DNF__recombination()
    learn_DNF__HGT()
