import unittest

from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import MonotoneConjunctionNeighborhood
from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood_output_one import \
    ConjunctionNeighborhoodOutputOne

__author__ = 'yben_000'


class TestNeighborsFinder(unittest.TestCase):
    def setUp(self):
        self.neighbors_finder = MonotoneConjunctionNeighborhood()
        self.neighbor_getter = ConjunctionNeighborhoodOutputOne()

    def test_find_for_zero(self):
        neighbors = set()

        neighbors.add((0, 0, 0, 0, 0))
        neighbors.add((1, 0, 0, 0, 0))
        neighbors.add((0, 1, 0, 0, 0))
        neighbors.add((0, 0, 1, 0, 0))
        neighbors.add((0, 0, 0, 1, 0))
        neighbors.add((0, 0, 0, 0, 1))

        self.assertEqual(neighbors, self.neighbors_finder.get_neighborhood_of_rep((0, 0, 0, 0, 0)))
        self.assertIn(self.neighbor_getter.get_one_of_neighborhood_of_rep((0, 0, 0, 0, 0)), neighbors)

    def test_find_for_other(self):
        neighbors = set()

        neighbors.add((0, 0, 0, 0, 0))

        neighbors.add((1, 0, 0, 0, 0))
        neighbors.add((0, 1, 0, 0, 0))
        neighbors.add((0, 0, 1, 0, 0))
        neighbors.add((0, 0, 0, 1, 0))
        neighbors.add((0, 0, 0, 0, 1))

        neighbors.add((1, 0, 1, 0, 0))
        neighbors.add((0, 1, 1, 0, 0))
        neighbors.add((0, 0, 1, 1, 0))
        neighbors.add((0, 0, 1, 0, 1))

        self.assertEqual(neighbors, self.neighbors_finder.get_neighborhood_of_rep((0, 0, 1, 0, 0)))
        self.assertIn(self.neighbor_getter.get_one_of_neighborhood_of_rep((0, 0, 1, 0, 0)), neighbors)

    def test_find_for_another_one(self):
        neighbors = set()

        neighbors.add((1, 1, 1, 1, 0))

        neighbors.add((1, 1, 1, 0, 1))
        neighbors.add((1, 1, 0, 1, 1))
        neighbors.add((1, 0, 1, 1, 1))
        neighbors.add((0, 1, 1, 1, 1))

        neighbors.add((1, 1, 1, 0, 0))
        neighbors.add((1, 1, 0, 1, 0))
        neighbors.add((1, 0, 1, 1, 0))
        neighbors.add((0, 1, 1, 1, 0))
        neighbors.add((1, 1, 1, 1, 1))

        self.assertEqual(neighbors, self.neighbors_finder.get_neighborhood_of_rep((1, 1, 1, 1, 0)))
        self.assertIn(self.neighbor_getter.get_one_of_neighborhood_of_rep((1, 1, 1, 1, 0)), neighbors)

    def test_find_for_unique(self):
        neighbors = set()

        neighbors.add((1, 0))
        neighbors.add((0, 1))
        neighbors.add((0, 0))
        neighbors.add((1, 1))

        self.assertEqual(neighbors, self.neighbors_finder.get_neighborhood_of_rep((0, 1)))
        self.assertIn(self.neighbor_getter.get_one_of_neighborhood_of_rep((0, 1)), neighbors)
