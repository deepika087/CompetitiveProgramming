__author__ = 'deepika'


"""
Edge coloring problem.
https://www.geeksforgeeks.org/edge-coloring-of-a-graph/?ref=rp

Use BFS traversal to start traversing the graph.
Pick any vertex and give different colors to all of the edges connected to it, and mark those edges as colored.
Traverse one of it's edges.
Repeat step to with a new vertex until all edges are colored.

"""


class Graph:

    def __init__(self):
        self.dict = {}

    def insertEdge(self, a, b, id):
        if a not in self.dict:
            self.dict[a] = []
        self.dict[a].append( [b, id] )

        if b not in self.dict:
            self.dict[b] = []
        self.dict[b].append( [a, id] )

    def startColoring(self):
        print(self.dict)

        visited = set()
        colored = set()
        edgeColors = dict()
        colored.add(0)
        self.startBFS(0, visited, edgeColors)
        print(edgeColors)

    def startBFS(self, index, visited, edgeColors):

        q = []
        q.append(index)
        while len(q) > 0:
            nextLevel = []

            while len(q) > 0 :
                col = 0
                colored = set() # It should be a local variable not a global one.
                popped = q.pop()

                for neighbour in self.dict.get(popped, []):
                    if neighbour[0] not in visited:
                        nextLevel.append( neighbour[0] )

                    if neighbour[1] not in edgeColors:
                        while col in colored:    # Basically we are selecting a new color.
                            col += 1
                        edgeColors[neighbour[1]] = col
                        colored.add(col)
                        col += 1
                    else:
                        colored.add(edgeColors[neighbour[1]])

                visited.add(popped)
            q = nextLevel

g=Graph()
g.insertEdge(0, 1, 0)
g.insertEdge(1, 2, 1)
g.insertEdge(2, 3, 2)
g.insertEdge(3, 0, 3)

g.startColoring()