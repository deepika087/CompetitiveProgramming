__author__ = 'deepika'

import sys
"""
Runtime: 136 ms, faster than 65.90% of Python online submissions for Number of Islands.
Memory Usage: 20.1 MB, less than 28.78% of Python online submissions for Number of Islands.
"""
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        max_count = 0
        for i in range(m):
            for j in range(n):
                count = self.startDFS(i, j, grid)
                max_count = max(max_count, count)
        return max_count

    def findValidNeighbours(self, popped, visited, grid):
        result = []
        isUsed = popped[3]
        for dir in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            new_i = popped[0] + dir[0]
            new_j = popped[1] + dir[1]
            key = str(new_i) + '-' + str(new_j)
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and key not in visited:
                if grid[new_i][new_j] == 1:
                    result.append((new_i, new_j))
                if grid[new_i][new_j] == 0 and not isUsed:
                    result.append((new_i, new_j))
        return result


    def startDFS(self, i, j, grid):

        stack = [(i, j, 1, True if grid[i][j] == 0 else False)]
        count = 0
        visited = set()
        while stack:
            popped = stack.pop(-1)
            count = max(count, popped[2])
            visited.add(str(popped[0]) + '-' + str(popped[1]))
            neighbours = self.findValidNeighbours(popped, visited, grid)

            if len(neighbours) == 0:
                continue

            stack += [popped]
            nei = neighbours[0]
            if grid[nei[0]][nei[1]] == 0:
                stack += [(nei[0], nei[1], popped[2] + 1, True)]
            else:
                stack += [(nei[0], nei[1], popped[2] + 1, popped[3])]
        return count





s=Solution()
print(s.largestIsland(grid = [[1,0],[0,1]]))
print(s.largestIsland(grid = [[1,1],[1,0]]))
print(s.largestIsland(grid = [[1,1],[1,1]]))
print(s.largestIsland(grid = [[1,1, 1],[1, 0, 1], [0, 0, 1]]))
print(s.largestIsland([[0,0],[0,0]]))
print(s.largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]]))
"""
print(s.largestIsland(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(s.largestIsland(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
"""