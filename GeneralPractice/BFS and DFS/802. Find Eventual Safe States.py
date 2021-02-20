__author__ = 'deepika'

"""
Runtime: 648 ms, faster than 77.78% of Python online submissions for Find Eventual Safe States.
Memory Usage: 19.6 MB, less than 81.67% of Python online submissions for Find Eventual Safe States.

TLE: 101 / 111 test cases passed. - the issue was the local visited. Had to make it shared across all calls
"""
class Solution(object):
    def eventualSafeNodes(self, graph):


        if len(graph) == 0:
            return []

        safeNodes = [False for _ in range(len(graph))]
        visited = [False for _ in range(len(graph))]
        for i in range(0, len(graph)):

            if safeNodes[i]:
                continue

            res = self.startDFS(i, graph, visited, safeNodes)
            if res:
                safeNodes[i] = True

        result = []
        for i in range(len(safeNodes)):
            if safeNodes[i]:
                result.append(i)
        return result

    def startDFS(self, startNode, graph, visited, safeNodes):

        if safeNodes[startNode]:
            return True

        if visited[startNode]:
            return False

        visited[startNode] = True
        for node in graph[startNode]:
            if not self.startDFS(node, graph, visited, safeNodes):
                return False
            else:
                safeNodes[node] = True
        visited[startNode] = False
        return True

s=Solution()
print(s.eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))
print(s.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))