from math import log
from random import randint
from evolvability.monotone_conjunction.algorithm import MonotoneConjunctionAlgorithm

__author__ = 'yben_000'


class ConjunctionEvolvabilityAlgorithm(MonotoneConjunctionAlgorithm):
    def __init__(self, mutator, length, epsilon, performance):
        super(ConjunctionEvolvabilityAlgorithm, self).__init__(performance, epsilon)
        self.mutator = mutator
        self.length = length
        self.epsilon = epsilon

    def learn_ideal_function(self, epsilon):
        number_of_generations = self.length * (log(self.length / epsilon))

        i = 0
        current_rep = tuple([0 for _ in xrange(self.length)])

        while i <= number_of_generations:
            i += 1
            current_rep = self.mutator.evolutionary_step(current_rep)

            if current_rep == self.mutator.performance.concept_class.ideal_function:
                print "EXACT MATCH!"
                return current_rep
            print "current is: " + str(current_rep)

        return current_rep

    def get_random_function(self):
        return tuple([randint(0, 1) for _ in xrange(self.length)])

    def learn_ideal_function_until_match(self):
        generation_number = 0

        current_rep = self.get_random_function()

        while not self.is_representation_similar_to_ideal(current_rep):
            current_rep = self.mutator.evolutionary_step_feas(current_rep)
            generation_number += 1

        return generation_number

    def get_learning_rate(self):
        current_rep = self.get_random_function()

        performance_in_generations = [self.performance_oracle.get_real_performance(current_rep)]

        while not self.is_representation_similar_to_ideal(current_rep):
            current_rep = self.mutator.evolutionary_step_feas(current_rep)
            performance_in_generations.append(self.performance_oracle.get_real_performance(current_rep))

        print len(performance_in_generations)
        return performance_in_generations
