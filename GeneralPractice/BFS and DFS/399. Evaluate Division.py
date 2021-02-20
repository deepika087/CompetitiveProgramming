__author__ = 'deepika'


class Graph:
    def __init__(self):
        self.nodes = dict()

    def __repr__(self):
        return str(self.nodes)

class Node:
    def __init__(self):
        self.edges = dict()

    def handleEdge(self, tn, v):
        self.edges[tn] = v

    def contains(self, t):
        return t in self.edges

    def fetchEdge(self, t):
        return self.edges[t]

    def __repr__(self):
        return str(self.edges)


class Solution(object):
    def __init__(self):
        self.g = Graph()

    def handleRepresentation(self, equations, values):

        for i in range(len(equations)):
            eq = equations[i]
            if eq[0] not in self.g.nodes:
                self.g.nodes[eq[0]] = Node()
            self.g.nodes[eq[0]].handleEdge(eq[1], values[i])

            if eq[1] not in self.g.nodes:
                self.g.nodes[eq[1]] = Node()
            self.g.nodes[eq[1]].handleEdge(eq[0], round(float(1/values[i]), 2))



    def calcEquation(self, equations, values, queries):
        self.handleRepresentation(equations, values)
        print(self.g)
        result = []

        for q in queries:
            print(q)
            if q[0] not in self.g.nodes or q[1] not in self.g.nodes:
                result.append(-1.0)
            elif q[0] == q[1]:
                result.append(1.0)
            elif q[0] in self.g.nodes and self.g.nodes[q[0]].contains(q[1]):
                print(self.g.nodes[q[0]]) #:
                result.append(self.g.nodes[q[0]].fetchEdge([q[1]]))
            else:
                print("not handled yet")




s=Solution()
print(s.calcEquation(equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ] ))


