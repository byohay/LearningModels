from LearningModels.evolvability.monotone_conjunction.algorithm import MonotoneConjunctionAlgorithm

__author__ = 'yben_000'


class MutationAlgorithm(MonotoneConjunctionAlgorithm):
    def __init__(self, mutator, length, epsilon, performance_oracle):
        super(MutationAlgorithm, self).__init__(performance_oracle, epsilon)
        self.mutator = mutator
        self.length = length
        self.epsilon = epsilon

    def learn_ideal_function(self, concept_class):
        current_population = list()

        ''' In the reduction, Kanade generates random functions '''
        for i in xrange(self.population_size):
            current_population.append(self.get_random_function())

        for i in xrange(self.generation_size):
            if self.concept_class.ideal_function in current_population:
                print "EXACT MATCH!!"
                return current_population
            elif self.is_representation_exists_that_is_almost_as_ideal_function(current_population):
                print "ALMOST MATCH!!"
                return current_population

            current_population = self.mutator.get_next_population(current_population)

        return current_population

    def learn_ideal_function_until_match(self):
        current_population = list()

        ''' In the reduction, Kanade generates random functions '''
        for _ in xrange(self.population_size):
            random_func = self.get_random_function()
            current_population.append(random_func)

        generation_number = 0
        while not self.is_representation_exists_that_is_almost_as_ideal_function(current_population):
            current_population = self.mutator.get_next_population(current_population)
            generation_number += 1

        return generation_number

    def get_learning_rate(self):
        current_population = list()

        ''' In the reduction, Kanade generates random functions '''
        for _ in xrange(self.population_size):
            random_func = self.get_random_function()
            current_population.append(random_func)

        performance_in_generations = [self.get_max_perf(current_population)]

        while not self.is_representation_exists_that_is_almost_as_ideal_function(current_population):
            current_population = self.mutator.get_next_population(current_population)
            performance_in_generations.append(self.get_max_perf(current_population))

        return performance_in_generations
