"""

127 / 127 test cases passed.
Status: Accepted
Runtime: 112 ms
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
        j=len(matrix[0]) - 1

        while (i < len(matrix) and j >= 0):
            if (matrix[i][j] == target):
                return True
            if (matrix[i][j] > target):
                j = j - 1
            else:
                i = i + 1
        return False


s=Solution()
matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print s.searchMatrix(matrix, 5)
print s.searchMatrix(matrix, 31)

