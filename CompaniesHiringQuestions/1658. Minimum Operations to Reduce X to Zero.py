__author__ = 'deepika'

"""
Intuition is when you remove elements from left or right. Basically you are left iwth a subarray.
with sum = sum(nums) - x
"""

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        cur_sum = 0
        numOfElements = -1
        left = 0
        for i in range(len(nums)):
            cur_sum += nums[i]

            while cur_sum >= target:
                if cur_sum == target:
                    numOfElements = max(numOfElements, i - left + 1)
                cur_sum -= nums[left]
                left += 1
        return len(nums) - numOfElements if numOfElements != -1 else -1

s=Solution()
assert s.minOperations(nums = [1,1,4,2,3], x = 5) == 2
assert  s.minOperations(nums = [5,6,7,8,9], x = 4) == -1
