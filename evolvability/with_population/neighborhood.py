import random

__author__ = 'yben_000'


class NeighborhoodWithOtherRepresentations(object):
    def __init__(self, number_of_activations, mutation_neighborhood, mutation_factor,
                 natural_process_mutation):
        self.number_of_activations = number_of_activations
        self.mutation_neighborhood = mutation_neighborhood
        self.mutation_factor = mutation_factor
        self.natural_process_mutation = natural_process_mutation

    def get_single_mutation(self, first_rep, other_reps_to_consider):
        """ This method creates a mutation that depends solely on the parameters.
            Then, it creates a mutation upon it according to mutation factor
        """
        single_mutation = self.natural_process_mutation.get_a_mutation_from_the_reps(first_rep, other_reps_to_consider)

        if random.random() < self.mutation_factor:
            return self.mutation_neighborhood.get_one_of_neighborhood_of_rep(single_mutation)

        return single_mutation

    def get_neighborhood(self, first_rep, other_reps_to_consider):
        """ This function gets a representation and some other representations.
            It computes a combination between the two and returns a mutated representation.
            It is done number_of_activations times.
            The mutations object is a list because repetitions are allowed.

        :param first_rep:
        :param other_reps_to_consider:
        :return:
        """
        mutations = list()

        for i in xrange(self.number_of_activations):
            mutation = self.get_single_mutation(first_rep, other_reps_to_consider)
            mutations.append(mutation)

        return mutations

