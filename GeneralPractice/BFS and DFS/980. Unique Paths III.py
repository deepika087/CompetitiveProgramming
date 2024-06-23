__author__ = 'deepika'

"""
Details
Runtime: 84 ms, faster than 24.47% of Python online submissions for Unique Paths III.
Memory Usage: 13 MB, less than 5.32% of Python online submissions for Unique Paths III.
Next challenges
"""
class Solution(object):


    result = 0
    numofzeroes = 0
    paths = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = [ [False for _ in range(n) ]  for _ in range(m)]
        iSave, jSave = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    iSave, jSave = i, j
                elif grid[i][j] == 0:
                    self.numofzeroes += 1

        print("Num of zeroes : ", self.numofzeroes)
        steps = 0
        self.startdfs(iSave, jSave, grid, visited, m, n, steps)
        return self.result

    def startdfs(self, startI, startJ, grid, visited, m, n, steps):
        if startI < 0 or startJ < 0 or startI >= m or startJ >= n or grid[startI][startJ] == -1 or visited[startI][startJ]:
            return False
        if grid[startI][startJ] == 2 and steps-1 == self.numofzeroes:
            self.result += 1
            return True
        visited[startI][startJ] = True
        self.startdfs(startI + 1, startJ, grid, visited, m, n, steps + 1)
        self.startdfs(startI - 1, startJ, grid, visited, m, n, steps + 1)
        self.startdfs(startI, startJ + 1, grid, visited, m, n, steps + 1)
        self.startdfs(startI, startJ - 1, grid, visited, m, n, steps + 1)
        visited[startI][startJ] = False
        return False

s1=Solution()
print("T1")
print(s1.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print("T2")
s2=Solution()
print(s2.uniquePathsIII( [[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print("T3")
s3=Solution()
print(s3.uniquePathsIII( [[0,1],[2,0]]))
s4=Solution()
print(s4.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))


