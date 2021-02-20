__author__ = 'deepika'

"""
Runtime: 136 ms, faster than 65.90% of Python online submissions for Number of Islands.
Memory Usage: 20.1 MB, less than 28.78% of Python online submissions for Number of Islands.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.startDFS(i, j, grid)
                    count += 1
        return count

    def isValid(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == '1': #only available then send true
            return True
        return False

    def startDFS(self, startI, startJ, grid):

        if not self.isValid(startI, startJ, grid):
            return
        grid[startI][startJ] = '2'
        self.startDFS(startI + 1, startJ, grid)
        self.startDFS(startI, startJ + 1, grid)
        self.startDFS(startI - 1, startJ, grid)
        self.startDFS(startI, startJ - 1, grid)

s=Solution()
print(s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))