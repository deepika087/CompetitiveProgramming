__author__ = 'deepika'


"""
Success
Details
Runtime: 432 ms, faster than 85.71% of Python online submissions for Capacity To Ship Packages Within D Days.
Memory Usage: 15.7 MB, less than 76.19% of Python online submissions for Capacity To Ship Packages Within D Days.

The idea is say you fnd capacity x.. now x could suffice in a specific scenario or grouping.

For ex:1,2,3,1,1 . Capacity = 3, D = 4
1, 2
3
1, 1 gives you 3 days.

1
2
3
1  1 gives you 4 days

So for a capacity if you are getting days < D that could be a potential too. The solution doesn't handle the positing of the
items. Just that somehow capacity should suffice.

K = maxCapacity - minCapacity
time complexity: O(K log K) * O(n) w

"""

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """

        minCapacity = max(weights)
        maxCapacity = sum(weights)
        ans = -1
        while minCapacity <= maxCapacity: # this <= is important here
            midCapacity = (minCapacity + maxCapacity) / 2

            expectedDays = self.canHandle(weights, midCapacity)
            if expectedDays > D:
                minCapacity = midCapacity + 1
            else:
                ans = midCapacity
                maxCapacity = midCapacity - 1
        return ans

    def canHandle(self, weights, capacity):

        days_so_far = 1
        total = 0
        for i in range(len(weights)):
            total += weights[i]

            if total > capacity:
                days_so_far += 1
                total = weights[i]

        return days_so_far

s=Solution()
print(s.shipWithinDays( weights = [1,2,3,4,5,6,7,8,9,10], D = 5))
print(s.shipWithinDays(weights = [3,2,2,4,1,4], D = 3))
print(s.shipWithinDays(weights = [1,2,3,1,1], D = 4))
print(s.shipWithinDays([10,50,100,100,50,100,100,100], 5))



