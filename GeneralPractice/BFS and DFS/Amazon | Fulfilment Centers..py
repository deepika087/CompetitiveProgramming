__author__ = 'deepika'


"""
My idea is that you are given a graph. First find any node with indegree equal to 0.
Now, start traversin in DFS fashion. just like you would to find cameras for Binary Tree.
"""

class Graph:
    pass

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


class Solution:

    def getUnique(self, cities):
        result = set()
        graph = dict()

        for data in cities:
            result.add(data[0])
            result.add(data[1])

            if data[0] not in graph:
                graph[data[0]] = []
            graph[data[0]].append(data[1])

        return result, graph

    def find(self, subsets, node):
        if subsets[node].parent != node:
            subsets[node].parent = self.find(subsets, subsets[node].parent)
        return subsets[node].parent

    def find1(self, subsets, city):

        while subsets[city].parent != city:
            subsets[city].parent = self.find(subsets, subsets[city].parent)
        return subsets[city].parent

    def union(self, subsets, u, v):

        # Attach smaller rank tree under root
        # of high rank tree(Union by Rank)
        if subsets[u].rank > subsets[v].rank:
            subsets[v].parent = u
        elif subsets[v].rank > subsets[u].rank:
            subsets[u].parent = v

        # If ranks are same, then make one as
        # root and increment its rank by one
        else:
            subsets[v].parent = u
            subsets[u].rank += 1

    def findMinimumSpanningTree(self, uniqueCities, graph):

        subsets = dict()

        for city in uniqueCities:
            subsets[city] = Subset(city, 0)


        for city in uniqueCities:
            u_repr = self.find(subsets, city)

            if city in graph:
                for neighbour in graph[city]:
                    v_repr = self.find(subsets, neighbour)

                    if u_repr == v_repr:
                        # remove this edge
                        graph[city].remove(neighbour)

                        if len(graph[city]) == 0 :
                            del graph[city]

                    else:
                        print("Merging: ", u_repr, " with ", v_repr)
                        self.union(subsets, u_repr, v_repr)

        print(graph)

    def findFulfillmentCenters(self, cities):

        uniqueCities, graph = self.getUnique(cities)

        self.findMinimumSpanningTree(uniqueCities, graph)



s=Solution()
s.findFulfillmentCenters([
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'A'],
    ['C', 'D']
])