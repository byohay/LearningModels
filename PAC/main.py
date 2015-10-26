from LearningModels.PAC.PAC_Algorithm import PAC_Algorithm
from LearningModels.PAC.PAC_oracle import PAC_Oracle
from LearningModels.conjunction import Conjunction
from LearningModels.uniform_distribution import UniformDistribution

__author__ = 'yben_000'


def main():
    length = 10
    concept = Conjunction(length)
    function = concept.get_ideal_function()
    distribution = UniformDistribution(concept, length)

    pac_oracle = PAC_Oracle(concept, distribution)
    pac_alg = PAC_Algorithm(pac_oracle, length)

    hypo = pac_alg.learn_ideal_function(0.5, 0.1)

    print "FUNC IS: " + str(function)
    print "HYPO IS: " + str(hypo)

if __name__ == "__main__":
    main()