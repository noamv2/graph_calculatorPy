from unittest import TestCase

from src.imp.DiGraph import DiGraph

d = DiGraph("../../data/A0.json")


class TestDiGraph(TestCase):

    def test_get_node(self):
        self.assertTrue(d.get_node(4).get__id() == 4)
        self.assertTrue(d.get_node(2).get__id() == 2)
        self.assertTrue(d.get_node(8).get__id() == 8)
        self.assertTrue(d.get_node(15) is None)

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
        self.assertTrue(d.get_all_v().keys().__str__() == "dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])")
        d.add_node(15, (32, 35))
        self.assertTrue(d.get_all_v().keys().__str__() == "dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])")
        d.remove_node(15)
        self.assertTrue(d.get_all_v().keys().__str__() == "dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])")

    def test_all_in_edges_of_node(self):
        self.assertTrue(d.all_in_edges_of_node(3).keys().__str__() == "dict_keys(['2', '4'])")
        d.add_edge(1, 3, 10)
        self.assertTrue(d.all_in_edges_of_node(3).keys().__str__() == "dict_keys(['2', '4', '1'])")
        d.remove_edge(1, 3)
        self.assertTrue(d.all_in_edges_of_node(3).keys().__str__() == "dict_keys(['2', '4'])")

    def test_all_out_edges_of_node(self):
        self.assertTrue(d.all_out_edges_of_node(3).keys().__str__() == "dict_keys(['2', '4'])")
        d.add_edge(3, 1, 10)
        self.assertTrue(d.all_out_edges_of_node(3).keys().__str__() == "dict_keys(['2', '4', '1'])")
        d.remove_edge(3, 1)
        self.assertTrue(d.all_out_edges_of_node(3).keys().__str__() == "dict_keys(['2', '4'])")

    def test_get_mc(self):
        self.assertTrue(d.mc == 0)
        d.add_edge(3, 1, 10)
        self.assertTrue(d.mc == 1)
        d.remove_edge(3, 1)
        self.assertTrue(d.mc == 2)
        d.add_node(15, (32, 35))
        self.assertTrue(d.mc == 3)
        d.remove_node(15)
        self.assertTrue(d.mc == 4)

    def test_add_edge(self):
        self.assertTrue(d.add_edge(3, 1, 10))
        self.assertFalse(d.add_edge(3, 1, 15))

    def test_add_node(self):
        self.assertTrue(d.add_node(15, (32, 35)))
        self.assertFalse(d.add_node(15, (32, 35)))

    def test_remove_node(self):
        self.assertFalse(d.remove_node(15))
        d.add_node(15, (32, 35))
        self.assertTrue(d.remove_node(15))

    def test_remove_edge(self):
        self.assertFalse(d.remove_edge(3, 1))
        d.add_edge(3, 1, 10)
        self.assertTrue(d.remove_edge(3, 1))
