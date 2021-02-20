__author__ = 'deepika'

"""
Runtime: 440 ms, faster than 5.03% of Python online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 16 MB, less than 10.50% of Python online submissions for Range Sum Query 2D - Immutable.

Approach: Is to consider a 2D matrix as a 1D matrix spawned over multiple rows.
Coord(i, j) in 2D matrix -> (i * number of columns + j ) in 1 D matrix.

Create a prefix sum 1 D array where prefixSum[i*n+j] = Sum of all elements (0, 0) to (i, j)
To compute sum from (r1, c1) to (r2, c2) Idea is to traverse from i in range [r1, r2]
sum += sumPrefix(i*n+c2) - sum( i* n + (c1-1) ) i.e prev element of to matrix[i][c1]

if edge case for some (i, c1) something like (3, 0) then Now, previous element to (3, 0) will be
 (2, N-1) that is the last element on the row above.

I think complexity wise. Space complexity remains the same as you are still storing same number of
prefix sum just in 1D format.
Time complexity Practically is the same.

It is just that some time your interviewer might know this solution so they will force you to give the answer in 1D format.
even though complexity wise it remains the same.
"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix) if len(matrix) > 0 else 0
        self.n = len(matrix[0]) if len(matrix) > 0 else 0
        self.prefixSum = [ 0 for i in range(self.m * self.n) ]

        sum_so_far = 0
        for i in range(self.m):
            for j in range(self.n):
                sum_so_far += matrix[i][j]
                self.prefixSum[self.getCordinate(i, j)] = sum_so_far


    def getCordinate(self, i, j):
        return i * self.n + j


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total_sum = 0

        for i in range(row1, row2+1):
            Coord1 = -1
            if col1 - 1 >=0 :
                Coord1 = self.getCordinate(i, col1-1)
            else:                       # now find the previous cooridnate to i, col1
                if i - 1 >=  0:
                    Coord1 = self.getCordinate(i-1, self.n - 1)
            Coord2 = self.getCordinate(i, col2)
            total_sum += self.prefixSum[Coord2] if Coord1 == -1 else self.prefixSum[Coord2] - self.prefixSum[Coord1]
        return total_sum

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

matrixSimple = [[1], [-7]]
#print(matrixSimple)
obj = NumMatrix(matrixSimple)


print(obj.sumRegion(0, 0, 0, 0)) #1
print(obj.sumRegion(1, 0, 1, 0)) #-6
print(obj.sumRegion(0, 0, 1, 0)) #-5

print("New Test case")
obj = NumMatrix(matrix)
print(obj.sumRegion(0, 0, 0, 0)) #3
print(obj.sumRegion(0, 0, 0, 3)) #8
print(obj.sumRegion(2, 1, 4, 3)) #8
print(obj.sumRegion(1, 1, 2, 2)) # 11
print(obj.sumRegion(1, 2, 2, 4)) #12

"""
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]

["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[1],[-7]]],[0,0,0,0],[1,0,1,0],[0,0,1,0]]
"""