import cProfile
import logging
import math
from typing import List
import heapq as hp
from src.imp.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
import json


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph):
        self.graph = g

    def get_graph(self):
        return self.graph

    def save_to_json(self, file_name: str) -> bool:
        try:
        nodes = json.dumps(list(self.graph.get_all_v().values()), default=lambda o: o.__dict__, sort_keys=True,indent=4)
        lstN = json.loads(nodes)
        for d in lstN:
            del d["tag"]

        lstE = []
        for node in self.graph.get_all_v().values():
            for edge in self.graph.all_out_edges_of_node(node.get__id()).values():
                lstE.append(edge)

        edges = json.dumps(lstE, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        lstEd = json.loads(edges)

        dic = {"Edges": lstEd, "Nodes": lstN}
        s = json.dumps(dic, indent=4)

        with open(file_name, 'w') as f:
            f.write(s)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        prev, distances = self.dijkstra(id1)
        return distances[id2], self.getPath(prev, id1, id2)

    def plot_graph(self) -> None:
        pass

    def load_from_json(self, file_name: str) -> bool:
        try:
            self.graph = DiGraph(file_name)

        except Exception as e:
            logging.exception(e)
            return False

        return True

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        minDist = dist = math.inf
        minAns = []
        citisMap = {}
        dijkstraMap = {}

        for ind in node_lst:
            src = self.graph.get_node(ind)
            for n in node_lst:
                citisMap[n] = self.graph.get_node(n)
            dist = 0
            ans = [src]
            del citisMap[ind]
            while len(citisMap) > 0:
                minNei = None
                minWeight = math.inf
                dijkstra = {}
                if src.get__id() in dijkstraMap:
                    dijkstra = dijkstraMap[src.get__id()]
                else:
                    dijkstra = self.dijkstra(src.get__id())
                    dijkstraMap[src.get__id()] = dijkstra
                distance = dijkstra[1]
                path = dijkstra[0]
                for nodeData in citisMap.values():
                    if distance[nodeData.get__id()] < minWeight:
                        minNei = nodeData
                        minWeight = distance[nodeData.get__id()]
                if minNei is None:
                    return None
                dist += distance[minNei.get__id()]
                ans.append(self.graph.get_node(minNei.get__id()))
                del citisMap[minNei.get__id()]
                node = path[minNei.get__id()]
                size = len(ans) - 1
                while node != src.get__id():
                    ans.insert(size, self.graph.get_node(int(node)))
                    if node in citisMap:
                        del citisMap[int(node)]
                    # if node in path:
                    node = path[node]
                src = minNei
            if dist < minDist:
                minAns = ans
                minDist = dist
        return minAns

    def centerPoint(self) -> (int, float):

        # calculate the eccentricity of each node
        eccentricity = {}  # saving the eccentricity of each node
        for node in self.graph.get_all_v().values():
            distance = self.dijkstra(node.get__id())[1]
            max_value = max(distance.values())
            eccentricity[node.get__id()] = max_value
        min_value = min(eccentricity.values())
        ind = list(eccentricity.keys())[list(eccentricity.values()).index(min_value)]
        return ind, min_value

    def plot_graph(self) -> None:
        pass

    @staticmethod
    def getPath(prev: dict, src, dest):

        path = []
        while dest != src:
            path.insert(0, dest)
            dest = prev[dest]

        path.insert(0, src)

        return path

    def dijkstra(self, src: int) -> (dict, dict):
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
        prev[src] = src

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

    # def main(self):


if __name__ == '__main__':
    g = DiGraph("../../data/1000Nodes.json");
    alg = GraphAlgo(g)
    alg.TSP()
    cProfile.run('alg.')
