
"""
463. Island Perimeter
"""
class Solution(object):
    def findSurroundingNumberOfZeros(self, i, j, M, N, grid):
        count = 0
        if ( i-1 >= 0 and grid[i-1][j] == 0):
            count = count + 1
        if ( i - 1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 0):
            count = count + 1
        if ( i - 1 >= 0 and j+1 < N  and grid[i-1][j+1] == 0):
            count = count + 1
        if (  j-1 >= 0  and grid[i][j-1] == 0):
            count = count + 1
        if ( j+1 < N  and grid[i][j+1] == 0):
            count = count + 1
        if ( i +1 < M and j-1 >= 0 and grid[i+1][j-1] == 0):
            count = count + 1
        if ( i +1 < M  and grid[i+1][j] == 0):
            count = count + 1
        if ( i +1 < M and j+1 < N and grid[i+1][j+1] == 0):
            count = count + 1
        return count

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        param = 0
        for i in range(M):
            for j in range(N):
                if (grid[i][j] == 1):
                    surrounding = self.findSurroundingNumberOfZeros(i, j, M, N, grid)
                    if (surrounding == 5):
                        param = param + 3
                        print " For (" + str(i), str(j) + ") adding 3 "
                    elif (surrounding == 1):
                        param = param + 1
                        print " For (" + str(i), str(j) + ") adding 1"
                    elif(surrounding == 2):
                        if (j == N-1 or i == M-1 or i == 0 or j == 0):
                            param = param + 3
                            print " For (" + str(i), str(j) + ") adding 3"
                        else:
                            param = param + 2
                            print " For (" + str(i), str(j) + ") adding 3"
                    elif(surrounding == 8):
                            param = param + 4
                            print " For (" + str(i), str(j) + ") adding 4"
                    elif(surrounding == 3):
                        param = param + 2
                    else:
                        print " No info found for surroudning = ", surrounding, i, j
        return param
s=Solution()
print s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
)