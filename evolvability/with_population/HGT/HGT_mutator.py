from evolvability.with_population.mutator_of_population import MutatorOfPopulation

__author__ = 'yben_000'


class HGT_Mutator(MutatorOfPopulation):
    def __init__(self, neighborhood, performance, tolerance, epsilon, HGT_process):
        super(HGT_Mutator, self).__init__(neighborhood, performance, tolerance, epsilon)
        self.HGT_process = HGT_process

    def get_next_population(self, current_population):
        next_population = list()
        self.HGT_process.compute_percent_of_number_of_reps_in_population(current_population)

        while len(next_population) < len(current_population):
            rep = self.get_one_of_the_list(current_population)

            """ A subtle point here: though we need to take the whole other population, we take instead
                the population without any instance of rep. It is basically the same because 'rep' is not
                going to receive genes from itself.
            """
            neighborhood = self.neighborhood.get_neighborhood(rep,
                                                              [x for x in current_population if x != rep])

            rep_performance = self.performance.get_estimated_performance(rep)
            tolerance = self.tolerance.get_tolerance(rep)
            feas = self.get_feas_from_neigh(neighborhood, rep_performance, tolerance)

            if len(feas) > 0:
                next_population.append(self.get_one_of_the_list(feas))

#            print "Now at " + str(len(next_population)) + " reps"
        return next_population
