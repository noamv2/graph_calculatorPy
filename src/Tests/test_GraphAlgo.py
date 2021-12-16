from unittest import TestCase
from src.imp.DiGraph import DiGraph
from src.imp.Dijkstra import Dijkstra
from src.imp.Edge import Edge
from src.imp.GraphAlgo import GraphAlgo
from src.imp.Node import Node


class TestGraphAlgo(TestCase):

    def setUp(self):
        self.graph = DiGraph("../../data/Gtest.json")
        self.algo = GraphAlgo(self.graph)

        self.graph0 = DiGraph("../../data/A0.json")
        self.algo0 = GraphAlgo(self.graph0)

        self.graph1 = DiGraph("../../data/A1.json")
        self.algo1 = GraphAlgo(self.graph1)

        self.graph2 = DiGraph("../../data/A2.json")
        self.algo2 = GraphAlgo(self.graph2)

        # self.graph3 = DiGraph("../../data/A3.json")
        # self.algo3 = GraphAlgo(self.graph3)
        #
        # self.graph4 = DiGraph("../../data/A4.json")
        # self.algo4 = GraphAlgo(self.graph4)

        self.graph5 = DiGraph("../../data/A5.json")
        self.algo5 = GraphAlgo(self.graph5)
        #
        self.graph1000 = DiGraph("../../data/1000Nodes.json")
        self.algo1000 = GraphAlgo(self.graph1000)
        #
        # self.graph10000 = DiGraph("../../data/10000Nodes.json")
        # self.algo10000 = GraphAlgo(self.graph10000)
        #
        # self.graph10000notCon = DiGraph("../../data/10000Nodes_notcon.json")
        # self.algo10000notCon = GraphAlgo(self.graph10000notCon)

        # self.graph100000 = DiGraph("../../data/100000.json")
        # self.algo100000 = GraphAlgo(self.graph100000)

    def test_get_graph(self):
        self.assertIsNotNone(self.algo.get_graph())
        self.assertIsNotNone(self.algo1.get_graph())
        self.assertIsNotNone(self.algo1000.get_graph())
        self.assertIsNotNone(self.algo5.get_graph())

    def test_save_to_json(self):
        self.algo.save_to_json("testG.json")
        # self.algo.load_from_json("testG.json")




    def test_shortest_path(self):
        self.assertEqual(self.algo.shortest_path(1, 2)[0], 45)
        self.assertEqual(self.algo.shortest_path(1, 3)[0], 45)
        self.assertEqual(self.algo.shortest_path(1, 4)[0], 10)
        self.assertEqual(self.algo.shortest_path(3, 6)[0], 60)
        self.assertEqual(self.algo.shortest_path(1, 5)[0], 25)
        self.assertEqual(self.algo.shortest_path(1, 6)[0], 55)
        self.assertEqual(self.algo.shortest_path(4, 3)[0], 45)
        self.assertEqual(self.algo1000.shortest_path(1, 100)[0], 1090.6025677384555)
        self.assertEqual(self.algo10000.shortest_path(14, 2345)[0], 830.6354147999858)

    def test_center(self):
        self.assertEqual(self.algo.centerPoint()[0], 4)
        self.assertEqual(self.algo0.centerPoint()[0], 7)
        self.assertEqual(self.algo1.centerPoint()[0], 8)
        self.assertEqual(self.algo5.centerPoint()[0], 40)
        self.assertEqual(self.algo1000.centerPoint()[0], 362)
        # self.assertEqual(self.algo10000.centerPoint()[0], 3846)

    def test_TSP(self):
        # lst = [6, 2, 4]
        # ans = self.algo.TSP(lst)
        # for i in range(len(ans)):
        #     ans[i] = ans[i].get__id()
        # self.assertEqual(ans.__str__(), "[6, 5, 2, 4]")
        #
        # lst = [1, 6, 3, 4]
        # ans = self.algo.TSP(lst)
        # for i in range(len(ans)):
        #     ans[i] = ans[i].get__id()
        # self.assertEqual(ans.__str__(), "[1, 4, 5, 6, 5, 2, 3]")
        #
        # lst = [16, 14]
        # self.algo1.graph.remove_node(1)
        # self.algo1.graph.remove_node(15)
        # ans = self.algo1.TSP(lst)
        # self.assertIsNone(ans)

        lst = []
        for i in range(10):
            lst.append(i * 100)

        print(self.algo1000.TSP(lst))

    @staticmethod
    def calculator(algo: GraphAlgo, ans: list, citis: list):
        dist = 0
        for i in range(len(ans) - 1):
            dist += algo.graph.adjList[str(ans[i].get__id())].outEdges[str(ans[i + 1].get__id())].w
            if ans[i].get__id() in citis:
                citis.remove(ans[i].get__id())
        if ans[len(ans) - 1].get__id() in citis:
            citis.remove(ans[len(ans) - 1].get__id())
        if len(citis) != 0:
            return -1
        return dist
