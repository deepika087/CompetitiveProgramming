__author__ = 'deepika'

"""
Runtime: 24 ms, faster than 60.56% of Python online submissions for First Missing Positive.
Memory Usage: 13.5 MB, less than 34.61% of Python online submissions for First Missing Positive.

"""
class Solution:
    def firstMissingPositive(self, nums):

        constant = len(nums) + 100

        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = constant

        for i in range(len(nums)):
            idx = abs(nums[i])
            if (idx < len(nums) + 1) and (nums[idx - 1] > 0):
                nums[idx - 1] *= -1

        res = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] > 0:
                res = i + 1
                break

        return res

s=Solution()
print(s.firstMissingPositive([3, 4, -4, -8]))