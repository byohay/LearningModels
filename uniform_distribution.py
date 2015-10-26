from random import choice
from LearningModels.distribution import Distribution

__author__ = 'yben_000'


class UniformDistribution(Distribution):
    def __init__(self, concept_class, length):
        super(UniformDistribution, self).__init__(concept_class, length)

    def get_distribution_of_sample(self, sample):
        return 1 / (2 ** self.length)

    def get_random_sample(self):
        return [choice([-1,1]) for r in xrange(self.length)]
