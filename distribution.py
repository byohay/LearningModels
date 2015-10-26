__author__ = 'yben_000'


class Distribution(object):
    def __init__(self, concept_class, length):
        self.concept_class = concept_class
        self.length = length

    def get_random_sample(self):
        raise NotImplementedError

    def get_distribution_of_sample(self, sample):
        raise NotImplementedError