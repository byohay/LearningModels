__author__ = 'yben_000'


class PAC_Oracle:
    def __init__(self, concept_class, distribution):
        self.concept_class = concept_class
        self.distribution = distribution

    def get_random_sample_with_label(self):
        sample = self.distribution.get_random_sample()

        return sample, self.concept_class.is_function_answering_yes_on_sample(sample)
