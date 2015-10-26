import random
from LearningModels.evolvability.with_population.mutator_of_population import MutatorOfPopulation

__author__ = 'yben_000'


class Recombinator(MutatorOfPopulation):
    def __init__(self, neighborhood, performance, tolerance, epsilon):
        super(Recombinator, self).__init__(neighborhood, performance, tolerance, epsilon)

    def get_min_perf_of_parents(self, first_rep, second_rep):
        return min(self.performance.get_estimated_performance(first_rep),
                   self.performance.get_estimated_performance(second_rep))

    def get_next_population(self, current_population):
        next_population = list()

        while len(next_population) < len(current_population):
            first_rep = self.get_one_of_the_list(current_population)
            second_rep = self.get_one_of_the_list(current_population)

            desc = self.neighborhood.get_neighborhood(first_rep, second_rep)

            min_perf_of_parents = self.get_min_perf_of_parents(first_rep, second_rep)
            tolerance = self.tolerance.get_tolerance(first_rep, second_rep)
            feas = self.get_feas_from_neigh(desc, min_perf_of_parents, tolerance)

            if len(feas) > 0:
                next_population.append(self.get_one_of_the_list(feas))

        return next_population

