__author__ = 'deepika'

"""
Runtime: 72 ms, faster than 68.24% of Python online submissions for Reconstruct Itinerary.
Memory Usage: 13 MB, less than 86.18% of Python online submissions for Reconstruct Itinerary.
"""
class Solution(object):

    def presentation(self, tickets):
        graph = {}
        for t in tickets:
            if t[0] in graph:
                graph[t[0]].append(t[1])
            else:
                graph[t[0]] = [t[1]]

        for t in graph.keys():
            graph[t] = sorted(graph[t])
        return graph

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        graph = self.presentation(tickets)
        maxLen = len(tickets) + 1
        path = ["JFK"]
        self.startDFS("JFK", graph, maxLen, path)
        return path

    def startDFS(self, startNode, graph, maxLen, path):
        if len(path) == maxLen:
            return True

        for _ in range(len(graph.get(startNode, []))):
            popped = graph[startNode].pop(0)

            path.append(popped)

            if (self.startDFS(popped, graph, maxLen, path)):
                return True

            path.pop()
            graph[startNode].append(popped)

s=Solution()
s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
s.findItinerary( [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] )