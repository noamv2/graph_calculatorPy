import json
from abc import ABC

from Node import Node
from src.GraphInterface import GraphInterface


class Digraph(GraphInterface, ABC):

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
                adjList["id"] = Container(node)
                nodes["id"] = node
            for edgeData in edgesL:
                edgeDataD = dict(edgeData)
                src=edgeDataD["src"]
                dest = edgeDataD["dest"]
                weight = edgeDataD["weight"]



        # else:


if __name__ == '__main__':
    print("")
    Digraph("../../data/A0.json")


class Container:
    def __init__(self, node: Node, ):
        self.node = node
        self.outEdges = dict
        self.inEdges = dict
