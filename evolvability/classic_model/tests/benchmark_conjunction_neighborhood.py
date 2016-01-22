import cProfile
import pstats
from LearningModels.evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import \
    MonotoneConjunctionNeighborhood

__author__ = 'Ben'

def test_speed_of_rep_plus_minus():
    pr = cProfile.Profile()
    neighbors_finder = MonotoneConjunctionNeighborhood()

    pr.enable()

    for i in xrange(100):
        neighbors_finder.get_neighborhood_of_rep((1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1,
                                                  1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1))

    pr.disable()

    pstats.Stats(pr).sort_stats("time").print_stats()

if __name__ == "__main__":
    test_speed_of_rep_plus_minus()
