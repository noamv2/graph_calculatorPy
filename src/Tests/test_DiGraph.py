from unittest import TestCase

from src.imp.DiGraph import DiGraph

d = DiGraph("../../data/A0.json")


class TestDiGraph(TestCase):
    # d = DiGraph("../../data/A0.json")
    # @classmethod
    # def setUpClass(cls):
    #     d = DiGraph("../../data/A0.json")
    # cls._connection = createExpensiveConnectionObject()

    def test_get_node(self):
        self.assertTrue(d.get_node(4).get__id() == 4)
        self.assertTrue(d.get_node(2).get__id() == 2)
        self.assertTrue(d.get_node(8).get__id() == 8)
        self.assertTrue(d.get_node(15) == None)

    def test_v_size(self):
        self.assertTrue(d.v_size() == 11)
        d.add_node(15, (32, 35))
        self.assertTrue(d.v_size() == 12)
        d.remove_node(15)
        self.assertTrue(d.v_size() == 11)

    def test_e_size(self):
        # d = DiGraph("../../data/A0.json")
        self.assertTrue(d.e_size() == 22)
        d.add_edge(1, 3, 10)
        self.assertTrue(d.e_size() == 23)
        d.remove_edge(1, 3)
        self.assertTrue(d.e_size() == 22)

    def test_get_all_v(self):
        print(d.get_all_v())
        # self.assertTrue(d.get_all_v() is d.nodes)

    def test_all_in_edges_of_node(self):
        print(d.all_in_edges_of_node(3).keys())

    def test_all_out_edges_of_node(self):
        print(d.all_out_edges_of_node(3).keys())

    def test_get_mc(self):
        print(d.mc)

    def test_add_edge(self):
        pass

    def test_add_node(self):
        pass

    def test_remove_node(self):
        pass

    def test_remove_edge(self):
        pass
