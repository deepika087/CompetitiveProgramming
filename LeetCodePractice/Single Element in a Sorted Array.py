"""
7 / 7 test cases passed.
Status: Accepted
Runtime: 46 ms

#later realised since it was sorted in any case binary search makes more sense as this code take O(n)
# whereas binary search will take O(log n)
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]
        else:
            xoredSum = 1
            for num in nums:
                xoredSum = xoredSum ^ int(num)
            xoredSum = xoredSum ^ 1
            return xoredSum

s=Solution()
print s.singleNonDuplicate([1,1,2])
print s.singleNonDuplicate([0,1,1])