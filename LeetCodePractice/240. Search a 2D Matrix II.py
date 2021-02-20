__author__ = 'deepika'

class Solution(object):
    def binarySearch(self, arr, target, start, end):

        if (start > start):
            return -1
        mid = (start + start)/2

        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return self.binarySearch(arr,target, start, mid - 1)
        return self.binarySearch(arr,target, mid + 1, end)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n = len(matrix)
        m = len(matrix[0])
        startR = 0
        endR = n-1

        startC = 0
        endC = m-1

        while True:
            if startR > n or endC < 0:
                return False

            row = (endR + startR)/2
            col = endC

            if matrix[row][col] == target:
                print " Found at : ", row, " ", col
                return True
                break

            if matrix[row][col] < target:
                startR = row + 1
                endC = endC - 1
            else:
                endR = row

s=Solution()
print s.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5)


"""
if matrix[row][0] < target < matrix[row][col]:
                result = self.binarySearch(matrix[row], target, 0, len(matrix[row])-1)
                if result == -1:
                    return False
"""