from evolvability.monotone_conjunction.common_classes_creator import CommonClassesCreator
from evolvability.with_population.HGT.HGT_mutator import HGT_Mutator
from evolvability.with_population.HGT.HGT_process import HGTProcess
from evolvability.with_population.HGT.mutation_conjunction_algorithm import HGTConjunctionAlgorithm
from evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations
from monotone_conjunctions import MonotoneConjunction

__author__ = 'yben_000'


def HGT_main():
    common_classes = CommonClassesCreator()

    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    mutation_factor = 0.1
    HGT_factor = 1

    concept_class = MonotoneConjunction(length)
    performance = common_classes.get_perf_without_precomp(concept_class)

    HGT_process = HGTProcess(HGT_factor, length)
    neighborhood = NeighborhoodWithOtherRepresentations(length, mutation_neighborhood,
                                                        mutation_factor, HGT_process)
    HGT_mutator = HGT_Mutator(neighborhood, performance, tolerance, epsilon, HGT_process)
    mutation = HGTConjunctionAlgorithm(HGT_mutator, length, epsilon, performance)

    final_population = mutation.learn_ideal_function(concept_class)

    if len(final_population) <= 30:
        print final_population

if __name__ == "__main__":
    HGT_main()
