from random import randint, choice

__author__ = 'yben_000'


class Conjunction:
    def __init__(self, n):
        self.n = n
        self.ideal_function = [randint(-1, 1) for _ in xrange(self.n)]

    def get_ideal_function(self):
        return self.ideal_function

    def get_random_sample(self):
        return [choice([-1, 1]) for _ in xrange(self.n)]

    def is_ideal_function_all_zeros(self):
        return self.ideal_function == tuple([0 for _ in xrange(self.n)])

    # TODO: this doesn't output a sample with equal probability
    def get_random_false_sample(self):
        false_sample = list()
        number_of_non_zeros = 0
        indices_of_non_zeros = list()

        for i in xrange(self.n):
            if self.ideal_function[i] is not 0:
                number_of_non_zeros += 1
                indices_of_non_zeros.append(i)

        random_number_of_falses_in_sample = randint(1, number_of_non_zeros)
        indices_that_contradict_function = list()

        for i in xrange(random_number_of_falses_in_sample):
            index = choice(indices_of_non_zeros)
            indices_that_contradict_function.append(index)
            indices_of_non_zeros.remove(index)

        for i in xrange(self.n):
            if i in indices_that_contradict_function:
                false_sample.append(-1 * self.ideal_function[i])
            elif self.ideal_function[i] is not 0:
                false_sample.append(self.ideal_function[i])
            else:
                false_sample.append(choice([-1, 1]))

        return false_sample

    def is_function_answering_yes_on_sample(self, sample, function=None):
        if function is None:
            function = self.ideal_function

        index = -1
        for i in function:
            index += 1
            if i is 0:
                continue
            if i != sample[index]:
                return False

        return True
