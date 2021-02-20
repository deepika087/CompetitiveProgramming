__author__ = 'deepika'
"""
17 / 17 test cases passed.
Status: Accepted
Runtime: 172 ms
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        prefix = 1
        for i in range(len(nums)):
            ret.append(prefix)
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = ret[i]*suffix
            suffix = suffix * nums[i]
        return ret

s=Solution()
print s.productExceptSelf([1, 2, 3,4])