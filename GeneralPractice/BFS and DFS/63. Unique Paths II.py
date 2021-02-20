__author__ = 'deepika'

"""
TLE because it should be done with DP but the idea here is right.
result[i][j] = result[i-1][j] + result[i][j+1]
"""
class Solution(object):
    def uniquePathsWithObstaclesSpaceUnoptimized(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        if m == 0:
            return []
        n = len(obstacleGrid[0])

        visited = [ [ False for i in range(n)] for j in range(m)]
        #visited[0][0] = True

        result = []
        path_so_far = [ (0, 0) ]
        self.startDFS(0, 0, m, n, path_so_far, result, visited, obstacleGrid)
        return len(result)

    def startDFSSpaceUnoptimized(self, i, j, m, n, path_so_far, result, visited, obstacleGrid):
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        if visited[i][j] == True:
            return False

        if obstacleGrid[i][j] == 1:
            return False

        if i == m-1 and j == n-1:
            result.append(path_so_far)

        visited[i][j] = True
        self.startDFS(i+1, j, m, n, path_so_far + [ (i+1, j)], result, visited, obstacleGrid)
        self.startDFS(i, j+1, m, n, path_so_far + [ (i, j+1)], result, visited, obstacleGrid)
        visited[i][j] = False


    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            else:
                return 0

        count = [0]
        self.startDFS(0, 0, m, n, count, obstacleGrid)
        return count[0]

    def startDFS(self, i, j, m, n, count, obstacleGrid):
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        if obstacleGrid[i][j] == 2:
            return False

        if obstacleGrid[i][j] == 1:
            return False

        if i == m-1 and j == n-1:
            return True

        obstacleGrid[i][j] = 2
        if (self.startDFS(i+1, j, m, n, count, obstacleGrid)):
            count[0] += 1
        if (self.startDFS(i, j+1, m, n, count, obstacleGrid)):
            count[0] +=1
        obstacleGrid[i][j] = 0
        return False


s=Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))

print(s.uniquePathsWithObstacles([
  [0]
]))

print(s.uniquePathsWithObstacles([
  [0],
  [0],
  [0]
]))

print(s.uniquePathsWithObstacles([
  [1],
  [1],
  [1]
]))