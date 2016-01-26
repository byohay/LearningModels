from evolvability.monotone_conjunction.common_classes_creator import CommonClassesCreator
from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_evolvability_algorithm import \
    ConjunctionEvolvabilityAlgorithm
from evolvability.classic_model.mutator import Mutator
from monotone_conjunctions import MonotoneConjunction

__author__ = 'yben_000'


def main():
    common_classes = CommonClassesCreator(False)

    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()

    concept_class = MonotoneConjunction(length)
    performance = common_classes.get_perf_without_precomp(concept_class)
    mutation_probability = common_classes.get_mutation_probability()

    mutator = Mutator(mutation_neighborhood, performance, tolerance, mutation_probability, epsilon)
    algorithm = ConjunctionEvolvabilityAlgorithm(mutator, length, epsilon, performance)

    hypo = algorithm.learn_ideal_function(epsilon)

    print "HYPO IS: " + str(hypo)

if __name__ == "__main__":
    main()