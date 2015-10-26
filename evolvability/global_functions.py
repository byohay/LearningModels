from math import log

__author__ = 'yben_000'


def get_set_of_all_representations_with_length(length):
    representation_class = set()

    for i in xrange(2**length):
        representation_class.add(tuple(int(x) for x in bin(i)[2:].zfill(length)))

    return representation_class


def get_selection_size_for_perf(length, epsilon):
        #return (self.length / epsilon)**6
        """ This is an alternative param taken from Kanade's dissertation,
            In there he takes the approximation param to be epsilon^2/36.
            We get the selection size by using chernoff bound.
            Note that this parameter won't work on all sizes, but it works well on length=10
        """
        return int(log(1 / epsilon) / (((epsilon**2)/36)**2))


def compute_part(length, epsilon, mutation_neighborhood,
                 tolerance, natural_process, representation_class,
                 times_to_compute, get_number_of_generations_of_single_run):
    generation_number = 0

    for _ in xrange(times_to_compute):
        generation_number += get_number_of_generations_of_single_run(length, epsilon, mutation_neighborhood,
                                                                     tolerance, natural_process, representation_class)

    print "finished with " + str(float(generation_number) / times_to_compute)
    return float(generation_number) / times_to_compute


def frange(x, y, jump):
    list_range = list()
    while x <= y:
        list_range.append(x)
        x += jump

    return list_range



