from random import choice

__author__ = 'yben_000'


class MutatorOfPopulation(object):
    def __init__(self, neighborhood, performance, tolerance, epsilon):
        self.neighborhood = neighborhood
        self.performance = performance
        self.tolerance = tolerance
        self.epsilon = epsilon

    def get_one_of_the_list(self, list_of_mutations):
        return choice(list_of_mutations)

    def get_feas_from_neigh(self, desc, parent_performance, parent_tolerance):
        feas = list()

        for rep in desc:
            rep_perf = self.performance.get_estimated_performance(rep)

            if rep_perf >= parent_performance - parent_tolerance:
                feas.append(rep)

        return feas

