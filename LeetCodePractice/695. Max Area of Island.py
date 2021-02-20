__author__ = 'deepika'

"""
726 / 726 test cases passed.
Status: Accepted
Runtime: 109 ms
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[ False for i in range(n)] for j in range(m)]
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    visited[i][j] = True
                    area = self.startDFS(grid, visited, i, j, m, n)
                    #print "running for i =", i, " and j = ", j, " area: ", area
                    maxArea = max(maxArea, area)

        return maxArea

    def getNeighbours(self, grid, visited, i, j, m, n):

        result = []
        if i + 1 < m and not visited[i+1][j] and grid[i+1][j] == 1:
            result.append((i+1, j))
        if i - 1 >= 0 and not visited[i-1][j] and grid[i-1][j] == 1:
            result.append((i-1, j))
        if j + 1 < n and not visited[i][j+1] and grid[i][j+1] == 1:
            result.append((i, j+1))
        if j - 1 >= 0 and not visited[i][j-1] and grid[i][j-1] == 1:
            result.append((i, j-1))

        for (i, j) in result:
            visited[i][j] = 1

        return result

    def startDFS(self, grid, visited, i, j, m, n):
        stack = []
        stack.append((i, j))
        area = 0
        while stack:
            popped = stack.pop()
            area = area + 1
            #visited[popped[0]][popped[1]] = True
            neighbours = self.getNeighbours(grid, visited, popped[0], popped[1], m, n)
            if len(neighbours) == 0 and len(stack) == 0:
                return area

            stack += neighbours

s=Solution()
grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print s.maxAreaOfIsland(grid1)

grid2 = [[0,0,0,0,0,0,0,0]]
print s.maxAreaOfIsland(grid2)

grid3 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print s.maxAreaOfIsland(grid3)
