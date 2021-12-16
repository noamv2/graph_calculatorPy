import json
from abc import ABC

from src.imp.Edge import Edge
from src.GraphInterface import GraphInterface
from src.imp.Node import Node


class Container:
    def __init__(self, node):
        self.node = node
        self.outEdges = {}
        self.inEdges = {}


class DiGraph(GraphInterface, ABC):

    def __init__(self, file_name):
        self.mc = 0
        adjList = {}
        nodes = {}
        if file_name != "":
            with open(file_name, "r") as f:
                dict2 = json.load(f)
            edgesL = list(dict2.get('Edges'))
            nodesL = list(dict2.get('Nodes'))

            for nodeData in nodesL:
                nodeDataD = dict(nodeData)
                n_id = nodeDataD["id"]
                n_pos = nodeDataD["pos"]
                node = Node(n_id, n_pos)
                adjList[str(n_id)] = Container(node)
                nodes[n_id] = node

            for edgeData in edgesL:
                edgeDataD = dict(edgeData)
                src = edgeDataD["src"]
                dest = edgeDataD["dest"]
                weight = edgeDataD["w"]
                edge = Edge(src, weight, dest)
                adjList[str(src)].outEdges[str(dest)] = edge
                adjList[str(dest)].inEdges[str(src)] = edge

        self.adjList = adjList
        self.nodes = nodes

    def get_node(self, node_id):
        if node_id not in self.nodes:
            return
        return self.nodes[node_id]

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        size = 0
        for container in self.adjList.values():
            size += len(container.outEdges)

        return size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.adjList[str(id1)].inEdges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.adjList[str(id1)].outEdges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes and str(id2) not in self.adjList[str(id1)].outEdges:
            edge = Edge(id1, weight, id2)
            self.adjList[str(id1)].outEdges[str(id2)] = edge
            self.adjList[str(id2)].inEdges[str(id1)] = edge
            self.mc += 1
            return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            node = Node(node_id, [pos[0], pos[1], 0.0])
            self.adjList[str(node_id)] = Container(node)
            self.nodes[node_id] = node
            self.mc += 1
            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            outE = list(self.adjList[str(node_id)].outEdges.keys())
            inE = list(self.adjList[str(node_id)].inEdges.keys())
            for i in outE:
                self.remove_edge(node_id, i)
            for i in inE:
                self.remove_edge(i, node_id)

            del self.adjList[str(node_id)]
            del self.nodes[node_id]
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if str(node_id2) in self.adjList[str(node_id1)].outEdges:
            del self.adjList[str(node_id1)].outEdges[str(node_id2)]
            del self.adjList[str(node_id2)].inEdges[str(node_id1)]
            self.mc += 1
            return True
        return False


if __name__ == '__main__':
    d = DiGraph("../../data/A0.json")
    print("")
