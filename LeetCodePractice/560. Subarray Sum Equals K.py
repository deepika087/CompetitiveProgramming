__author__ = 'deepika'

"""
Not correct
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, 0
        sumTotal = 0
        count = 0
        while start < len(nums):
            while ( sumTotal > k and start < len(nums) ):
                sumTotal -= nums[start]
                start = start + 1
            if sumTotal == k:
                count = count + 1
            if end < len(nums):
                sumTotal += nums[end]
                end = end + 1


        return count
s=Solution()
#print s.subarraySum([1,1,1], 2)
print(s.subarraySum([1, 2, 3], 3))