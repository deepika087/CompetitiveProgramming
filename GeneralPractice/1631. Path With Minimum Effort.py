__author__ = 'deepika'

import sys
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        m = len(heights)
        n = len(heights[0])
        efforts = [ [sys.maxint for i in range(n)] for j in range(m)]

        efforts[0][0] = heights[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                efforts[i][j] = min(efforts[i][j], abs( heights[i][j] - max (heights[i-1][j] if i-1>=0 else -sys.maxint,
                                    heights[i][j-1] if j-1 >= 0 else -sys.maxint,
                                    heights[i+1][j] if i+1 < m else -sys.maxint,
                                    heights[i][j+1] if j+1 < n else -sys.maxint) ) )

        print(efforts)
        return efforts[m-1][n-1]

s=Solution()
print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))