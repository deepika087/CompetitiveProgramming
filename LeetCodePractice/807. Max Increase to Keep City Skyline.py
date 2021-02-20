__author__ = 'deepika'
"""

133 / 133 test cases passed.
Status: Accepted
Runtime: 64 ms
"""

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col_max = self.getColMax(grid)
        row_max = self.getRowMax(grid)
        #print col_max
        #print row_max
        totalSum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == col_max[j]:
                    continue
                elif grid[i][j] == row_max[i]:
                    continue
                else:
                    totalSum +=  min(row_max[i], col_max[j]) - grid[i][j]
                    grid[i][j] = min(row_max[i], col_max[j])

        return totalSum

    def getColMax(self, grid):
        result = [0 for i in range(len(grid[0]))]
        for j in range(len(grid[0])):
            result[j] = grid[0][j]
            for i in range(1, len(grid)):
                result[j] = max(result[j], grid[i][j])
        return result


    def getRowMax(self, grid):
        result = [0 for i in range(len(grid))]
        for i in range(len(grid)):
            result[i] = max(grid[i])
        return result

s= Solution()
print s.maxIncreaseKeepingSkyline(
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ])