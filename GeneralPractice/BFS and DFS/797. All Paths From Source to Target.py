__author__ = 'deepika'

"""
Runtime: 92 ms, faster than 70.99% of Python online submissions for All Paths From Source to Target.
Memory Usage: 13.9 MB, less than 99.46% of Python online submissions for All Paths From Source to Target.
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        results = []
        path = []

        self.allPathsSourceTargetUtil(0, path, results, graph)
        return results


    def allPathsSourceTargetUtil(self, startNode, path, results, graph):
        if startNode == len(graph) - 1:
            results.append(path + [startNode])
        else:
            for neighbour in graph[startNode]:
                self.allPathsSourceTargetUtil(neighbour, path + [startNode], results, graph)

s=Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))