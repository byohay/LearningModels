from LearningModels.evolvability.monotone_conjunction.common_classes_creator import CommonClassesCreator
from LearningModels.evolvability.with_population.HGT.HGT_mutator import HGT_Mutator
from LearningModels.evolvability.with_population.HGT.HGT_process import HGTProcess
from LearningModels.evolvability.with_population.HGT.mutation_conjunction_algorithm import HGTConjunctionAlgorithm
from LearningModels.evolvability.with_population.neighborhood import NeighborhoodWithOtherRepresentations
from LearningModels.evolvability.global_functions import compute_part
from LearningModels.monotone_conjunctions import MonotoneConjunction
from joblib import Parallel, delayed

__author__ = 'yben_000'


def get_number_of_generations_of_single_run(common_classes, population_factor=1, mutation_factor=0.1):
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    natural_process = common_classes.get_natural_process()

    concept_class = MonotoneConjunction(length)

    performance_oracle = common_classes.get_perf(concept_class)
    neighborhood = common_classes.get_neighborhood_with_other_representations(mutation_factor)
    HGT_mutator = HGT_Mutator(neighborhood, performance_oracle, tolerance, epsilon, natural_process)
    algorithm = HGTConjunctionAlgorithm(HGT_mutator, length, epsilon, performance_oracle, population_factor)

    return algorithm.learn_ideal_function_until_match()


def get_performance_rate_of_single_run(common_classes, population_factor=1, mutation_factor=0.1):
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    natural_process = common_classes.get_natural_process()

    concept_class = MonotoneConjunction(length)

    performance_oracle = common_classes.get_perf(concept_class)
    neighborhood = common_classes.get_neighborhood_with_other_representations(mutation_factor)
    HGT_mutator = HGT_Mutator(neighborhood, performance_oracle, tolerance, epsilon, natural_process)
    algorithm = HGTConjunctionAlgorithm(HGT_mutator, length, epsilon, performance_oracle, population_factor)

    return algorithm.get_learning_rate()


def HGT_simulations_main__performance_rate():
    common_classes = CommonClassesCreator()
    number_of_activations, population_factors, \
    HGT_factors, mutation_factors = common_classes.get_simulation_variables()
    HGT_factor = 0.5

    avg_performance_rate = list()
    for i in xrange(1000):
        avg_performance_rate.append((0, [0]*i))

    common_classes.create_next_HGT_process(HGT_factor)

    for _ in xrange(number_of_activations):
        current_performance_rate = get_performance_rate_of_single_run(common_classes)

        performance_rate_with_same_generation = avg_performance_rate[len(current_performance_rate)]
        avg_performance_rate[len(current_performance_rate)] = (performance_rate_with_same_generation[0]+1,
                                                               [a+b for a, b in zip(performance_rate_with_same_generation[1],current_performance_rate)])

    for i in xrange(len(avg_performance_rate)):
        if avg_performance_rate[i][0] is not 0:
            average_rate_for_generation_i = [avg_rate / avg_performance_rate[i][0] for avg_rate in avg_performance_rate[i][1]]
            print "performance rate for " + str(i) + " generation is: " + str(average_rate_for_generation_i)


def HGT_simulations_main__HGT_factor():
    common_classes = CommonClassesCreator()
    number_of_activations, population_factors, \
    HGT_factors, mutation_factors = common_classes.get_simulation_variables()
    number_of_generations_per_factor = list()

    for HGT_factor in HGT_factors:
        generation_number = 0
        common_classes.create_next_HGT_process(HGT_factor)

        for _ in xrange(number_of_activations):
            generation_number += get_number_of_generations_of_single_run(common_classes)

        avg_number_of_generations = float(generation_number) / number_of_activations

        print "number_of_generations for " + str(HGT_factor) + " factor is: " + str(avg_number_of_generations)
        number_of_generations_per_factor.append(avg_number_of_generations)

    print "number_of_generations_per_factor: " + str(number_of_generations_per_factor)


def HGT_simulations_main__mutation_factor(HGT_factor):
    common_classes = CommonClassesCreator()
    number_of_activations, population_factors, \
    HGT_factors, mutation_factors = common_classes.get_simulation_variables()
    number_of_generations_per_factor = list()

    for mutation_factor in mutation_factors:
        generation_number = 0
        common_classes.create_next_HGT_process(HGT_factor)

        for _ in xrange(number_of_activations):
            generation_number += get_number_of_generations_of_single_run(common_classes, 1, mutation_factor)

        avg_number_of_generations = float(generation_number) / number_of_activations

        print "number_of_generations for " + str(mutation_factor) + " mutation_factor " \
              "is: " + str(avg_number_of_generations)
        number_of_generations_per_factor.append(avg_number_of_generations)

    print "number_of_generations_per_factor: " + str(number_of_generations_per_factor)


def HGT_simulations_main__parallel():
    common_classes = CommonClassesCreator()

    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    number_of_activations, population_factors, HGT_factors, mutation_factors = common_classes.get_simulation_variables()

    number_of_generations_per_factor = list()
    parallel = Parallel(n_jobs=-1)

    for HGT_factor in HGT_factors:
        HGT_process = HGTProcess(HGT_factor, length)

        avg_number_of_generations = sum(parallel(delayed(compute_part)(length, epsilon, mutation_neighborhood,
                                                                       tolerance, HGT_process, representation_class,
                                                                       number_of_activations / 4,
                                                                       get_number_of_generations_of_single_run)
                                                 for _ in xrange(4))) / 4

        print "number_of_generations for " + str(HGT_factor) + " factor is: " + str(avg_number_of_generations)
        number_of_generations_per_factor.append(avg_number_of_generations)

    print "number_of_generations_per_factor: " + str(number_of_generations_per_factor)


def HGT_simulations_main__population_factor():
    common_classes = CommonClassesCreator()

    number_of_activations, population_factors, \
    HGT_factors, mutation_factors = common_classes.get_simulation_variables()
    HGT_factor = 0.2

    number_of_generations_per_factor = list()

    for population_factor in population_factors:
        generation_number = 0
        common_classes.create_next_HGT_process(HGT_factor)

        for _ in xrange(number_of_activations):
            generation_number += get_number_of_generations_of_single_run(common_classes, population_factor)

        avg_number_of_generations = float(generation_number) / number_of_activations

        print "number_of_generations for " + str(population_factor) + " population is: " + str(avg_number_of_generations)
        number_of_generations_per_factor.append(avg_number_of_generations)

    print "number_of_generations_per_factor: " + str(number_of_generations_per_factor)

if __name__ == "__main__":
    HGT_simulations_main__HGT_factor()
