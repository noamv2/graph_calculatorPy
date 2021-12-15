import heapq as hp
import math
from DiGraph import DiGraph


class Dijkstra:

    def __init__(self, graph: DiGraph):
        self.graph = graph

    def shp(self, src: int):
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

            return prev, distances
