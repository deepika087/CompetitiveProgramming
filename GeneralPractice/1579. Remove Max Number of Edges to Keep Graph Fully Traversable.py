__author__ = 'deepika'

"""
Details
Runtime: 2224 ms, faster than 33.33% of Python online submissions for Remove Max Number of Edges to Keep Graph Fully Traversable.
Memory Usage: 61.4 MB, less than 66.67% of Python online submissions for Remove Max Number of Edges to Keep Graph Fully Traversable.
"""
class DSU:
    def __init__(self, N):
        self.p = range(N+1)
        self.cmp = N

    def find(self, x):

        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)

        if xr == yr:
            return True
        self.p[xr] = yr
        self.cmp -= 1
        return False

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """


        N = len(edges)

        d1 = DSU(n)
        d2 = DSU(n)

        count = 0
        for edge in edges:

            if edge[0] == 3: # Biderectional
                if d1.union(edge[1], edge[2]): #Already connected
                    count += 1
                d2.union(edge[1], edge[2])

            if edge[0] == 2:
                if d1.union(edge[1], edge[2]):
                    count += 1

        for edge in edges:
            if edge[0] == 1:
                if d2.union(edge[1], edge[2]):
                    count += 1

        if d1.cmp != 1 or d2.cmp != 1:
            return -1
        return count

s=Solution()
print(s.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
print(s.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
print(s.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))