from LearningModels.evolvability.monotone_conjunction.common_classes_creator import CommonClassesCreator
from LearningModels.evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations
from LearningModels.evolvability.with_population.recombination.monotone_conjunction_algorithm.recombination_conjunction import \
    RecombinationConjunctionAlgorithm
from LearningModels.evolvability.with_population.recombination.recombination_process import RecombinationProcess
from LearningModels.evolvability.with_population.recombination.recombinator import Recombinator
from LearningModels.monotone_conjunctions import MonotoneConjunction

__author__ = 'yben_000'


def recombination_main():
    common_classes = CommonClassesCreator()

    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()

    mutation_factor = 0.1

    concept_class = MonotoneConjunction(length)
    performance = common_classes.get_perf_without_precomp(concept_class)

    recomb_process = RecombinationProcess()
    neighborhood = NeighborhoodWithOtherRepresentations(length, mutation_neighborhood,
                                                        mutation_factor, recomb_process)
    recombinator = Recombinator(neighborhood, performance, tolerance, epsilon)
    recombination = RecombinationConjunctionAlgorithm(recombinator, length, epsilon, concept_class)

    recombination.learn_ideal_function(concept_class)

if __name__ == "__main__":
    recombination_main()
