import heapq as hp
import math
from src.imp.DiGraph import DiGraph


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

        # and a queue based on heap
        que = []
        hp.heappush(que, (0, src))

        for k, v in nodes.items():
            if k != src:
                visited[k] = False
                distances[k] = math.inf
                prev[k] = None


        distances[src] = 0

        while len(que) > 0:
            # pop the smallest vertex
            dis, u = hp.heappop(que)
            visited[u] = True  # mark the node as visited

            # traverse U's neighbours
            edges = self.graph.all_out_edges_of_node(u)

            for ID, w in edges.items():
                # print(visited[ID])
                if not visited[int(ID)]:
                    altDis = dis + w.get_w()  # compute the distance to U + dis(u,v)
                    if altDis < distances[int(ID)]:
                        distances[int(ID)] = altDis
                        prev[int(ID)] = u
                        hp.heappush(que, (altDis, int(ID)))  # requeue v with the new priority

        return prev, distances
