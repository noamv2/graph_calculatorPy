import heapq as hp
import math
from DiGraph import DiGraph


class Dijkstra:

    def __init__(self, graph: DiGraph):
        self.graph = graph

    def shp(self, src: int):

        # get the number of nodes from the graph
        size = self.graph.v_size()
        nodes = self.graph.get_all_v()
        # create and initialize distance and prev dicts, we return these as the result
        distances = {}
        prev = {}
        # create a list that keep track of visited nodes
        visited = {}

        for k, v in nodes.items():
            visited[k] = False
            distances[k] = math.inf
            prev[k] = None

        distances[src] = 0

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
                if not visited[ID]:
                    altDis = dis + w.get_w()  # compute the distance to U + dis(u,v)
                    if altDis < distances[ID]:
                        distances[ID] = altDis
                        prev[ID] = u
                        hp.heappush(que, (altDis, ID))  # requeue v with the new priority

            return prev, distances
