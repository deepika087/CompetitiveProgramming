__author__ = 'deepika'

"""
Given two arrays(of different lengths),int lower,int upper, count how many pairs have the following property
lower <= a[i]*a[i] + b[j]*b[j] <= higher

lower - a[i]*a[i] <= b[j]*b[j] <= higher -  a[i]*a[i]

Let X = lower - a[i]*a[i]
Let Y = higher -  a[i]*a[i]
Let p = b[j]

X <= p2 <= Y
sqrt(X) <= p <= sqrt(Y)

Now, do binary searches to find possible values of p in array b.

Time complexity : O(n log n) because for each a[i] we will do 2 binary search calls.
Assuming: Arr is sorted + size of both the arrays is approx n
"""

import math
class Solution:

    def findPairsBruteForce(self, a, b, lo, hi):
        if len(a) > len(b):
            return self.findPairsBruteForce(b, a, lo, hi)

        count = 0
        a.sort()
        b.sort()

        for i in range(len(a)):
            for j in range(len(b)):
                if lo <= a[i]*a[i] +b[j]*b[j] <= hi:
                    count += 1
        return count

    """
    Basically we have to find first element in arr that is greater than or equal to num
    """
    def findLowerBound(self, arr, num): # first index: sqrt(x) <= y

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = right - (right - left)/2
            if arr[mid] >= num:
                if mid == 0 or mid - 1 >= 0 and arr[mid-1] < num:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

        return -1

    """
    find the first element in arr that is less than or equal to num
    """
    def findUpperBound(self, arr, num):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = right - (right - left)/2
            if arr[mid] <= num:
                if mid == len(arr)-1 or mid + 1 < len(arr) and arr[mid+1] > num:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1

        return -1

    def findPairsOptimized(self, a, b, lo, hi):
        if lo < 0 or hi < 0 :
            return 0 # sum of two squares can never be less than zero

        if len(a) > len(b):
            return self.findPairsBruteForce(b, a, lo, hi)

        a.sort()
        b.sort()

        count = 0
        for i in range(len(a)):
            loprime = lo - a[i] * a[i] if lo > a[i] * a[i] else lo
            hiprime = hi - a[i] * a[i]

            if a[i] > math.sqrt(hi) + 1 or hiprime < 0 :
                break

            index1 = self.findLowerBound(b, math.sqrt(loprime))
            if index1 == -1:
                continue
            index2 = self.findUpperBound(b, int(math.sqrt(hiprime)))
            if index2 == -1 or index2 < index1:
                continue
            count += index2 - index1 + 1
        return count

s=Solution()
assert s.findPairsOptimized([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], lo=25, hi=80) == s.findPairsBruteForce([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], lo=25, hi=80)
assert s.findPairsOptimized([-1, 12, 31, 4, 15], [9, 7, 8, 16, 15, 9, 10], lo=25, hi=80) == s.findPairsBruteForce([-1, 12, 31, 4, 15], [9, 7, 8, 16, 15, 9, 10], lo=25, hi=80)
assert s.findPairsOptimized([-2, 2, 9, 4, 15, 0, 8, 7], [9, 7, 8, 16, 15, 9, 10], lo=25, hi=1000) == s.findPairsBruteForce([-2, 2, 9, 4, 15, 0, 8, 7], [9, 7, 8, 16, 15, 9, 10], lo=25, hi=1000)
assert s.findPairsOptimized([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], lo=0, hi=80) == s.findPairsBruteForce([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], lo=0, hi=80)
assert s.findPairsOptimized([-1, 12, 31, 4, 15], [9, 7, 8, 16, 15, 9, 10], lo=1, hi=200) == s.findPairsBruteForce([-1, 12, 31, 4, 15], [9, 7, 8, 16, 15, 9, 10], lo=1, hi=200)
assert s.findPairsOptimized([-2, 2, 9, 4, 15, 0, 8, 7], [9, 7, 8, 16, 15, 9, 10], lo=10, hi=1000) == s.findPairsBruteForce([-2, 2, 9, 4, 15, 0, 8, 7], [9, 7, 8, 16, 15, 9, 10], lo=10, hi=1000)

