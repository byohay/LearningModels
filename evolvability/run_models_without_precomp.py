import cProfile
import pstats
from joblib.parallel import Parallel, delayed
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_evolvability_algorithm import \
    ConjunctionEvolvabilityAlgorithm
from LearningModels.evolvability.classic_model.mutator import Mutator
from LearningModels.evolvability.global_functions import frange
from LearningModels.evolvability.monotone_conjunction.common_classes_creator import CommonClassesCreator
from LearningModels.evolvability.with_population.HGT.HGT_mutator import HGT_Mutator
from LearningModels.evolvability.with_population.monotone_conjunction_algorithm.constant_population_algorithm import \
    ConstantPopulationMutationConjunctionAlgorithm
from LearningModels.evolvability.with_population.recombination.recombinator import Recombinator
from LearningModels.monotone_conjunctions import MonotoneConjunction

__author__ = 'yben_000'


def get_params_for_mutator(common_classes):
    mutation_factor = common_classes.get_mutation_factor()
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    natural_process = common_classes.get_natural_process()

    concept_class = MonotoneConjunction(length)

    performance_oracle = common_classes.get_perf_without_precomp(concept_class)
    neighborhood = common_classes.get_neighborhood_with_other_representations(mutation_factor)
    return neighborhood, performance_oracle, natural_process


def learn_single_time__recombination(common_classes):
    neighborhood, performance_oracle, natural_process = get_params_for_mutator(common_classes)
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    population_size, population_factor = common_classes.get_population_size_and_factor()

    recombinator = Recombinator(neighborhood, performance_oracle, tolerance, epsilon)
    algorithm = ConstantPopulationMutationConjunctionAlgorithm(recombinator, length, epsilon, performance_oracle,
                                                               population_size, population_factor)

    return algorithm.learn_ideal_function_until_match()


def learn_single_time__HGT(common_classes):
    neighborhood, performance_oracle, natural_process = get_params_for_mutator(common_classes)
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    population_size, population_factor = common_classes.get_population_size_and_factor()

    HGT_mutator = HGT_Mutator(neighborhood, performance_oracle, tolerance, epsilon, natural_process)
    algorithm = ConstantPopulationMutationConjunctionAlgorithm(HGT_mutator, length, epsilon, performance_oracle,
                                                               population_size, population_factor)

    return algorithm.learn_ideal_function_until_match()


def learn_single_time__classic_model(common_classes):
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()
    mutation_probability = common_classes.get_mutation_probability()

    concept_class = MonotoneConjunction(length)
    performance = common_classes.get_perf_without_precomp(concept_class)
    mutator = Mutator(mutation_neighborhood, performance, tolerance, mutation_probability, epsilon)
    algorithm = ConjunctionEvolvabilityAlgorithm(mutator, length, epsilon, performance)

    return algorithm.learn_ideal_function_until_match()


def learn_recombination(common_classes, number_of_activations):
    total_number_of_generations = 0
    common_classes.create_recombination_process()
    for _ in xrange(number_of_activations):
        current_generation_number = learn_single_time__recombination(common_classes)
        total_number_of_generations += current_generation_number

    avg_number_of_generations = float(total_number_of_generations) / number_of_activations

    return avg_number_of_generations


def learn_HGT(common_classes, number_of_activations):
    total_number_of_generations = 0
    HGT_factor = common_classes.get_HGT_factor()
    common_classes.create_next_HGT_process(HGT_factor)

    for _ in xrange(number_of_activations):
        current_generation_number = learn_single_time__HGT(common_classes)
        total_number_of_generations += current_generation_number

    avg_number_of_generations = float(total_number_of_generations) / number_of_activations

    return avg_number_of_generations


def learn_classical_model(common_classes, number_of_activations):
    total_number_of_generations = 0

    for _ in xrange(number_of_activations):
        current_generation_number = learn_single_time__classic_model(common_classes)
        total_number_of_generations += current_generation_number

    avg_number_of_generations = float(total_number_of_generations) / number_of_activations

    return avg_number_of_generations


def run_in_parallel(common_classes, number_of_activations, function_to_run,
                    parallel, number_of_parallel):

    avg_number_of_generations = sum(parallel(delayed(function_to_run)(common_classes, number_of_activations / number_of_parallel)
                                             for _ in xrange(number_of_parallel))) / number_of_parallel

    f = open('results.txt', 'a')

    HGT_factor, mutation_factor, population_factor = common_classes.get_simulation_variables()

    f.write("results for the following parameters: HGT_factor=" + str(HGT_factor) +
            " mutation factor=" + str(mutation_factor) + " population_factor=" + str(population_factor) +
            " is: " + str(avg_number_of_generations) + "\n")

    f.close()


def compare_with_HGT_factors(common_classes):
    number_of_activations = common_classes.get_number_of_activations()
    common_classes.set_simulation_variables(0, 0.1, 1)
    number_of_parallel = 3
    parallel = Parallel(n_jobs=number_of_parallel)
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()

    f = open('results.txt', 'a')
    f.write("\n~~~HGT rate experiment~~~\n")
    f.write("\npopulation size is " + str(common_classes.get_population_size()))
    f.write("\nlenghth is {0} and epsilon is {1}\n".format(length, epsilon))
    f.close()

    f = open('results.txt', 'a')
    f.write("\nbasic model:\n")
    f.close()

    run_in_parallel(common_classes, number_of_activations, function_to_run=learn_classical_model,
                    parallel=parallel, number_of_parallel=number_of_parallel)

    f = open('results.txt', 'a')
    f.write("\nHGT:\n")
    f.close()

    for HGT_factor in frange(0, 1, 0.1):
        common_classes.set_simulation_variables(HGT_factor, 0.1, 1)
        run_in_parallel(common_classes, number_of_activations, function_to_run=learn_HGT,
                        parallel=parallel, number_of_parallel=number_of_parallel)

    f = open('results.txt', 'a')
    f.write("\nrecombination:\n")
    f.close()

    run_in_parallel(common_classes, number_of_activations, function_to_run=learn_recombination,
                    parallel=parallel, number_of_parallel=number_of_parallel)


def compare_with_mutation_factors(common_classes):
    number_of_activations = common_classes.get_number_of_activations()
    number_of_parallel = 3
    parallel = Parallel(n_jobs=number_of_parallel)
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()

    f = open('results.txt', 'a')
    f.write("\n~~~mutation factor experiment~~~\n")
    f.write("\npopulation size is " + str(common_classes.get_population_size()))
    f.write("\nlenghth is {0} and epsilon is {1}\n".format(length, epsilon))
    f.close()

    f = open('results.txt', 'a')
    f.write("\nHGT 1:\n")
    f.close()

    for mutation_factor in frange(0.1, 1, 0.1):
        common_classes.set_simulation_variables(1, mutation_factor, 1)
        run_in_parallel(common_classes, number_of_activations, function_to_run=learn_HGT,
                        parallel=parallel, number_of_parallel=number_of_parallel)

    f = open('results.txt', 'a')
    f.write("\nHGT 0.1:\n")
    f.close()

    for mutation_factor in frange(0.1, 1, 0.1):
        common_classes.set_simulation_variables(0.1, mutation_factor, 1)
        run_in_parallel(common_classes, number_of_activations, function_to_run=learn_HGT,
                        parallel=parallel, number_of_parallel=number_of_parallel)

    f = open('results.txt', 'a')
    f.write("\nrecombination:\n")
    f.close()

    for mutation_factor in frange(0.1, 1, 0.1):
        common_classes.set_simulation_variables(1, mutation_factor, 1)
        run_in_parallel(common_classes, number_of_activations, function_to_run=learn_recombination,
                        parallel=parallel, number_of_parallel=number_of_parallel)


def compare_with_population_factors(common_classes):
    number_of_activations = common_classes.get_number_of_activations()
    common_classes.set_simulation_variables(0, 0.1, 1)
    number_of_parallel = 3
    parallel = Parallel(n_jobs=number_of_parallel)
    length, epsilon, mutation_neighborhood, tolerance = common_classes.get_common_classes()

    f = open('results.txt', 'a')
    f.write("\n~~~population factor experiment~~~\n")
    f.write("\npopulation size is " + str(common_classes.get_population_size()))
    f.write("\nlenghth is {0} and epsilon is {1}\n".format(length, epsilon))
    f.close()

    f = open('results.txt', 'a')
    f.write("\nHGT 0.2:\n")
    f.close()

    for population_factor in frange(1, 5, 0.5):
        common_classes.set_simulation_variables(0.2, 0.1, population_factor)
        run_in_parallel(common_classes, number_of_activations, function_to_run=learn_HGT,
                        parallel=parallel, number_of_parallel=number_of_parallel)

    f = open('results.txt', 'a')
    f.write("\nrecombination:\n")
    f.close()

    for population_factor in frange(1, 5, 0.5):
        common_classes.set_simulation_variables(0.1, 0.1, population_factor)
        run_in_parallel(common_classes, number_of_activations, function_to_run=learn_recombination,
                        parallel=parallel, number_of_parallel=number_of_parallel)


def run_models_without_precomp():
    pr = cProfile.Profile()

    pr.enable()

    common_classes = CommonClassesCreator(False)
    compare_with_HGT_factors(common_classes)
    compare_with_mutation_factors(common_classes)
    compare_with_population_factors(common_classes)

    pr.disable()

    pstats.Stats(pr).sort_stats("time").print_stats()


if __name__ == "__main__":
    run_models_without_precomp()
