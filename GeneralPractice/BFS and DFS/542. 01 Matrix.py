__author__ = 'deepika'

import sys
"""
Details
Runtime: 880 ms, faster than 21.93% of Python online submissions for 01 Matrix.
Memory Usage: 17.4 MB, less than 9.92% of Python online submissions for 01 Matrix.

For each matrix[i][j] find the distance to nearest 0
"""
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(matrix)
        n = len(matrix[0])

        dist = [ [ sys.maxint for i in range(n)] for j in range(m)]

        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append( (i, j) )
                    dist[i][j] = 0

        while queue:
            popped = queue.pop()
            for dirs in [ [-1, 0], [1, 0], [0, -1], [0, 1]]:
                    newI = popped[0] + dirs[0]
                    newJ = popped[1] + dirs[1]

                    if (newI >= 0 and newJ >= 0 and newI < m and newJ < n):
                        if dist[newI][newJ] > dist[popped[0]][popped[1]] + 1:
                            dist[newI][newJ] = dist[popped[0]][popped[1]] + 1
                            # bcz say matrix is [ [0, 1, 1], [0, 1, 1], [0, 1, 0] ]
                            # now if you at 1, at matrix[0][1] then you need to go futher.
                            # If you only bank on position of 0s in queue then you will never reach that 1.
                            queue.append( (newI, newJ) )
        return dist

s=Solution()
print(s.updateMatrix([[0],[0],[0],[0],[0]]))
print(s.updateMatrix([[0,0,0],
 [0,1,0],
 [0,0,0]]))
print(s.updateMatrix([[0,0,0],
 [0,1,0],
 [1,1,1]]))