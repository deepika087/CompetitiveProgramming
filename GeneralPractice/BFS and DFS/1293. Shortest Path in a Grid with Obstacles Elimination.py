__author__ = 'deepika'


"""
correct approach is BFS. It gives TLE in DFS approach.

BFS approach
Runtime: 760 ms, faster than 25.00% of Python online submissions for Shortest Path in a Grid with Obstacles Elimination.
Memory Usage: 22.7 MB, less than 19.12% of Python online submissions for Shortest Path in a Grid with Obstacles Elimination.
"""
import sys
class Solution(object):
    def __init__(self):
        self.minPathCount = sys.maxint

    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        dist = self.startBFS(0, 0, grid, m, n, k)
        return dist

        #self.startDFS(0, 0, grid, k, 0, 0)

    def startBFS(self, i, j, grid, m, n, k):

        queue = [  ]
        queue.append( [ i, j, k ] )
        dist = 1
        visited = {(0, 0, k)}

        while queue:
            nextLevel = []

            while queue:
                startI, startJ, obst = queue.pop()

                if startI == m - 1 and startJ == n - 1:
                    return dist

                for dir in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    newX = startI + dir[0]
                    newY = startJ + dir[1]

                    if 0 <= newX < m and 0 <= newY < n:
                        key = (newX, newY, obst)
                        if key not in visited:
                            if grid[newX][newY] == 1 and obst > 0:
                                nextLevel.append([newX, newY, obst - 1] )
                                visited.add(key)
                            elif grid[newX][newY] == 0:
                                nextLevel.append([newX, newY, obst] )
                                visited.add(key)

            dist += 1
            queue = nextLevel
        return -1

    def isValid(self, i, j, grid, k, eliminatedObstacles):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 0:
            return True
        if grid[i][j] == 2:
            return False
        if grid[i][j] == 1:
            if eliminatedObstacles < k:
                return True
            else:
                return False
        return True


    def startDFS(self, startI, startJ, grid, k, eliminatedObstacles, pathCount):
        if not self.isValid(startI, startJ, grid, k, eliminatedObstacles):
            return False

        if pathCount > self.minPathCount:
            return True

        if startI == len(grid) - 1 and startJ == len(grid[0]) - 1:
            #print self.minPathCount
            self.minPathCount = min( self.minPathCount, pathCount)
            return False

        save = grid[startI][startJ]
        grid[startI][startJ] = 2
        if (self.startDFS(startI + 1, startJ, grid, k, eliminatedObstacles + 1 if save == 1 else eliminatedObstacles, pathCount + 1)):
            return
        if self.startDFS(startI - 1, startJ, grid, k, eliminatedObstacles + 1 if save == 1 else eliminatedObstacles, pathCount + 1):
            return
        if self.startDFS(startI, startJ + 1, grid, k, eliminatedObstacles + 1 if save == 1 else eliminatedObstacles, pathCount + 1):
            return
        if self.startDFS(startI, startJ - 1, grid, k, eliminatedObstacles + 1 if save == 1 else eliminatedObstacles, pathCount + 1):
            return

        grid[startI][startJ] = save
        return False

s=Solution()
print(s.shortestPath(grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1))

s1 = Solution()
print(s1.shortestPath(grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1))

