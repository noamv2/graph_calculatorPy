from unittest import TestCase
from src.imp.DiGraph import DiGraph
from src.imp.Dijkstra import Dijkstra
from src.imp.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self):
        self.graph = DiGraph("../../data/Gtest.json")
        self.algo = GraphAlgo(self.graph)

        self.graph0 = DiGraph("../../data/A0.json")
        self.algo0 = GraphAlgo(self.graph0)

        self.graph1 = DiGraph("../../data/A1.json")
        self.algo1 = GraphAlgo(self.graph1)
        #
        self.graph2 = DiGraph("../../data/A2.json")
        self.algo2 = GraphAlgo(self.graph2)

        self.graph5 = DiGraph("../../data/A5.json")
        self.algo5 = GraphAlgo(self.graph5)

    def test_shortest_path(self):
        print(self.algo.shortest_path(1,2))
        self.assertTrue(self.algo.shortest_path(1, 2)[0] == 45)
        self.assertEqual(self.algo.shortest_path(4, 3)[0] , 45)

    def test_center(self):
        print(self.algo.centerPoint())
        print(self.algo0.centerPoint())
        print(self.algo1.centerPoint())
        print(self.algo2.centerPoint())
        print(self.algo5.centerPoint())

    def test_TSP(self):
        print(self.algo.TSP([4,2,6]))
