from unittest import TestCase
from src.imp.DiGraph import DiGraph
from src.imp.Dijkstra import Dijkstra
from src.imp.GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):

    def test_shortest_path(self):

        d = DiGraph("../../data/Gtest.json")
        algo = Dijkstra(d)

        a = algo.shp(1)
        print("")


