import json
from abc import ABC

from Node import Node
from Edge import Edge
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface, ABC):

    def __init__(self, file_name):
        self.mc = 0
        adjList = dict
        nodes = dict
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
                adjList[n_id] = Container(node)
                nodes[n_id] = node

            for edgeData in edgesL:
                edgeDataD = dict(edgeData)
                src=edgeDataD["src"]
                dest = edgeDataD["dest"]
                weight = edgeDataD["weight"]
                edge=Edge(src,weight,dest)
                Container(adjList[src]).outEdges[dest]=edge
                Container(adjList[dest]).inEdges[src] = edge





        # else:


if __name__ == '__main__':
    print("")
    DiGraph("../../data/A0.json")


class Container:
    def __init__(self, node):
        self.node = node
        self.outEdges = dict
        self.inEdges = dict
