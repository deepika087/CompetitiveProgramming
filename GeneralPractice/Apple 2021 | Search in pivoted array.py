__author__ = 'deepika'


class Solution:


    def findPivot(self, arr, left, right, n):

        while left <= right:

            if left == right:
                return left

            mid = right - (right - left)/2

            if mid - 1 >= 0 and mid + 1 < n and arr[mid - 1 ] < arr[mid] > arr[mid + 1]:
                return mid

            if (mid - 1 >= 0 and mid + 1 < n and arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]):
                right = mid - 1
            else:
                left = mid + 1
        return n-1 #Strictly increasing array


    def binarySearch(self, arr, left, right, element, greaterThanFunction):

        while left <= right:
            mid = right - (right - left)/2

            if arr[mid] == element:
                return mid
            if greaterThanFunction(arr[mid],  element):
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def findElement(self, arr, x):

        pivot = self.findPivot(arr, 0, len(arr)-1 , len(arr))

        index = self.binarySearch(arr, 0, pivot, x,  lambda x, y : x > y )
        if index == -1:
            index = self.binarySearch(arr, pivot+1, len(arr) - 1, x,  lambda x, y : y > x )
        print("Found x: ", x, " at pivot: ", pivot)
        return index


s=Solution()
s.findElement([1, 2, 3, 4, 5], 5)
s.findElement([4, 5, 3, 2, 1], 5)
s.findElement([5, 4, 3, 2, 1], 2)
s.findElement([-10, -9, -8, -7, -6, -5, 0, 7, 5, 4, 3, 2], -10)
s.findElement([-10, -9, -8, -7, -6, -5, 0, 7, 5, 4, 3, 2], -8)
s.findElement([-10, -9, -8, -7, -6, -5, 0, 7, 5, 4, 3, 2], 2)
s.findElement([-10, -8, 0, 7, 5, 4, 3, 2], -10)
s.findElement([-10, -8, 0, 7, 5, 4, 3, 2], -8)
s.findElement([-10, -8, 0, 7, 5, 4, 3, 2], 2)
