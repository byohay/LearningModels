__author__ = 'yben_000'

from numpy import random


class Mutator(object):
    def __init__(self, neighborhood, performance, tolerance, mutation_probability, epsilon):
        self.neighborhood = neighborhood
        self.performance = performance
        self.tolerance = tolerance
        self.mutation_probability = mutation_probability
        self.epsilon = epsilon

    def get_one_of_the_list(self, list_of_mutations, current_rep):
        probabilities = list()

        for rep in list_of_mutations:
            probabilities.append(self.mutation_probability.get_relational_probability(current_rep, rep, self.epsilon))

        sum_of_prob = sum(probabilities)
        normalized_prob = [prob / sum_of_prob for prob in probabilities]

        return self.get_random_choice_from_prob(list_of_mutations, normalized_prob)

    def get_random_choice_from_prob(self, list_of_mutations, normalized_prob):
        list_of_mutations_str = list()
        for mutation in list_of_mutations:
            list_of_mutations_str.append(''.join([str(x) for x in mutation]))

        chosen = random.choice(list_of_mutations_str, p=normalized_prob)

        return tuple(int(x) for x in tuple(chosen))

    def evolutionary_step(self, current_rep):
        neighborhood = self.neighborhood.get_neighborhood_of_rep(current_rep)
        beneficial = list()
        neutral = list()

        current_rep_perf = self.performance.get_estimated_performance(current_rep)
        for other_rep in neighborhood:
            other_rep_perf = self.performance.get_estimated_performance(other_rep)
            if other_rep_perf >= current_rep_perf + self.tolerance.get_tolerance(other_rep):
                beneficial.append(other_rep)
            else:
                neutral.append(other_rep)

        if len(beneficial) > 0:
            return self.get_one_of_the_list(beneficial, current_rep)

        return self.get_one_of_the_list(neutral, current_rep)

    def evolutionary_step_feas(self, current_rep):
        neighborhood = self.neighborhood.get_neighborhood_of_rep(current_rep)
        feas = list()
        neutral = list()

        current_rep_perf = self.performance.get_estimated_performance(current_rep)
        for other_rep in neighborhood:
            other_rep_perf = self.performance.get_estimated_performance(other_rep)
            if other_rep_perf >= current_rep_perf - self.tolerance.get_tolerance(other_rep):
                feas.append(other_rep)
            else:
                neutral.append(other_rep)

        if len(feas) > 0:
            return self.get_one_of_the_list(feas, current_rep)

        return self.get_one_of_the_list(neutral, current_rep)
