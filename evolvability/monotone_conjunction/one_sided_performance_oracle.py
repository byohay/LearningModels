__author__ = 'yben_000'


class OneSidedPerformanceOracle:
    def __init__(self, concept_class, selection_size):
        self.concept_class = concept_class
        self.selection_size = selection_size

    def get_estimated_performance(self, representation):
        """ TODO: consider making this with matrix multiplication

        :param representation:
        :return:
        """
        summation = 0

        if self.concept_class.is_ideal_function_all_zeros():
            return 1

        i = 0
        while i < self.selection_size:
            sample = self.concept_class.get_random_sample()
            while self.concept_class.is_function_answering_yes_on_sample(sample):
                sample = self.concept_class.get_random_sample()

            if not self.concept_class.is_function_answering_yes_on_sample(sample, representation):
                summation += 1

            i += 1

        return (1 / float(self.selection_size)) * summation
