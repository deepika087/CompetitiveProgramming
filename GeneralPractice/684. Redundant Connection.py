__author__ = 'deepika'

"""
Details
Runtime: 52 ms, faster than 29.64% of Python online submissions for Redundant Connection.
Memory Usage: 14.2 MB, less than 29.09% of Python online submissions for Redundant Connection.
"""
class DSU:
    def __init__(self, N):
        self.par = range(N+1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr: # it means this edge is not practically required.
            return  False
        self.par[xr] = yr # This edge is required to connect the two disconnected component.
        return True

class Solution(object):

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        N = len(edges)
        if N == 0:
            return 0

        dsu = DSU(N)
        print(edges)

        for edge in edges:
            #print("Union of : ", edge[0], edge[1])
            if not dsu.union(dsu.find(edge[0]), dsu.find(edge[1])):
                return edge

s=Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))