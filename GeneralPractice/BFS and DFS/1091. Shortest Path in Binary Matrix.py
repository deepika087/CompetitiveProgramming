from typing import List
import sys


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return -1

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1

        return self.bfs(0, 0, grid)

    def getValidNeighbours(self, x, y, grid):

        neighbours = []
        for dir in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            nx = x + dir[0]
            ny = y + dir[1]

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) \
                    and grid[nx][ny] == 0:
                neighbours.append((nx, ny))
        return neighbours

    def bfs(self, i, j, grid):
        queue = [(i, j, 1)]
        grid[i][j] = 1
        while queue:
            x, y, count_so_far = queue.pop(0)

            # print("Exploring index: " + str(x) + "," + str(y))
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return count_so_far # this was returning wrong answer cz of pop(-1)

            for neighbour in self.getValidNeighbours(x, y, grid):
                grid[neighbour[0]][neighbour[1]] = 1 #Rather than using visited use the grid itself it is a simpler operation
                queue.append((neighbour[0], neighbour[1], count_so_far + 1))

        return -1