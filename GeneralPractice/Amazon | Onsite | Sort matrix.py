__author__ = 'deepika'

"""
Given a 2d array in which each row is sorted and rotated, you need to come up with an algorithm which efficiently sort the entire 2d matrix in descenting order.

eg:
input: arr[][] = {
{41, 45, 20, 21},
{1 ,2, 3, 4},
{30, 42, 43, 29 },
{16, 17, 19, 10}
}

output: {
{ 45, 43, 42, 41},
{30, 29, 21, 20},
{19, 17, 16, 10},
{4, 3, 2, 1}
}

time complexity analysis:
find pivot for  one row with c columns : O(log c)
find pivot with r rows : O(r log c)

Merge k- arrays:
O(r*c * log c)

Heap itself will be of size 'c'

Overall: O(r log c) + O(r*c * log c)

Space: O(c). excluding the result itself but priority queue of size 'c'
"""

import heapq
import copy
class Solution:

    def sortMatrix(self, matrix):

        m = len(matrix)
        if m == 0:
            return []

        n = len(matrix[0])

        originalPivot = [-1] * m
        for i in range(m):
            originalPivot[i] = self.findPivot(matrix[i])
            if originalPivot[i] == -1: #To stop the infinite recursion in case when array has no pivot.
                originalPivot[i] = n-1

        return self.heapifyAndSort(matrix, originalPivot, n)

    def heapifyAndSort(self, matrix, originalPivot, n):

        pq = []

        currentPivot = copy.copy(originalPivot)

        result = []
        for i in range(len(currentPivot)):
            if currentPivot[i] >= 0:
                heapq.heappush(pq, [ -matrix[i][currentPivot[i]], i ]) #Because it is the max heap add the negative value.

        while pq:
            popped = heapq.heappop(pq)
            result.append( -popped[0] )

            idx = self.getNextIndexFromArray(currentPivot, originalPivot, popped[1], n)

            if idx == -2: #Means all consumed from this specific row of the matrix
                continue

            heapq.heappush(pq, [ -matrix[popped[1]][idx], popped[1]  ] )

        return result

    def getNextIndexFromArray(self, currentPivot, originalPivot, i, n):

        if currentPivot[i] > 0:
            currentPivot[i] = currentPivot[i] - 1
        elif currentPivot[i] == 0:
            currentPivot[i] = n-1
        elif currentPivot[i] == -1: # This array is not pivoted. Since we have already added column n-1. So, the next element to be processed will be from column n-1
            currentPivot[i] = n-2

        if currentPivot[i] == originalPivot[i]: # whenever you reach the point that you have already seen just break.
                return -2

        return currentPivot[i]


    def findPivot(self, array):

        lo = 0
        hi = len(array) - 1

        while lo < hi:
            mid = hi - (hi - lo)/2

            if mid == 0:
                return len(array) - 1 #this means already sorted
            if mid < hi and array[mid] > array[mid + 1]: #3, 4, 5, 1, 2,
                return mid

            if mid > lo and array[mid] < array[mid - 1]:
                return mid - 1


            if array[lo] > array[mid]: #consider example 4, 5, 1, 2, 3..mid = 1 but 4 > 1 so search in left side.
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

s=Solution()
print(s.sortMatrix([
    [41, 45, 20, 21],
    [1 ,2, 3, 4],
    [30, 42, 43, 29],
    [16, 17, 19, 10]
]))

print(s.sortMatrix([
    [1, 2, 3, 4],
    [5 ,6, 7, 8],
    [9, 10, 11, 12]
]))