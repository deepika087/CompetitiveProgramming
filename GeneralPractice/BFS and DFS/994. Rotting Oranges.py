__author__ = 'deepika'


"""
Runtime: 48 ms, faster than 34.52% of Python online submissions for Rotting Oranges.
Memory Usage: 12.7 MB, less than 64.29% of Python online submissions for Rotting Oranges.
"""

class Solution(object):
    def isValid(self, i, j, m, n, grid):
        #print(i, j)
        if i < 0 or j < 0:
            return False

        if i >= m or j >= n:
            return False

        if grid[i][j] in [0, 2]:
            return False
        return True

    def findneighbours(self, i, j, m, n, grid):

        result = []
        dirs = [ [-1, 0], [1, 0], [0, 1], [0, -1]]

        for dir in dirs:
            newX = i + dir[0]
            newY = j + dir[1]

            if self.isValid(newX, newY, m, n, grid):
                result.append( (newX, newY) )
        return result

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        #print(m, n)

        queue = []
        visited = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.append( (i, j))
                if grid[i][j] == 2: # rotten
                    queue.append( (i, j))
                    visited.append( (i, j))

        if len(visited) == m*n:
            return 0 #already everything is rotten

        time = 0
        while len(queue) > 0:
            nextLevel = []

            if len(visited) == m*n:
                    return time

            while len(queue) > 0:
                popped = queue.pop()

                neighbours = self.findneighbours(popped[0], popped[1], m, n, grid)
                if len(neighbours) > 0:
                    nextLevel.extend(neighbours)
                    for _n in neighbours:
                        visited.append( (_n[0], _n[1]) )
                        grid[_n[0]][_n[1]] = 2

            queue = nextLevel
            time += 1
        return -1

s=Solution()
print(s.orangesRotting([[1],[2],[1],[1]]))
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0,2]]))
