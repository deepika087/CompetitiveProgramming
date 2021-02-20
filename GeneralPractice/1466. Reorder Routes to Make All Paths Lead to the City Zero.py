__author__ = 'deepika'

"""
Success
Details
Runtime: 1048 ms, faster than 100.00% of Python online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
Memory Usage: 43.1 MB, less than 100.00% of Python online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
"""
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        return self.startDfs(connections)

    def findNeighbours(self, connections):
        graph = {}
        for connection in connections:
            if connection[0] in graph:
                graph[connection[0]].append([connection[1], True])
            else:
                graph[connection[0]] = [ [connection[1], True] ]

            if connection[1] in graph:
                graph[connection[1]].append([connection[0], False])
            else:
                graph[connection[1]] = [ [connection[0], False] ]

        return graph

    def startDfs(self, connections):
        graph = self.findNeighbours(connections)
        stack = []
        stack.append(0)
        count = 0
        visited = set()

        while len(stack) > 0:
            popped = stack.pop()

            if popped not in visited:
                neighbours = graph[popped]

                for neighbour in neighbours:
                    if neighbour[0] not in visited:
                        if neighbour[1]: # If isforward
                            count = count + 1

                    stack.append(neighbour[0])
                visited.add(popped)
        return count

s=Solution()
print(s.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(s.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
print(s.minReorder(n = 3, connections = [[1,0],[2,0]]))