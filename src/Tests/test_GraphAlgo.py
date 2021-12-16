from unittest import TestCase
from src.imp.DiGraph import DiGraph
from src.imp.Dijkstra import Dijkstra
from src.imp.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self):
        self.d = DiGraph("../../data/Gtest.json")
        self.algo = GraphAlgo(self.d)

    def test_shortest_path(self):
        print(self.algo.shortest_path(1,2))
        self.assertTrue(self.algo.shortest_path(1, 2)[0] == 45)
        self.assertEqual(self.algo.shortest_path(4, 3)[0] , 45)

    def test_center(self):
        print(self.algo.centerPoint())
