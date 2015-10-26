from itertools import izip
from math import log
from random import randint

__author__ = 'yben_000'


class PAC_Algorithm:
    def __init__(self, oracle, n):
        self.oracle = oracle
        self.n = n
        self.positive = [1 for r in xrange(self.n)]
        self.negative = [-1 for i in xrange(self.n)]

    def get_current_hypo(self):
        current_hypo = list()
        index = 0
        for pos, neg in izip(self.positive, self.negative):
            if pos == 0 and neg == 0:
                current_hypo.append(0)
            elif pos == 0:
                current_hypo.append(-1)
            elif neg == 0:
                current_hypo.append(1)
            else:
                print "NOT GONNA HAPPEN!!!"
                raise ValueError
        return current_hypo

    def eliminate_unfit_from_current_hypo(self, sample):
        index = 0
        for i in sample:
            if i == 1:
                self.negative[index] = 0
            elif i == -1:
                self.positive[index] = 0
            index += 1

    def learn_ideal_function(self, delta, epsilon):
        number_of_samples = 2 * self.n / epsilon *(log(2 * self.n) + log(1 / delta))
        i = 0
        while i <= number_of_samples:
            [sample, label] = self.oracle.get_random_sample_with_label()

            if not label:
                continue

            self.eliminate_unfit_from_current_hypo(sample)
            i += 1
            print "sample " + str(i)

        return self.get_current_hypo()