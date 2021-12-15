import math
from typing import List
import heapq as hp
from DiGraph import DiGraph

from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph):
        self.graph = g

    def get_graph(self):
        return self.graph

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        src = id1
        dest = id2
        # get the number of nodes from the graph
        size = self.graph.v_size()

        # create and initialize distance and prev lists, we return these as the result
        distances = [math.inf] * size
        prev = [None] * size

        # create a list that keep track of visited nodes
        visited = [False] * size
        # and a queue based on heap
        que = []
        hp.heappush(que, (0, src))  # add the source with distance 0 (to itself)

        while not que:
            # pop the smallest vertex
            dis, u = hp.heappop(que)
            visited[u] = True  # mark the node as visited

            # traverse U's neighbours
            edges = self.graph.all_out_edges_of_node(self.graph.get_node(u))

            for ID, w in edges.items():
                if not visited[int(ID)]:
                    altDis = dis + w  # compute the distance to U + dis(u,v)
                    if altDis < distances[int(ID)]:
                        distances[int(ID)] = altDis
                        prev[int(ID)] = u
                        hp.heappush(que, (altDis, int(ID)))  # requeue v with the new priority

        return distances[dest], self.getPath(prev, src, dest)

    def plot_graph(self) -> None:
        pass

    def load_from_json(self, file_name: str) -> bool:
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):

        # calculate the eccentricity of each node
        eccentricity = {}  # saving the eccentricity of each node
        for node in self.graph.get_all_v():
            pass





    def plot_graph(self) -> None:
        pass

    @staticmethod
    def getPath(prev: dict, src, dest):

        path = [dest]
        while dest != src:
            dest = prev[dest]
            path.insert(0, dest)

        path.insert(0, src)

        return path
