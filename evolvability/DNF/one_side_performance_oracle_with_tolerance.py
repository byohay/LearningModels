from numpy import random

__author__ = 'yben_000'


class DNFOneSidePerformanceOracleWithTolerance(object):
    def __init__(self, concept_class, tolerance_param, epsilon, conjunction_performance_function):
        self.concept_class = concept_class
        self.tolerance_param = tolerance_param
        self.epsilon = epsilon
        self.conjunction_performance_function = conjunction_performance_function

    def get_max_performance(self, representation):
        """


        :param representation:
        :return: the max performance of the representation with a conjunction in DNF.
        """
        max_perf_with_conjunction = 0
        for conjunction in self.concept_class.get_ideal_function():
            current_conjunction_perf = self.conjunction_performance_function.get_real_performance(representation, conjunction)
            max_perf_with_conjunction = max(current_conjunction_perf, max_perf_with_conjunction)

        return max_perf_with_conjunction

    def get_average_performance(self, representation):
        """


        :param representation:
        :return: the average performance of the representation with a conjunction in DNF.
        """
        average_perf_with_conjunctions = 0
        for conjunction in self.concept_class.get_ideal_function():
            average_perf_with_conjunctions += \
                self.conjunction_performance_function.get_real_performance(representation, conjunction)

        return float(average_perf_with_conjunctions) / len(self.concept_class.get_ideal_function())

    def get_max_performance_and_others_lower(self, representation):
        """


        :param representation:
        :return: the max perf with a conjunction in the DNF, while other conjunctions
                 lower the received perf.
        """
        list_of_perfs = list()

        for conjunction in self.concept_class.get_ideal_function():
            list_of_perfs.append(self.conjunction_performance_function.get_real_performance(representation,
                                                                                            conjunction))

        perf_to_return = max(list_of_perfs)

        for i in xrange(len(list_of_perfs)):
            perf_to_return -= (1 - list_of_perfs[i])/len(self.concept_class.get_ideal_function())

        return perf_to_return

    def get_real_performance(self, representation):
        return self.get_max_performance_and_others_lower(representation)

    def get_estimated_performance(self, representation):
        return self.get_real_performance(representation) + random.uniform(-self.tolerance_param, self.tolerance_param)
