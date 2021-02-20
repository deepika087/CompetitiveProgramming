__author__ = 'deepika'

"""
Assume we have a 2D array of integers, a grid. We have a bug who starts at the upper left corner
and wants to walk across the grid to the lower right corner. The bug can only move down or right.

Say the integers represent number of candies at that particular spot. The bug wants to eat the
most candies during its journey from the upper left corner to the lower right corner.

Write a function that calculates the most number of candies the bug can possible eat, keeping in
mind it can only move down or right.


Example:

[[3, 9, 9],
 [9, 0, 0],
 [9, 2, 0]]

 The bug can eat at most 23 candies

N x N
 N>=2

 arr[i, j] = max(arr[i-1, j], arr[i, j-1]) + matrix[i][j]

arr[m-1, n-1]
"""
class Solution:
    def collectMaxCandies(self, matrix):

        N = len(matrix)

        dp = [ [0 for _ in range(N)] for _ in range(N) ]

        dp[0][0] = matrix[0][0]
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue

                onRowAbove = dp[i-1][j] if i > 0 else 0
                onColLeft = dp[i][j - 1] if j > 0 else 0

                dp[i][j] = max ( onRowAbove, onColLeft)  + matrix[i][j]

        print(dp)
        self.retracePath(dp)

        return dp[N-1][N-1]

    def retracePath(self, dp):
        N = len(dp)
        result = [ (N-1, N-1) ]

        i = N-1
        j = N-1
        while i >= 0 and j >= 0:
            if i == 0 and j == 0:
                print(result)
                return

            onLeft = dp[i][j-1] if j-1 >= 0 else -1
            onTop = dp[i-1][j] if i-1 >= 0 else -1

            if onLeft > onTop:
                result.insert(0, (i, j-1) )
                j -= 1
            else:
                result.insert(0, (i-1, j) )
                i -= 1

s=Solution()
matrix = [[3, 9, 9],
 [9, 0, 0],
 [9, 2, 0]]
print(s.collectMaxCandies( matrix ))



matrix2 = [[9, 9, 9, 9],
             [9, 0, 0, 9],
             [9, 0, 0, 9],
             [9, 0, 0, 9]]  # ans: 63
print(s.collectMaxCandies( matrix2 ))


matrix3 = [[9, 9, 9],
            [9, 9, 9],
            [9, 9, 9]]  # ans: 45
print(s.collectMaxCandies( matrix3 ))


matrix4 = [  [6, 8, 1, 2, 1],
             [7, 4, 8, 8, 2],
             [2, 4, 9, 0, 5],
             [7, 5, 3, 8, 9],
             [8, 1, 9, 9, 0]] # ans: 56
print(s.collectMaxCandies(matrix4 ))
