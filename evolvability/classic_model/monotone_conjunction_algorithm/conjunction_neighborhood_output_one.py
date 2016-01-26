import random

__author__ = 'Ben'


class ConjunctionNeighborhoodOutputOne(object):
    def __init__(self):
        pass

    def get_one_of_neighborhood_of_rep(self, rep):
        if random.random() > 0.5:
            return self.get_one_of_rep_plus_and_rep_minus(rep)
        else:
            return self.get_one_of_rep_plus_minus(rep)

    def get_one_of_rep_plus_minus(self, rep):
        one_added_one_taken_rep = list(rep)

        index_of_0 = [i for i in range(len(rep)) if rep[i] == 0]

        if len(index_of_0) == 0:
            return rep

        added_index = random.choice(index_of_0)
        one_added_one_taken_rep[added_index] = 1

        index_of_1 = [i for i in range(len(rep)) if one_added_one_taken_rep[i] == 1]
        removed_index = random.choice(index_of_1)
        one_added_one_taken_rep[removed_index] = 0

        return tuple(one_added_one_taken_rep)

    def get_one_of_rep_plus_and_rep_minus(self, rep):
        flipped_rep = list(rep)
        index_of_flipped = random.randint(0, len(rep)-1)

        flipped_rep[index_of_flipped] = 1 - rep[index_of_flipped]

        return tuple(flipped_rep)
