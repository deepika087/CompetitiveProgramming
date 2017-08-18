# This question is different that FB question
"""
49 / 49 test cases passed.
Status: Accepted
Runtime: 72 ms
"""
class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = 0
        while(left < right):
            maxWater = max(maxWater, min(height[left], height[right])* (right - left))
            if (height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
        return maxWater

s=Solution()
print s.maxArea([1, 2, 3, 4, 5])
print s.maxArea([5, 4, 3, 2, 1])
#print s.maxArea([5, 4, 30, 12, 11])
print s.maxArea([1, 1])
print s.maxArea([1, 2, 1])
print s.maxArea([1,2,4,3]) #expected 4
print s.maxArea([2,3,10,5,7,8,9])
