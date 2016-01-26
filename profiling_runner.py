import cProfile
import pstats
from evolvability.classic_model.monotone_conjunction_algorithm.run_simulation import \
    run_simulation__classical_model

from evolvability.with_population.HGT.run_simulation import\
    HGT_simulations_main__HGT_factor, HGT_simulations_main__population_factor, HGT_simulations_main__mutation_factor, \
    HGT_simulations_main__performance_rate
from evolvability.with_population.recombination.run_simulation import recombination_simulations_main, \
    recombination_simulations_main__population_factor

__author__ = 'yben_000'


def main():
    pr = cProfile.Profile()

    pr.enable()

    for i in xrange(1):
        recombination_simulations_main()
        HGT_simulations_main__HGT_factor()
        run_simulation__classical_model()
    pr.disable()

    pstats.Stats(pr).sort_stats("time").print_stats()

if __name__ == "__main__":
    main()
